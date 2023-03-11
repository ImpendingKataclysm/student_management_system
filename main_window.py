from PyQt6.QtWidgets import QMainWindow, QTableWidget
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    """
    Displays the main window for the student management system. Shows a table
    that lists all registered students by id, name, course and phone number.
    Also includes a menu bar with options for:
    - Adding a new student
    - Finding information about the program itself
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Phone"))
        self.setCentralWidget(self.table)
