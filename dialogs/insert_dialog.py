from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton
from database import Database


class InsertDialog(QDialog):
    """
    A dialog box for adding new student records to a database. Contains input fields
    for the student's name and phone number and a dropdown list of courses from
    which to select.
    """
    def __init__(self):
        super().__init__()
        window_side_len = 300
        self.setWindowTitle("Add New Student")
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
        db = Database()
        name = self.student_name.text().title()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.phone_number.text()
        connection = db.connect()
        cursor = connection.cursor()

        cursor.execute(db.add_query, (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        self.close()
