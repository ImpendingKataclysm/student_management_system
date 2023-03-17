from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton


class SearchDialog(QDialog):
    """
    A dialog box for searching for students registered in the database by name
    """
    def __init__(self):
        super().__init__()
        window_side_len = 300
        self.setWindowTitle("Search Students")
        self.setFixedHeight(window_side_len)
        self.setFixedWidth(window_side_len)

        layout = QVBoxLayout()

        # Search student name
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Search button
        button = QPushButton("Search")
        button.clicked.connect(self.search)
        layout.addWidget(button)

        self.setLayout(layout)

    def search(self):
        print(self.student_name.text())
