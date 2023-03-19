from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton, QMessageBox
from database import Database


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
        no.clicked.connect(self.abort_delete)

    def delete_student(self):
        """
        Delete selected student record from the database
        """
        db = Database()
        connection = db.connect()
        cursor = connection.cursor()
        cursor.execute(db.delete_query, (self.student_id, ))
        connection.commit()
        cursor.close()
        connection.close()
        self.close()

        # Success message
        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Success")
        confirmation_widget.setText(f"Deleted record for {self.student_name}")
        confirmation_widget.exec()

    def abort_delete(self):
        """
        Exits delete dialog without deleting selected record
        """
        exit_message = QMessageBox()
        exit_message.setWindowTitle("Exit")
        exit_message.setText(f"Record for {self.student_name} has not been deleted")
        exit_message.exec()
        self.close()
