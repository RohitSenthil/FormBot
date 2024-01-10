from PySide6.QtWidgets import QMessageBox, QWidget

from finishWidget import FinishDialogueWidget
from ui_questions import Ui_CorrelationWidget


class CorrelationWidget(QWidget, Ui_CorrelationWidget):
    def __init__(self, parent):
        super(CorrelationWidget, self).__init__(parent)
        self.setupUi(self)
        self.page = []
        self.correlationQuestion1.itemClicked.connect(
            lambda newItem: self.questionChanged(newItem, 0)
        )
        self.correlationQuestion2.itemClicked.connect(
            lambda newItem: self.questionChanged(newItem, 1)
        )
        self.probabilityQuestion1.itemClicked.connect(
            lambda newItem: self.questionChanged(newItem, 2)
        )
        self.correlationAnswer1.itemClicked.connect(
            lambda newItem: self.questionChanged(newItem, 3)
        )
        self.correlationAnswer2.itemClicked.connect(
            lambda newItem: self.questionChanged(newItem, 4)
        )
        self.probabilityAnswer1.itemClicked.connect(
            lambda newItem: self.questionChanged(newItem, 5)
        )
        self.correlationQ1 = -1
        self.correlationA1 = []
        self.correlationQ2 = -1
        self.correlationA2 = []
        self.probabilityQ1 = -1
        self.probabilityA1 = []
        self.correlationType = True
        self.probabilityType = True
        self.positiveCorrelationButton.toggled.connect(self.correlationTypeChanged)
        self.positiveProbabilityButton.toggled.connect(self.probabilityTypeChanged)
        self.correlationSubmitButton.clicked.connect(self.addCorrelation)
        self.probabilitySubmitButton.clicked.connect(self.addProbability)
        self.showCorrelationsButton.clicked.connect(self.showCorrelations)
        self.showProbabilitiesButton.clicked.connect(self.showProbabilities)
        self.finishButton.clicked.connect(self.finished)

    def loadQuestions(self):
        self.page = self.parent().parent().page
        questions = [question.questionText for question in self.page[0]]
        self.correlationQuestion1.addItems(questions)
        self.correlationQuestion2.addItems(questions)
        self.probabilityQuestion1.addItems(questions)
        self.formTitleLabel.setText(self.page[2])

    def addCorrelation(self):
        if (
            self.correlationQ1 < 0
            or self.correlationQ2 < 0
            or self.correlationA1 == []
            or self.correlationA2 == []
        ):
            QMessageBox.critical(
                self,
                "You are dumb",
                "You have not selected all the answer choices needed to make a correlation. Try again",
                QMessageBox.Ok,
            )
            return
        elif self.correlationQ1 == self.correlationQ2:
            QMessageBox.critical(
                self,
                "You are slow",
                "How are two answer choices from the same quesiton going to be correlated? Try again",
                QMessageBox.Ok,
            )
            return
        for answerChoice1 in self.correlationA1:
            for answerChoice2 in self.correlationA2:
                correlationList = (
                    [
                        self.correlationQ1,
                        answerChoice1,
                        self.correlationQ2,
                        answerChoice2,
                        self.correlationType,
                    ]
                    if self.correlationQ1 < self.correlationQ2
                    else [
                        self.correlationQ2,
                        answerChoice2,
                        self.correlationQ1,
                        answerChoice1,
                        self.correlationType,
                    ]
                )
                self.parent().parent().addCorrelation(correlationList)
        self.correlationQuestion1.clearSelection()
        self.correlationQuestion2.clearSelection()
        self.correlationAnswer1.clear()
        self.correlationAnswer2.clear()
        self.correlationQ1 = -1
        self.correlationA1 = []
        self.correlationQ2 = -1
        self.correlationA2 = []
        QMessageBox.information(
            self,
            "Good job",
            f"You have succesfully added the correlation",
            QMessageBox.Ok,
        )

    def addProbability(self):
        if self.probabilityQ1 < 0 or self.probabilityA1 == []:
            QMessageBox.critical(
                self,
                "Get some brain cells",
                "You have not selected all the answer choices needed to add a probability. Try again",
                QMessageBox.Ok,
            )
            return
        for answerChoice in self.probabilityA1:
            self.parent().parent().probabilities.append(
                [self.probabilityQ1, answerChoice, self.probabilityType]
            )
        self.probabilityQuestion1.clearSelection()
        self.probabilityAnswer1.clear()
        QMessageBox.information(
            self,
            "Good job",
            f"You have succesfully modified the probability",
            QMessageBox.Ok,
        )
        self.probabilityQ1 = -1
        self.probabilityA1 = []

    def questionChanged(self, newItem, listIndex):
        if listIndex == 0:
            answers = self.page[0][self.correlationQuestion1.row(newItem)].answersText
            self.correlationAnswer1.clear()
            self.correlationAnswer1.addItems(answers)
            self.correlationQ1 = self.correlationQuestion1.row(newItem)
            self.correlationA1 = []
        elif listIndex == 1:
            answers = self.page[0][self.correlationQuestion2.row(newItem)].answersText
            self.correlationAnswer2.clear()
            self.correlationAnswer2.addItems(answers)
            self.correlationQ2 = self.correlationQuestion2.row(newItem)
            self.correlationA2 = []
        elif listIndex == 2:
            answers = self.page[0][self.probabilityQuestion1.row(newItem)].answersText
            self.probabilityAnswer1.clear()
            self.probabilityAnswer1.addItems(answers)
            self.probabilityQ1 = self.probabilityQuestion1.row(newItem)
            self.probabilityA1 = []
        elif listIndex == 3:
            selectedAnswers = []
            for item in self.correlationAnswer1.selectedItems():
                selectedAnswers.append(self.correlationAnswer1.row(item))
            self.correlationA1 = selectedAnswers
        elif listIndex == 4:
            selectedAnswers = []
            for item in self.correlationAnswer2.selectedItems():
                selectedAnswers.append(self.correlationAnswer2.row(item))
            self.correlationA2 = selectedAnswers
        elif listIndex == 5:
            selectedAnswers = []
            for item in self.probabilityAnswer1.selectedItems():
                selectedAnswers.append(self.probabilityAnswer1.row(item))
            self.probabilityA1 = selectedAnswers

    def finished(self):
        self.dialogue = FinishDialogueWidget(self)
        self.dialogue.open()

    def showCorrelations(self):
        correlationText = ""
        questions = self.page[0]
        for firstCorrelation in self.parent().parent().correlations.keys():
            correlationText += f"{questions[firstCorrelation[0]].questionText}-{questions[firstCorrelation[0]].answersText[firstCorrelation[1]]} is\n"
            for secondCorrelation in (
                self.parent().parent().correlations[firstCorrelation]
            ):
                correlationText += f'\t{"positively" if secondCorrelation[2] else "negatively"} correlated with {questions[secondCorrelation[0]].questionText}-{questions[secondCorrelation[0]].answersText[secondCorrelation[1]]}\n'
        QMessageBox.information(
            self,
            "Good job",
            "There are no correlations"
            if correlationText == ""
            else f"The current correlations are\n{correlationText}",
            QMessageBox.Ok,
        )

    def showProbabilities(self):
        probabilitiesText = ""
        questions = self.page[0]
        for probabilityModification in self.parent().parent().probabilities:
            probabilitiesText += f'The probability of {questions[probabilityModification[0]].questionText}-{questions[probabilityModification[0]].answersText[probabilityModification[1]]} will be {"increased" if probabilityModification[2] else "decreased"}\n'
        QMessageBox.information(
            self,
            "Good job",
            "There are no probability modifications"
            if probabilitiesText == ""
            else f"The current probabilites are\n{probabilitiesText}",
            QMessageBox.Ok,
        )

    def correlationTypeChanged(self, checked):
        self.correlationType = checked

    def probabilityTypeChanged(self, checked):
        self.probabilityType = checked
