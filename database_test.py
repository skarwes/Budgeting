from Database.db import initialize_database, get_connection

# 1. Initialize the database using schema.sql
initialize_database()
print("1. Schema executed successfully!")

# 2. Check which tables exist
with get_connection() as connection:
    tables = connection.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
    """).fetchall()

print("2. Tables found:", tables)

# 3. Test inserting and retrieving a transaction
with get_connection() as connection:
    connection.execute("""
        INSERT INTO transactions
            (date, description, category, amount)
        VALUES (?, ?, ?, ?)
    """, ("2026-10-10", "Test purchase", "Food", -10.50))

    transaction = connection.execute("""
        SELECT date, description, category, amount
        FROM transactions
        WHERE description = ?
    """, ("Test purchase",)).fetchone()

print("3. Retrieved transaction:", transaction)
print("Database test completed!")
