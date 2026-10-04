"""Read the public Scholar profile once; never replace data on a failed fetch."""
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse
from urllib.request import Request, HTTPRedirectHandler, build_opener

from bs4 import BeautifulSoup
from protego import Protego


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("Scholar redirected the request; stopping without retry.")


def read_url(url):
    request = Request(url, headers={"User-Agent": "AcademicHomepageCitationUpdater/1.0"})
    with build_opener(NoRedirect).open(request, timeout=30) as response:
        return response.read().decode("utf-8")


def parse_profile(html, scholar_id):
    soup = BeautifulSoup(html, 'html.parser')
    if soup.select_one('#captcha, .g-recaptcha, form[action*="sorry"]'):
        raise ValueError('Scholar requested verification; stopping without retry.')
    name = soup.select_one('#gsc_prf_in')
    total = soup.select_one('#gsc_rsb_st .gsc_rsb_std')
    rows = soup.select('#gsc_a_b .gsc_a_tr')
    if not name or not total or not rows:
        raise ValueError('Missing Scholar profile data; retaining previous snapshot.')
    def count(text):
        text = text.strip().replace(',', '')
        if not text:
            return None
        if not text.isdecimal():
            raise ValueError('Unexpected citation count.')
        return int(text)
    publications = {}
    for row in rows:
        title = row.select_one('a.gsc_a_at')
        citations = row.select_one('.gsc_a_c')
        if not title or citations is None:
            raise ValueError('Incomplete publication row.')
        paper_id = parse_qs(urlparse(title.get('href', '')).query).get('citation_for_view', [''])[0]
        if not paper_id.startswith(scholar_id + ':') or paper_id in publications:
            raise ValueError('Invalid or duplicate publication ID.')
        year = row.select_one('.gsc_a_y')
        publications[paper_id] = {
            'author_pub_id': paper_id,
            'bib': {'title': title.get_text(' ', strip=True),
                    'pub_year': year.get_text(' ', strip=True) if year else ''},
            'num_citations': count(citations.get_text('', strip=True)),
        }
    next_button = soup.select_one('#gsc_bpf_next')
    if next_button is not None and not next_button.has_attr('disabled'):
        raise ValueError('Profile exceeds one page; refusing a partial snapshot.')
    total_count = count(total.get_text('', strip=True))
    if total_count is None:
        raise ValueError('Missing total citation count.')
    return {'name': name.get_text(' ', strip=True), 'scholar_id': scholar_id,
            'citedby': total_count, 'publications': publications}


def main():
    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip() or 'ORwuKSYAAAAJ'
    url = 'https://scholar.google.com/citations?' + urlencode({
        'user': scholar_id, 'hl': 'en', 'pagesize': 100})
    # No proxy rotation, CAPTCHA solving, or retries on access restrictions.
    robots = Protego.parse(read_url('https://scholar.google.com/robots.txt'))
    if not robots.can_fetch(url, 'AcademicHomepageCitationUpdater'):
        raise ValueError('Scholar robots.txt disallows this URL; stopping.')
    data = parse_profile(read_url(url), scholar_id)
    data['updated'] = datetime.now(timezone.utc).isoformat(timespec='seconds')
    data['source'] = url
    data['collection_method'] = 'automated'
    results = Path('results')
    results.mkdir(exist_ok=True)
    (results / 'gs_data.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    badge = {'schemaVersion': 1, 'label': 'citations', 'message': str(data['citedby'])}
    (results / 'gs_data_shieldsio.json').write_text(json.dumps(badge) + '\n', encoding='utf-8')
    print(f"Collected {len(data['publications'])} publications at {data['updated']}")


if __name__ == '__main__':
    main()
