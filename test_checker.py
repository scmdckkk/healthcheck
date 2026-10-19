from unittest.mock import patch

from checker import run_once


def test_run_once_saves_each_site():
    with patch("checker.load_sites", return_value=["https://a.com", "https://b.com"]), \
         patch("checker.check_site", side_effect=[("https://a.com", 200), ("https://b.com", "ОШИБКА: x")]), \
         patch("checker.save_check") as save:
        run_once()
    assert save.call_count == 2
    save.assert_any_call("https://a.com", 200, True)
    save.assert_any_call("https://b.com", "ОШИБКА: x", False)
