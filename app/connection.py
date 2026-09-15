
import os
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def connect_database():
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", 3306))
    )

    return db


def execute_query(sql):
    db = connect_database()

    try:
        cursor = db.cursor()
        cursor.execute(sql)

        response = cursor.fetchall()

        columns = [column[0] for column in cursor.description]

        print("COLONNES :", columns)

        return pd.DataFrame(response, columns=columns)

    finally:
        cursor.close()
        db.close()