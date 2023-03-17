import sqlite3

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton
from db_queries import DB_FILE, add_query


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        window_side_len = 300
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(window_side_len)
        self.setFixedHeight(window_side_len)
        
        layout = QVBoxLayout()

        # Add student name
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Select student course
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add phone number
        self.phone_number = QLineEdit()
        self.phone_number.setPlaceholderText("Phone Number")
        layout.addWidget(self.phone_number)

        # Submit button
        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        """
        Add new student information to the database
        """
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.phone_number.text()
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()

        cursor.execute(add_query, (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        self.close()
