# Scholar citation snapshots

The existing workflow attempts an update daily at 08:00 UTC and after a Pages build. This is not real-time synchronization. No new API key or service is required; the existing public profile is the default when `GOOGLE_SCHOLAR_ID` is unset.

The updater checks Google's robots.txt before requesting one public profile page (`user=` first, no pagination). It stops on disallowed access, redirects, HTTP errors, CAPTCHA, incomplete data or unexpected counts. It does not retry, rotate proxies or solve challenges. This follows the access guidance at https://scholar.google.com/intl/en/scholar/help.html .

Only successful fetches publish to `google-scholar-stats`, using a normal Git push. Failures leave that branch unchanged. Empty citation cells become JSON null, distinct from an explicit zero. Successful snapshots have an ISO UTC `updated` timestamp and `collection_method: automated`.

The homepage includes a separately verified fallback in `_data/scholar_snapshot.json` (2026-10-04T15:59:04Z). This is a manual research snapshot, not evidence that scheduled fetching succeeded. The frontend accepts newer snapshots only, reports source timestamps and data older than 48 hours, and retains displayed data when a request fails. The existing CDN may add delay. Publication additions and metadata remain editorial changes; the scheduled job updates counts only.

Tests (no Scholar access):

```sh
python -m pip install -r google_scholar_crawler/requirements.txt
python -m unittest discover -s google_scholar_crawler -v
node google_scholar_crawler/test_frontend.js
```
