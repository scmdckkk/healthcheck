from unittest.mock import patch

from app import app

ROWS = [{"url": "https://a.com", "status": "200", "ok": True, "checked_at": "now"}]


def test_api_status():
    with patch("app.latest_checks", return_value=ROWS):
        resp = app.test_client().get("/api/status")
    assert resp.status_code == 200
    assert resp.get_json() == ROWS


def test_index_page():
    with patch("app.latest_checks", return_value=ROWS):
        resp = app.test_client().get("/")
    assert resp.status_code == 200
    assert "https://a.com" in resp.get_data(as_text=True)
