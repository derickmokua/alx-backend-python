import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=None, db_name="my_database.db"):
        self.query = query
        self.params = params if params is not None else []
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    params = [25]
    with ExecuteQuery(query, params) as results:
        for row in results:
            print(row)
