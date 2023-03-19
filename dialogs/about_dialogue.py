from PyQt6.QtWidgets import QMessageBox


class AboutDialog(QMessageBox):
    """
    A message box containing information about the student management system
    including how it was created and how it may be used.
    """
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.setWindowTitle("About")
        content = "The student management system app was created during \"The Python Megacourse\". Feel free to modify and reuse it."
        self.setText(content)
