from unittest.mock import Mock, patch

import requests

from main import check_site, load_sites


def test_site_ok():
    fake_response = Mock(status_code=200)
    with patch("main.requests.get", return_value=fake_response):
        assert check_site("https://example.com") == ("https://example.com", 200)


def test_site_error():
    with patch("main.requests.get", side_effect=requests.ConnectionError("boom")):
        url, result = check_site("https://example.com")
    assert url == "https://example.com"
    assert "ОШИБКА" in result


def test_load_sites_skips_comments_and_blanks(tmp_path):
    f = tmp_path / "sites.txt"
    f.write_text("# комментарий\n\nhttps://a.com\n  https://b.com  \n", encoding="utf-8")
    assert load_sites(f) == ["https://a.com", "https://b.com"]
