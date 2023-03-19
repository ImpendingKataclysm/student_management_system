from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QToolBar, \
     QStatusBar, QPushButton
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
from dialogs.insert_dialog import InsertDialog
from dialogs.search_dialog import SearchDialog
from dialogs.delete_dialog import DeleteDialog
from dialogs.edit_dialog import EditDialog
from dialogs.about_dialogue import AboutDialog
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

        # Menu Elements
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        add_student_action = QAction(QIcon("icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.about)
        help_menu_item.addAction(about_action)

        search_action = QAction(QIcon("icons/search.png"), "Search", self)
        search_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_action)

        # Display Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Phone"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # Toolbar Elements
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # Status Bar Elements
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Detect when cell is clicked
        self.table.cellClicked.connect(self.cell_clicked)

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

    def cell_clicked(self):
        """
        Adds buttons for editing and deleting student records to the status bar
        when a cell in the student table is clicked
        """
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        buttons = self.findChildren(QPushButton)
        if buttons:
            for button in buttons:
                self.status_bar.removeWidget(button)

        self.status_bar.addWidget(edit_button)
        self.status_bar.addWidget(delete_button)

    def edit(self):
        """
        Update the student record with new information entered by the user
        """
        index = self.table.currentRow()
        student_id = self.table.item(index, 0).text()
        student_name = self.table.item(index, 1).text()
        student_course = self.table.item(index, 2).text()
        student_phone = self.table.item(index, 3).text()
        dialog = EditDialog(student_id, student_name, student_course, student_phone)
        dialog.exec()
        self.load_data()

    def delete(self):
        """
        Delete the record selected by the user
        """
        index = self.table.currentRow()
        student_id = self.table.item(index, 0).text()
        student_name = self.table.item(index, 1).text()
        dialog = DeleteDialog(student_id, student_name)
        dialog.exec()
        self.load_data()

    def about(self):
        """
        Displays some information about the program
        """
        dialog = AboutDialog()
        dialog.exec()
