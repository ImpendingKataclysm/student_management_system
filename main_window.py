from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QAction
from insert_dialog import InsertDialog
from db_queries import DB_FILE, display_query
import sqlite3


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
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Phone"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        """
        Reads student data from a database and displays it in the main window table
        """
        connection = sqlite3.connect(DB_FILE)
        result = connection.execute(display_query)
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        """
        Opens a dialog box to allow the user to register a new student
        """
        dialog = InsertDialog()
        dialog.exec()
        self.load_data()

