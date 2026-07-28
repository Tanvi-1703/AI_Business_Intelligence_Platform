import sqlite3
import pandas as pd


DATABASE = "database/business.db"


def create_connection():
    conn = sqlite3.connect(DATABASE)
    return conn


def save_to_database(df):
    conn = create_connection()

    df.to_sql(
        "sales_data",
        conn,
        if_exists="replace",
        index=False
    )

    conn.commit()
    conn.close()

    print("✅ Data Stored Successfully in SQLite")


def read_database():
    conn = create_connection()

    df = pd.read_sql(
        "SELECT * FROM sales_data",
        conn
    )

    conn.close()

    return df