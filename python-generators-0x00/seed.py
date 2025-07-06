#!/usr/bin/env python3

import mysql.connector
import csv
import uuid
from mysql.connector import Error


def connect_db():
    """Connect to MySQL server (not the specific database yet)."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_mysql_password'  # replace this!
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_database(connection):
    """Create the ALX_prodev database if it doesn't exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        connection.commit()
        print("Database ALX_prodev created or already exists.")
    except Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_mysql_password',  # replace this!
            database='ALX_prodev'
        )
        return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None


def create_table(connection):
    """Create user_data table if it doesn't exist."""
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX(user_id)
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, filename):
    """Insert data into user_data table from CSV."""
    try:
        cursor = connection.cursor()

        # Read CSV data
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']

                # Avoid duplicate emails
                cursor.execute("SELECT email FROM user_data WHERE email = %s", (email,))
                if cursor.fetchone():
                    continue  # Skip inserting duplicate

                insert_query = """
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s);
                """
                cursor.execute(insert_query, (user_id, name, email, age))

        connection.commit()
        print("Data inserted successfully.")
    except Error as e:
        print(f"Error inserting data: {e}")
