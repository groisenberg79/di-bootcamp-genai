import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """Open a new DB connection. Caller must close it."""
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "postgres"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
    )

def run_select_one(sql: str, params=None):
    """
    Execute a query expected to return at most one row.
    Returns a tuple row, or None if no rows.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(sql, params)
        row = cur.fetchone()
        conn.commit()  # important for INSERT/UPDATE/DELETE ... RETURNING
        return row
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


def run_select_all(sql: str, params=None):
    """
    Execute a query that may return many rows.
    Returns a list of tuple rows (possibly empty).
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(sql, params)
        rows = cur.fetchall()
        conn.commit()
        return rows
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

def run_execute(sql: str, params=None) -> None:
    """
    Execute a statement that doesn't need returned rows (INSERT/UPDATE/DELETE without RETURNING).
    Commits on success, rolls back on error.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(sql, params)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()