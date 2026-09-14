import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from urllib.parse import quote_plus

load_dotenv()


def extract_schema():

    host = os.getenv("DB_HOST", "localhost")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")
    port = int(os.getenv("DB_PORT", 3306))

    encoded_password = quote_plus(password)

    connection_string = (
        f"mysql+mysqlconnector://{user}:{encoded_password}"
        f"@{host}:{port}/{database}"
    )

    engine = create_engine(connection_string)
    inspector = inspect(engine)

    schema = {}

    for table in inspector.get_table_names():

        columns = inspector.get_columns(table)

        primary_key = inspector.get_pk_constraint(table)

        foreign_keys = inspector.get_foreign_keys(table)

        schema[table] = {
            "columns": [
                {
                    "name": column["name"],
                    "type": str(column["type"]),
                    "nullable": column["nullable"],
                }
                for column in columns
            ],

            "primary_key": primary_key.get("constrained_columns", []),

            "foreign_keys": [
                {
                    "column": fk["constrained_columns"][0],
                    "references_table": fk["referred_table"],
                    "references_column": fk["referred_columns"][0],
                }
                for fk in foreign_keys
            ],
        }

    return schema