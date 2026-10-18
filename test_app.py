from unittest.mock import patch

from app import app


def test_api_status():
    with patch("app.load_sites", return_value=["https://a.com"]), patch(
        "app.check_site", return_value=("https://a.com", 200)
    ):
        resp = app.test_client().get("/api/status")
    assert resp.status_code == 200
    assert resp.get_json() == [{"url": "https://a.com", "status": 200, "ok": True}]


def test_index_page():
    with patch("app.load_sites", return_value=["https://a.com"]), patch(
        "app.check_site", return_value=("https://a.com", 200)
    ):
        resp = app.test_client().get("/")
    assert resp.status_code == 200
    assert "https://a.com" in resp.get_data(as_text=True)
