import psycopg2


def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="etl_project",
        user="postgres",
        password="YOUR_PASSWORD",
        port="5432"
    )