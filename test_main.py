from unittest.mock import Mock, patch

import requests

from main import check_site


def test_site_ok():
    fake_response = Mock(status_code=200)
    with patch("main.requests.get", return_value=fake_response):
        assert check_site("https://example.com") == ("https://example.com", 200)


def test_site_error():
    with patch("main.requests.get", side_effect=requests.ConnectionError("boom")):
        url, result = check_site("https://example.com")
    assert url == "https://example.com"
    assert "ОШИБКА" in result
