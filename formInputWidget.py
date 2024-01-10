import time
from time import gmtime, strftime

from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot
from PySide6.QtWidgets import QMessageBox, QWidget

from ui_dataProgress import Ui_FormDataWidget


class FormInputWidget(QWidget, Ui_FormDataWidget):
    def __init__(self, parent):
        super(FormInputWidget, self).__init__(parent)
        self.setupUi(self)
        self.users = []
        self.startFormButton.clicked.connect(self.inputForms)
        self.threadpool = QThreadPool()

    def setUsers(self, users):
        self.users = users

    def inputForms(self):
        self.startFormButton.setEnabled(False)
        self.startTime = time.time()
        formWorker = FormWorker(self.formLoop)
        formWorker.signals.progress.connect(self.formProgressBar.setValue)
        formWorker.signals.timeRemaining.connect(self.estimatedTimeLabel.setText)
        formWorker.signals.finished.connect(self.formFinished)
        self.threadpool.start(formWorker)

    def formLoop(self, progressSignal, timeSignal, finishedSignal):
        driver = self.parent().parent().driver
        for index, user in enumerate(self.users):
            self.currentTime = time.time()
            self.parent().parent().loadPage()
            questions, submitButton, title = self.parent().parent().page
            for question in user:
                driver.execute_script(
                    "arguments[0].click();", questions[question[0]].answers[question[1]]
                )
            driver.execute_script("arguments[0].click();", submitButton)
            progressSignal.emit((index) / (len(self.users)) * 100)
            timeRemaining = f"User {index+1}/{len(self.users)} - {self.formatTime(index, self.currentTime-self.startTime)} remaining"
            timeSignal.emit(timeRemaining)
        finishedSignal.emit()

    def formatTime(self, index, timeDifference):
        if index == 0:
            return ""
        timePerUser = timeDifference / (index + 1)
        timeRemaining = (len(self.users) - index) * timePerUser
        return strftime("%M Minutes %S Seconds", gmtime(timeRemaining))

    def formFinished(self):
        okPressed = QMessageBox.information(
            self,
            "Good job",
            f"{len(self.users)} Submissions Successfully Added",
            QMessageBox.Ok,
        )
        if okPressed:
            self.parent().parent().driver.quit()
            self.parent().parent().close()


class FormWorker(QRunnable):
    def __init__(self, LoopFn):
        super(FormWorker, self).__init__()
        self.LoopFn = LoopFn
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        self.LoopFn(
            self.signals.progress, self.signals.timeRemaining, self.signals.finished
        )


class WorkerSignals(QObject):
    progress = Signal(float)
    timeRemaining = Signal(str)
    finished = Signal()
