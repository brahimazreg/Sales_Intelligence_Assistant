import os
import mysql.connector
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

        return response

    finally:
        cursor.close()
        db.close()
