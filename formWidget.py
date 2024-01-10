import re

from PySide6.QtWidgets import QMessageBox, QWidget

from ui_enterForm import Ui_FormWidget


class FormWidget(QWidget, Ui_FormWidget):
    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.setupUi(self)
        self.formLineEdit.setPlaceholderText("Type Form Link Here")
        self.submitButton.clicked.connect(self.submitForm)
        self.formLineEdit.returnPressed.connect(self.submitForm)
        self.formRegex = re.compile(
            "(?:(?:https?|ftp):\/\/|\b(?:[a-z\d]+\.))(?:(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))?\))+(?:\((?:[^\s()<>]+|(?:\(?:[^\s()<>]+\)))?\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))?"
        )

    def submitForm(self):
        if not self.formRegex.match(self.formLineEdit.text()):
            QMessageBox.critical(
                self,
                "You are not intelligent",
                "You have not entered a valid link. Try again",
                QMessageBox.Ok,
            )
            return
        self.parent().parent().loadPage(self.formLineEdit.text(), True)
