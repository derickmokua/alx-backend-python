#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

def stream_users_in_batches(batch_size):
    """
    Generator that yields user records in batches from the user_data table.
    Each batch is a list of dictionaries.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_mysql_password',  # Replace this
            database='ALX_prodev'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT COUNT(*) as total FROM user_data;")
            total_rows = cursor.fetchone()['total']

            for offset in range(0, total_rows, batch_size):
                cursor.execute(
                    "SELECT * FROM user_data LIMIT %s OFFSET %s;",
                    (batch_size, offset)
                )
                batch = cursor.fetchall()
                if not batch:
                    break
                yield batch

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Database error: {e}")
        return


def batch_processing(batch_size):
    """
    Process each batch and yield users with age > 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
