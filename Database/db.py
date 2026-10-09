import sqlite3
from pathlib import Path

DATABASE_DIR = Path(__file__).resolve().parent
SCHEMA_PATH = DATABASE_DIR / "schema.sql"
DATABASE_PATH = DATABASE_DIR / "budget.db"


def initialize_database():
    with sqlite3.connect(DATABASE_PATH) as connection:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
            schema = file.read()

        connection.executescript(schema)


def get_connection():
    return sqlite3.connect(DATABASE_PATH)