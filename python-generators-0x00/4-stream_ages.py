#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error


def stream_user_ages():
    """
    Generator that yields one user age at a time from the user_data table.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_mysql_password',  # Replace with actual password
            database='ALX_prodev'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT age FROM user_data;")

            for row in cursor:
                yield row[0]  # age is the only column selected

            cursor.close()
            connection.close()

    except Error as e:
        print(f"Database error: {e}")


def average_user_age():
    """
    Calculates and prints the average age using the stream_user_ages generator.
    """
    total = 0
    count = 0

    for age in stream_user_ages():
        total += age
        count += 1

    average = total / count if count > 0 else 0
    print(f"Average age of users: {average:.2f}")
