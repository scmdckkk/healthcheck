import os
from contextlib import closing


def get_conn():
    import psycopg2

    return psycopg2.connect(os.environ["DATABASE_URL"])


def init_db():
    with closing(get_conn()) as conn, conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS checks (
                    id SERIAL PRIMARY KEY,
                    url TEXT NOT NULL,
                    status TEXT NOT NULL,
                    ok BOOLEAN NOT NULL,
                    checked_at TIMESTAMPTZ NOT NULL DEFAULT now()
                )
                """
            )


def save_check(url, status, ok):
    with closing(get_conn()) as conn, conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO checks (url, status, ok) VALUES (%s, %s, %s)",
                (url, str(status), ok),
            )


def latest_checks():
    """Последний результат по каждому сайту."""
    init_db()
    with closing(get_conn()) as conn, conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT DISTINCT ON (url) url, status, ok, checked_at
                FROM checks
                ORDER BY url, checked_at DESC
                """
            )
            return [
                {"url": u, "status": s, "ok": ok, "checked_at": str(t)}
                for u, s, ok, t in cur.fetchall()
            ]


def last_ok(url):
    """Результат прошлой проверки сайта: True, False или None, если проверок не было."""
    with closing(get_conn()) as conn, conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT ok FROM checks WHERE url = %s ORDER BY checked_at DESC LIMIT 1",
                (url,),
            )
            row = cur.fetchone()
            return row[0] if row else None
