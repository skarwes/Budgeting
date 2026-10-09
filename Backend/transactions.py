from Database.db import get_connection


def insert_trans(date, description, category, ammount):
    with get_connection() as connection:
        tables = connection.execute("""
        INSERT INTO transactions
            (date, description, category, amount)
        VALUES (?, ?, ?, ?)
        """, (date, description, category, ammount))


def get_trans(category):
    
    with get_connection() as connection:
        transactions = connection.execute("""
        SELECT date, description, category, amount
        FROM transactions
        WHERE description = ?
    """, (category,)).fetchall()
    return transactions
    
