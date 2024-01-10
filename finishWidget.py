from PySide6.QtWidgets import QDialog, QInputDialog

from ui_finishDialogue import Ui_FinishDialogue


class FinishDialogueWidget(QDialog, Ui_FinishDialogue):
    def __init__(self, parent):
        super(FinishDialogueWidget, self).__init__(parent)
        self.setupUi(self)
        self.showCorrelationsFinishButton.clicked.connect(
            self.parent().showCorrelations
        )
        self.showProbabilitiesFinishButton.clicked.connect(
            self.parent().showProbabilities
        )

    def accept(self):
        submissions, accepted = QInputDialog.getInt(
            self,
            "Choose Submissions",
            "How many submissions do you want",
            value=100,
            minValue=0,
            maxValue=1000,
        )
        if accepted:
            self.parent().parent().parent().createData(submissions)
            super().accept()

    def reject(self):
        super().reject()
