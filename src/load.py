from psycopg2.extras import execute_batch
from db import connect_db
from logger import log_progress


def load_data(df):
    log_progress("Load phase started")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM banks")

    query = """
        INSERT INTO banks (bank, country, market_cap_usd)
        VALUES (%s, %s, %s)
    """

    data = list(df.itertuples(index=False, name=None))

    execute_batch(cursor, query, data)

    conn.commit()
    cursor.close()
    conn.close()

    log_progress("Load phase completed")