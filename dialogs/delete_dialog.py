from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton
from db_queries import DB_FILE, delete_query
import sqlite3


class DeleteDialog(QDialog):
    """
    A dialog box for deleting students from the database
    """
    def __init__(self, student_id, name):
        super().__init__()
        self.setWindowTitle("Delete Student Record")

        layout = QGridLayout()

        self.student_id = student_id
        self.student_name = name
        confirmation = QLabel(f"Delete record for {self.student_name}?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

        yes.clicked.connect(self.delete_student)

    def delete_student(self):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(delete_query, (self.student_id, ))
        connection.commit()
        cursor.close()
        connection.close()
        self.close()
