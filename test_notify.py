from unittest.mock import Mock, patch

from notify import send_telegram


def test_skips_without_credentials(monkeypatch):
    monkeypatch.delenv("TELEGRAM_BOT_TOKEN", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
    with patch("notify.requests.post") as post:
        assert send_telegram("hi") is False
    post.assert_not_called()


def test_sends_message(monkeypatch):
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "t")
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "1")
    with patch("notify.requests.post", return_value=Mock(ok=True)) as post:
        assert send_telegram("hi") is True
    assert post.call_args.kwargs["data"] == {"chat_id": "1", "text": "hi"}
