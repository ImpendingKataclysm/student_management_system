from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        window_side_len = 300
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(window_side_len)
        self.setFixedHeight(window_side_len)
        
        layout = QVBoxLayout()

        # Add student name
        student_name = QLineEdit()
        student_name.setPlaceholderText("Name")
        layout.addWidget(student_name)

        # Select student course
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.setLayout(layout)
