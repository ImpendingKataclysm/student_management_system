import sqlite3


class Database:
    def __init__(self):
        super(Database, self).__init__()
        self.db_file = "database.db"
        self.name = "students"
        self.display_query = f"SELECT * FROM {self.name}"
        self.add_query = f"INSERT INTO {self.name} (name, course, mobile) VALUES (?,?,?)"
        self.search_query = f"SELECT * FROM {self.name} WHERE name = ?"
        self.update_query = f"UPDATE {self.name} SET name = ?, course = ?, mobile = ? WHERE id = ?"
        self.delete_query = f"DELETE FROM {self.name} WHERE id = ?"

    def connect(self):
        return sqlite3.connect(self.db_file)
