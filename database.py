import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO anketa (user_id) VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM anketa WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def get_user(self):
        with self.connection:
            return self.cursor.execute("SELECT*FROM anketa")

    def get_user_one(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT * FROM anketa WHERE user_id = ?", (user_id,)).fetchall()

    def set_time_sub(self, user_id, time_sub):
        with self.connection:
            return self.cursor.execute("UPDATE anketa SET time_sub = ? WHERE user_id = ?", (time_sub, user_id,))

    def add_name(self, user_id, name):
        with self.connection:
            return self.cursor.execute("UPDATE anketa SET name = ? WHERE user_id = ?", (name, user_id,))

    def set_lust_name(self, user_id, lust_name):
        with self.connection:
            return self.cursor.execute("UPDATE anketa SET lust_name = ? WHERE user_id = ?", (lust_name, user_id,))

    def set_age(self, user_id, age):
        with self.connection:
            return self.cursor.execute("UPDATE anketa SET age = ? WHERE user_id = ?", (age, user_id,))

    def set_weight(self, user_id, weight):
        with self.connection:
            return self.cursor.execute("UPDATE anketa SET weight = ? WHERE user_id = ?", (weight, user_id,))

    def set_height(self, user_id, height):
        with self.connection:
            return self.cursor.execute("UPDATE anketa SET height = ? WHERE user_id = ?", (height, user_id,))
    def add_state(self, user_id, state):
        with self.connection:
            return self.cursor.execute("UPDATE anketa SET state = ? WHERE user_id = ?", (state, user_id,))


