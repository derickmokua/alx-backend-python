#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

def stream_users():
    """
    Generator that yields user records one by one from the user_data table.
    Each row is yielded as a dictionary.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_mysql_password',  # Replace with  real MYSQL password
            database='ALX_prodev'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM user_data;")

            for row in cursor:
                yield row

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Database error: {e}")
        return
