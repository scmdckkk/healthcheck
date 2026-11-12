from unittest.mock import patch

from checker import run_once


def run_with(previous):
    with patch("checker.load_sites", return_value=["https://a.com", "https://b.com"]), \
         patch("checker.check_site", side_effect=[("https://a.com", 200), ("https://b.com", "ОШИБКА: x")]), \
         patch("checker.last_ok", side_effect=previous), \
         patch("checker.save_check") as save, \
         patch("checker.send_telegram") as send:
        run_once()
    return save, send


def test_notifies_only_on_state_change():
    save, send = run_with([True, True])  # a остался живым, b упал
    assert save.call_count == 2
    send.assert_called_once()
    assert "https://b.com" in send.call_args.args[0]


def test_no_notification_on_first_check():
    _, send = run_with([None, None])
    send.assert_not_called()
