import sqlite3


class DatabaseTest2:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO test_num2 (user_id) VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM test_num2 WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def set_time_sub(self, user_id, time_sub):
        with self.connection:
            return self.cursor.execute("UPDATE test_num2 SET time_sub = ? WHERE user_id = ?", (time_sub, user_id,)) #  Основа

    def add_answ1(self, user_id, answ1):
        with self.connection:
            return self.cursor.execute("UPDATE test_num2 SET answ1 = ? WHERE user_id = ?", (answ1, user_id,))

    def add_answ2(self, user_id, answ2):
        with self.connection:
            return self.cursor.execute("UPDATE test_num2 SET answ2 = ? WHERE user_id = ?", (answ2, user_id,))

    def add_answ3(self, user_id, answ3):
        with self.connection:
            return self.cursor.execute("UPDATE test_num2 SET answ3 = ? WHERE user_id = ?", (answ3, user_id,))

    def add_answ4(self, user_id, answ4):
        with self.connection:
            return self.cursor.execute("UPDATE test_num2 SET answ4 = ? WHERE user_id = ?", (answ4, user_id,))
    def add_answ5(self, user_id, answ5):
        with self.connection:
            return self.cursor.execute("UPDATE test_num2 SET answ5 = ? WHERE user_id = ?", (answ5, user_id,))
    def add_answ6(self, user_id, answ6):
        with self.connection:
            return self.cursor.execute("UPDATE test_num2 SET answ6 = ? WHERE user_id = ?", (answ6, user_id,))
    def add_answ7(self, user_id, answ7):
        with self.connection:
            return self.cursor.execute("UPDATE test_num2 SET answ7 = ? WHERE user_id = ?", (answ7, user_id,))
    def add_answ8(self, user_id, answ8):
        with self.connection:
            return self.cursor.execute("UPDATE test_num2 SET answ8 = ? WHERE user_id = ?", (answ8, user_id,))
    def add_answ9(self, user_id, answ9):
        with self.connection:
            return self.cursor.execute("UPDATE test_num2 SET answ9 = ? WHERE user_id = ?", (answ9, user_id,))
    def add_answ10(self, user_id, answ10):
        with self.connection:
            return self.cursor.execute("UPDATE test_num2 SET answ10 = ? WHERE user_id = ?", (answ10, user_id,))


    def add_resalt(self, user_id):
        with self.connection:
            a = self.cursor.execute('SELECT*FROM test_num2  WHERE user_id = ?', (user_id,)).fetchall()
            return self.cursor.execute(f"UPDATE test_num2 SET test_result = {sum(a[0][3:-2])}  WHERE user_id = ?", (user_id,))

    def get_resalt(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT test_result FROM test_num2 WHERE user_id = ?", (user_id,)).fetchall()