import sqlite3


class DatabaseTest3:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO test_num3 (user_id) VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM test_num3 WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def set_time_sub(self, user_id, time_sub):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET time_sub = ? WHERE user_id = ?", (time_sub, user_id,)) #  Основа

    def add_answ1(self, user_id, answ1):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ1 = ? WHERE user_id = ?", (answ1, user_id,))

    def add_answ2(self, user_id, answ2):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ2 = ? WHERE user_id = ?", (answ2, user_id,))

    def add_answ3(self, user_id, answ3):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ3 = ? WHERE user_id = ?", (answ3, user_id,))

    def add_answ4(self, user_id, answ4):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ4 = ? WHERE user_id = ?", (answ4, user_id,))

    def add_answ5(self, user_id, answ5):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ5 = ? WHERE user_id = ?", (answ5, user_id,))

    def add_answ6(self, user_id, answ6):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ6 = ? WHERE user_id = ?", (answ6, user_id,))

    def add_answ7(self, user_id, answ7):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ7 = ? WHERE user_id = ?", (answ7, user_id,))

    def add_answ8(self, user_id, answ8):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ8 = ? WHERE user_id = ?", (answ8, user_id,))

    def add_answ9(self, user_id, answ9):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ9 = ? WHERE user_id = ?", (answ9, user_id,))
    def add_answ10(self, user_id, answ10):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ10 = ? WHERE user_id = ?", (answ10, user_id,))

    def add_answ11(self, user_id, answ11):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ11 = ? WHERE user_id = ?", (answ11, user_id,))

    def add_answ12(self, user_id, answ12):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ12 = ? WHERE user_id = ?", (answ12, user_id,))

    def add_answ13(self, user_id, answ13):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ13 = ? WHERE user_id = ?", (answ13, user_id,))

    def add_answ14(self, user_id, answ14):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ14 = ? WHERE user_id = ?", (answ14, user_id,))

    def add_answ15(self, user_id, answ15):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ15 = ? WHERE user_id = ?", (answ15, user_id,))

    def add_answ16(self, user_id, answ16):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ16 = ? WHERE user_id = ?", (answ16, user_id,))

    def add_answ17(self, user_id, answ17):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ17 = ? WHERE user_id = ?", (answ17, user_id,))

    def add_answ18(self, user_id, answ18):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ18 = ? WHERE user_id = ?", (answ18, user_id,))

    def add_answ19(self, user_id, answ19):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ19 = ? WHERE user_id = ?", (answ19, user_id,))

    def add_answ20(self, user_id, answ20):
        with self.connection:
            return self.cursor.execute("UPDATE test_num3 SET answ20 = ? WHERE user_id = ?", (answ20, user_id,))


    def add_resalt(self, user_id):
        with self.connection:
            a = self.cursor.execute('SELECT*FROM test_num3  WHERE user_id = ?', (user_id,)).fetchall()
            return self.cursor.execute(f"UPDATE test_num3 SET test_result = {sum(a[0][3:-2])}  WHERE user_id = ?", (user_id,))

    def get_resalt(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT test_result FROM test_num3 WHERE user_id = ?", (user_id,)).fetchall()