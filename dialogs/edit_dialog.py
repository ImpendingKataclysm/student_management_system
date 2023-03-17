from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton
from db_queries import DB_FILE, update_query
import sqlite3


class EditDialog(QDialog):
    """
    A dialog box for editing the records of students registered in the
    database.
    """
    def __init__(self, student_id, name, course, phone):
        super().__init__()
        window_side_len = 300
        self.setWindowTitle("Update Student Record")
        self.setFixedWidth(window_side_len)
        self.setFixedHeight(window_side_len)

        layout = QVBoxLayout()

        # Get Student ID
        self.student_id = student_id

        # Edit student name
        self.student_name = QLineEdit(name)
        layout.addWidget(self.student_name)

        # Update student course
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course)
        layout.addWidget(self.course_name)

        # Edit phone number
        self.phone_number = QLineEdit(phone)
        self.phone_number.setPlaceholderText("Phone Number")
        layout.addWidget(self.phone_number)

        # Submit button
        button = QPushButton("Update")
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        """
        Update an existing student record
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(update_query,
                       (self.student_name.text(),
                        self.course_name.currentText(),
                        self.phone_number.text(),
                        self.student_id))

        connection.commit()
        cursor.close()
        connection.close()
        self.close()
