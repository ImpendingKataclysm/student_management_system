from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QToolBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
from insert_dialog import InsertDialog
from search_dialog import SearchDialog
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
        self.setMinimumSize(800, 600)

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        add_student_action = QAction(QIcon("icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        search_action = QAction(QIcon("icons/search.png"), "Search", self)
        search_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Phone"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

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
        Opens a dialog box to register a new student
        """
        dialog = InsertDialog()
        dialog.exec()
        self.load_data()

    def search(self):
        """
        Opens a dialog box to search for a student
        """
        dialog = SearchDialog()
        dialog.exec()
        name = dialog.search()
        items = self.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            self.table.item(item.row(), 1).setSelected(True)
