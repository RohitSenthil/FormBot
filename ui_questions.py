# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'questions.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QButtonGroup,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_CorrelationWidget(object):
    def setupUi(self, CorrelationWidget):
        if not CorrelationWidget.objectName():
            CorrelationWidget.setObjectName("CorrelationWidget")
        CorrelationWidget.resize(658, 700)
        self.layoutWidget = QWidget(CorrelationWidget)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 641, 681))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formTitleLabel = QLabel(self.layoutWidget)
        self.formTitleLabel.setObjectName("formTitleLabel")

        self.verticalLayout.addWidget(self.formTitleLabel, 0, Qt.AlignHCenter)

        self.correlationTab = QTabWidget(self.layoutWidget)
        self.correlationTab.setObjectName("correlationTab")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget1 = QWidget(self.tab_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(360, 10, 241, 471))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.correlationQuestionLabel2 = QLabel(self.layoutWidget1)
        self.correlationQuestionLabel2.setObjectName("correlationQuestionLabel2")

        self.verticalLayout_3.addWidget(
            self.correlationQuestionLabel2, 0, Qt.AlignHCenter
        )

        self.correlationQuestion2 = QListWidget(self.layoutWidget1)
        self.correlationQuestion2.setObjectName("correlationQuestion2")
        self.correlationQuestion2.setAlternatingRowColors(True)
        self.correlationQuestion2.setProperty("isWrapping", False)
        self.correlationQuestion2.setSpacing(0)
        self.correlationQuestion2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.correlationQuestion2)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.correlationAnswerLabel2 = QLabel(self.layoutWidget1)
        self.correlationAnswerLabel2.setObjectName("correlationAnswerLabel2")

        self.verticalLayout_8.addWidget(
            self.correlationAnswerLabel2, 0, Qt.AlignHCenter
        )

        self.correlationAnswer2 = QListWidget(self.layoutWidget1)
        self.correlationAnswer2.setObjectName("correlationAnswer2")
        self.correlationAnswer2.setAlternatingRowColors(True)
        self.correlationAnswer2.setSelectionMode(QAbstractItemView.MultiSelection)
        self.correlationAnswer2.setProperty("isWrapping", False)
        self.correlationAnswer2.setSpacing(0)
        self.correlationAnswer2.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.correlationAnswer2)

        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.layoutWidget2 = QWidget(self.tab_2)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 10, 241, 471))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.correlationQuestionLabel1 = QLabel(self.layoutWidget2)
        self.correlationQuestionLabel1.setObjectName("correlationQuestionLabel1")

        self.verticalLayout_2.addWidget(
            self.correlationQuestionLabel1, 0, Qt.AlignHCenter
        )

        self.correlationQuestion1 = QListWidget(self.layoutWidget2)
        self.correlationQuestion1.setObjectName("correlationQuestion1")
        self.correlationQuestion1.setAlternatingRowColors(True)
        self.correlationQuestion1.setProperty("isWrapping", False)
        self.correlationQuestion1.setSpacing(0)
        self.correlationQuestion1.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.correlationQuestion1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.correlationAnswerLabel1 = QLabel(self.layoutWidget2)
        self.correlationAnswerLabel1.setObjectName("correlationAnswerLabel1")

        self.verticalLayout_6.addWidget(
            self.correlationAnswerLabel1, 0, Qt.AlignHCenter
        )

        self.correlationAnswer1 = QListWidget(self.layoutWidget2)
        self.correlationAnswer1.setObjectName("correlationAnswer1")
        self.correlationAnswer1.setAlternatingRowColors(True)
        self.correlationAnswer1.setSelectionMode(QAbstractItemView.MultiSelection)
        self.correlationAnswer1.setProperty("isWrapping", False)
        self.correlationAnswer1.setSpacing(0)
        self.correlationAnswer1.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.correlationAnswer1)

        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.layoutWidget3 = QWidget(self.tab_2)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(120, 500, 381, 84))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.correlationTypeBox = QGroupBox(self.layoutWidget3)
        self.correlationTypeBox.setObjectName("correlationTypeBox")
        self.correlationTypeBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.correlationTypeBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.positiveCorrelationButton = QRadioButton(self.correlationTypeBox)
        self.correlationTypeGroup = QButtonGroup(CorrelationWidget)
        self.correlationTypeGroup.setObjectName("correlationTypeGroup")
        self.correlationTypeGroup.addButton(self.positiveCorrelationButton)
        self.positiveCorrelationButton.setObjectName("positiveCorrelationButton")
        self.positiveCorrelationButton.setChecked(True)

        self.verticalLayout_4.addWidget(self.positiveCorrelationButton)

        self.negativeCorrelationButton = QRadioButton(self.correlationTypeBox)
        self.correlationTypeGroup.addButton(self.negativeCorrelationButton)
        self.negativeCorrelationButton.setObjectName("negativeCorrelationButton")

        self.verticalLayout_4.addWidget(self.negativeCorrelationButton)

        self.horizontalLayout_3.addWidget(self.correlationTypeBox)

        self.correlationSubmitButton = QPushButton(self.layoutWidget3)
        self.correlationSubmitButton.setObjectName("correlationSubmitButton")

        self.horizontalLayout_3.addWidget(self.correlationSubmitButton)

        self.showCorrelationsButton = QPushButton(self.layoutWidget3)
        self.showCorrelationsButton.setObjectName("showCorrelationsButton")

        self.horizontalLayout_3.addWidget(self.showCorrelationsButton)

        self.correlationTab.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget_2 = QWidget(self.tab)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(190, 10, 241, 471))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.probabilityQuestionLabel1 = QLabel(self.layoutWidget_2)
        self.probabilityQuestionLabel1.setObjectName("probabilityQuestionLabel1")

        self.verticalLayout_9.addWidget(
            self.probabilityQuestionLabel1, 0, Qt.AlignHCenter
        )

        self.probabilityQuestion1 = QListWidget(self.layoutWidget_2)
        self.probabilityQuestion1.setObjectName("probabilityQuestion1")
        self.probabilityQuestion1.setAlternatingRowColors(True)
        self.probabilityQuestion1.setProperty("isWrapping", False)
        self.probabilityQuestion1.setSpacing(0)
        self.probabilityQuestion1.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.probabilityQuestion1)

        self.horizontalLayout_7.addLayout(self.verticalLayout_9)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.probabilityAnswer1Label = QLabel(self.layoutWidget_2)
        self.probabilityAnswer1Label.setObjectName("probabilityAnswer1Label")

        self.verticalLayout_11.addWidget(
            self.probabilityAnswer1Label, 0, Qt.AlignHCenter
        )

        self.probabilityAnswer1 = QListWidget(self.layoutWidget_2)
        self.probabilityAnswer1.setObjectName("probabilityAnswer1")
        self.probabilityAnswer1.setAlternatingRowColors(True)
        self.probabilityAnswer1.setSelectionMode(QAbstractItemView.MultiSelection)
        self.probabilityAnswer1.setProperty("isWrapping", False)
        self.probabilityAnswer1.setSpacing(0)
        self.probabilityAnswer1.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.probabilityAnswer1)

        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.layoutWidget_6 = QWidget(self.tab)
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(120, 500, 381, 84))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.correlationTypeBox2 = QGroupBox(self.layoutWidget_6)
        self.correlationTypeBox2.setObjectName("correlationTypeBox2")
        self.correlationTypeBox2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_10 = QVBoxLayout(self.correlationTypeBox2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.positiveProbabilityButton = QRadioButton(self.correlationTypeBox2)
        self.probabilityTypeGroup = QButtonGroup(CorrelationWidget)
        self.probabilityTypeGroup.setObjectName("probabilityTypeGroup")
        self.probabilityTypeGroup.addButton(self.positiveProbabilityButton)
        self.positiveProbabilityButton.setObjectName("positiveProbabilityButton")
        self.positiveProbabilityButton.setChecked(True)

        self.verticalLayout_10.addWidget(self.positiveProbabilityButton)

        self.negativeProbabilityButton = QRadioButton(self.correlationTypeBox2)
        self.probabilityTypeGroup.addButton(self.negativeProbabilityButton)
        self.negativeProbabilityButton.setObjectName("negativeProbabilityButton")

        self.verticalLayout_10.addWidget(self.negativeProbabilityButton)

        self.horizontalLayout_8.addWidget(self.correlationTypeBox2)

        self.probabilitySubmitButton = QPushButton(self.layoutWidget_6)
        self.probabilitySubmitButton.setObjectName("probabilitySubmitButton")

        self.horizontalLayout_8.addWidget(self.probabilitySubmitButton)

        self.showProbabilitiesButton = QPushButton(self.layoutWidget_6)
        self.showProbabilitiesButton.setObjectName("showProbabilitiesButton")

        self.horizontalLayout_8.addWidget(self.showProbabilitiesButton)

        self.correlationTab.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.correlationTab)

        self.finishButton = QPushButton(self.layoutWidget)
        self.finishButton.setObjectName("finishButton")

        self.verticalLayout.addWidget(self.finishButton)

        self.retranslateUi(CorrelationWidget)

        self.correlationTab.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(CorrelationWidget)

    # setupUi

    def retranslateUi(self, CorrelationWidget):
        CorrelationWidget.setWindowTitle(
            QCoreApplication.translate("CorrelationWidget", "Form", None)
        )
        self.formTitleLabel.setText(
            QCoreApplication.translate("CorrelationWidget", "Form Title", None)
        )
        self.correlationQuestionLabel2.setText(
            QCoreApplication.translate("CorrelationWidget", "Question 2", None)
        )
        self.correlationAnswerLabel2.setText(
            QCoreApplication.translate("CorrelationWidget", "Answer Choice 2", None)
        )
        self.correlationQuestionLabel1.setText(
            QCoreApplication.translate("CorrelationWidget", "Question 1", None)
        )
        self.correlationAnswerLabel1.setText(
            QCoreApplication.translate("CorrelationWidget", "Answer Choice 1", None)
        )
        self.correlationTypeBox.setTitle(
            QCoreApplication.translate("CorrelationWidget", "Correlation Type", None)
        )
        self.positiveCorrelationButton.setText(
            QCoreApplication.translate("CorrelationWidget", "Positive", None)
        )
        self.negativeCorrelationButton.setText(
            QCoreApplication.translate("CorrelationWidget", "Negative", None)
        )
        self.correlationSubmitButton.setText(
            QCoreApplication.translate("CorrelationWidget", "Submit", None)
        )
        self.showCorrelationsButton.setText(
            QCoreApplication.translate("CorrelationWidget", "Show Correlations", None)
        )
        self.correlationTab.setTabText(
            self.correlationTab.indexOf(self.tab_2),
            QCoreApplication.translate("CorrelationWidget", "Correlations", None),
        )
        self.probabilityQuestionLabel1.setText(
            QCoreApplication.translate("CorrelationWidget", "Question", None)
        )
        self.probabilityAnswer1Label.setText(
            QCoreApplication.translate("CorrelationWidget", "Answer Choice", None)
        )
        self.correlationTypeBox2.setTitle(
            QCoreApplication.translate("CorrelationWidget", "Probability Type", None)
        )
        self.positiveProbabilityButton.setText(
            QCoreApplication.translate("CorrelationWidget", "Positive", None)
        )
        self.negativeProbabilityButton.setText(
            QCoreApplication.translate("CorrelationWidget", "Negative", None)
        )
        self.probabilitySubmitButton.setText(
            QCoreApplication.translate("CorrelationWidget", "Submit", None)
        )
        self.showProbabilitiesButton.setText(
            QCoreApplication.translate("CorrelationWidget", "Show Probabilities", None)
        )
        self.correlationTab.setTabText(
            self.correlationTab.indexOf(self.tab),
            QCoreApplication.translate(
                "CorrelationWidget", "Probability Modifications", None
            ),
        )
        self.finishButton.setText(
            QCoreApplication.translate("CorrelationWidget", "Finish", None)
        )

    # retranslateUi
