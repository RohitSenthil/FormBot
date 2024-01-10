from subprocess import CREATE_NO_WINDOW

import numpy as np
from PySide6.QtWidgets import QMainWindow, QStackedWidget
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from correlationWidget import CorrelationWidget
from formInputWidget import FormInputWidget
from formWidget import FormWidget
from question import Question


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumWidth(250)
        self.stackedWidget = QStackedWidget()
        self.formWidget = FormWidget(self)
        self.correlationWidget = CorrelationWidget(self)
        self.formInputWidget = FormInputWidget(self)
        self.stackedWidget.addWidget(self.formWidget)
        self.stackedWidget.addWidget(self.correlationWidget)
        self.stackedWidget.addWidget(self.formInputWidget)
        self.setCentralWidget(self.stackedWidget)
        self.setWindowTitle("FormBot v2.0")
        self.page = []
        chromeService = ChromeService(ChromeDriverManager().install())
        chromeService.creation_flags = CREATE_NO_WINDOW
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-startup-window")
        self.driver = webdriver.Chrome(service=chromeService, options=options)
        self.correlations = {}
        self.probabilities = []
        self.formLink = ""
        self.users = []

    def loadPage(self, formLink=None, first=False):
        formLink = formLink if formLink else self.formLink
        self.driver.get(formLink)
        self.driver.implicitly_wait(3)
        questions = []
        questionElements = self.driver.find_elements(By.CLASS_NAME, "geS5n")
        for questionElement in questionElements:
            question = questionElement.find_element(By.XPATH, ".//*[@class='M7eMe']")
            answers = questionElement.find_elements(
                By.XPATH, ".//*[@class='Od2TWd hYsg7c']"
            )
            if not answers:
                answers = questionElement.find_elements(
                    By.XPATH, ".//*[@class='uVccjd aiSeRd FXLARc wGQFbe BJHAP oLlshd']"
                )
            questions.append(Question(question, answers))
        submitButton = self.driver.find_element(
            By.XPATH, ".//*[@class='uArJ5e UQuaGc Y5sE8d VkkpIf QvWxOd']"
        )
        title = self.driver.find_element(
            By.XPATH, ".//*[@class='F9yp7e ikZYwf LgNcQe']"
        ).text
        self.page = [questions, submitButton, title]
        if first:
            self.stackedWidget.setCurrentIndex(1)
            self.resize(658, 700)
            self.correlationWidget.loadQuestions()
            self.formLink = formLink

    def addCorrelation(self, correlationList):
        if (*correlationList[0:2],) in self.correlations:
            self.correlations[(*correlationList[0:2],)].append(correlationList[2:])
        else:
            self.correlations[(*correlationList[0:2],)] = [correlationList[2:]]

    def createData(self, submissions):
        for i in range(0, submissions):
            self.users.append(self.createUser())
        self.formInputWidget.setUsers(self.users)
        self.stackedWidget.setCurrentIndex(2)
        self.resize(291, 197)

    def createUser(self):
        user = []
        matchingCorrelations = []
        matchingCorrelations += self.probabilities
        questions = self.page[0]
        for currentQuestion in range(0, len(questions)):
            answerLen = len(questions[currentQuestion].answers)
            defaultWeight = 1 / answerLen
            weights = [defaultWeight] * answerLen
            questionWeights = [
                correlation
                for correlation in matchingCorrelations
                if correlation[0] == currentQuestion
            ]
            for questionWeight in questionWeights:
                mainAnswerWeight = defaultWeight * 0.9
                alternateAnswerWeights = (
                    np.random.default_rng().dirichlet(np.ones(answerLen - 1))
                    * mainAnswerWeight
                ).tolist()
                for index in range(0, answerLen):
                    if index == questionWeight[1]:
                        changedWeight = weights[index] + (
                            mainAnswerWeight
                            if questionWeight[2]
                            else -1 * mainAnswerWeight
                        )
                        if changedWeight > 1:
                            correction = (changedWeight - 1) / (answerLen - 1)
                            weights = [
                                (
                                    weight + correction
                                    if weightIndex != index
                                    else weight
                                )
                                for weightIndex, weight in enumerate(weights)
                            ]
                            changedWeight = 1
                        elif changedWeight < 0:
                            correction = (changedWeight) / (answerLen - 1)
                            weights = [
                                (
                                    weight + correction
                                    if weightIndex != index
                                    else weight
                                )
                                for weightIndex, weight in enumerate(weights)
                            ]
                            changedWeight = 0
                        weights[index] = changedWeight
                    else:
                        weights[index] += (
                            (-1 * alternateAnswerWeights[0])
                            if questionWeight[2]
                            else (alternateAnswerWeights[0])
                        )
                        del alternateAnswerWeights[0]
            weights = [
                (0 if np.isclose(weight, 0, atol=1e-13) or weight < 0 else weight)
                for weight in weights
            ]
            if sum(weights) != 1:
                weights = weights / np.linalg.norm(weights, ord=1)
            answerChoice = np.random.choice(range(0, answerLen), 1, p=weights)[0]
            questionChoice = (currentQuestion, answerChoice)
            user.append(questionChoice)
            if questionChoice in self.correlations:
                for correlation in self.correlations[questionChoice]:
                    matchingCorrelations.append(correlation)
        return user
