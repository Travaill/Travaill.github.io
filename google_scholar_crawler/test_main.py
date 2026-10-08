import unittest
from pathlib import Path
from unittest.mock import patch

import main

PROFILE = '''<div id="gsc_prf_in">Shen Lin</div>
<table id="gsc_rsb_st"><tr><td class="gsc_rsb_std">187</td></tr></table>
<table><tbody id="gsc_a_b">
<tr class="gsc_a_tr"><td><a class="gsc_a_at" href="/citations?citation_for_view=ORwuKSYAAAAJ:one">Paper one</a></td><td class="gsc_a_c"><a>0</a></td><td class="gsc_a_y">2026</td></tr>
<tr class="gsc_a_tr"><td><a class="gsc_a_at" href="/citations?citation_for_view=ORwuKSYAAAAJ:two">Paper two</a></td><td class="gsc_a_c"><a></a></td><td class="gsc_a_y">2026</td></tr>
</tbody></table><button id="gsc_bpf_next" disabled></button>'''


class ProfileTests(unittest.TestCase):
    def test_blank_is_not_zero(self):
        d = main.parse_profile(PROFILE, 'ORwuKSYAAAAJ')
        self.assertEqual(d['citedby'], 187)
        self.assertEqual(d['publications']['ORwuKSYAAAAJ:one']['num_citations'], 0)
        self.assertIsNone(d['publications']['ORwuKSYAAAAJ:two']['num_citations'])

    def test_reject_partial_blocked_and_wrong_profile(self):
        for html in ['<div id="captcha"></div>', '<html>Access denied</html>',
                     PROFILE.replace(' disabled', ''), PROFILE.replace('ORwuKSYAAAAJ:one', 'other:one')]:
            with self.subTest(html=html), self.assertRaises(ValueError):
                main.parse_profile(html, 'ORwuKSYAAAAJ')

    def test_robots_disallow_stops_before_profile(self):
        with patch.object(main, 'read_url', return_value='User-agent: *\nDisallow: /') as read:
            with self.assertRaises(ValueError):
                main.main()
            self.assertEqual(read.call_count, 1)

    def test_failed_fetch_does_not_write(self):
        with patch.object(main, 'read_url', side_effect=OSError('Forbidden')), patch.object(Path, 'write_text') as write:
            with self.assertRaises(OSError):
                main.main()
            write.assert_not_called()


if __name__ == '__main__':
    unittest.main()
