# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finishDialogue.ui'
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
    QAbstractButton,
    QApplication,
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_FinishDialogue(object):
    def setupUi(self, FinishDialogue):
        if not FinishDialogue.objectName():
            FinishDialogue.setObjectName("FinishDialogue")
        FinishDialogue.resize(302, 168)
        self.layoutWidget = QWidget(FinishDialogue)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 261, 141))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.showCorrelationsFinishButton = QPushButton(self.layoutWidget)
        self.showCorrelationsFinishButton.setObjectName("showCorrelationsFinishButton")

        self.horizontalLayout.addWidget(self.showCorrelationsFinishButton)

        self.showProbabilitiesFinishButton = QPushButton(self.layoutWidget)
        self.showProbabilitiesFinishButton.setObjectName(
            "showProbabilitiesFinishButton"
        )

        self.horizontalLayout.addWidget(self.showProbabilitiesFinishButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Yes
        )
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(FinishDialogue)
        self.buttonBox.accepted.connect(FinishDialogue.accept)
        self.buttonBox.rejected.connect(FinishDialogue.reject)

        QMetaObject.connectSlotsByName(FinishDialogue)

    # setupUi

    def retranslateUi(self, FinishDialogue):
        FinishDialogue.setWindowTitle(
            QCoreApplication.translate("FinishDialogue", "Dialog", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "FinishDialogue", "Are you sure you would like to move on?", None
            )
        )
        self.showCorrelationsFinishButton.setText(
            QCoreApplication.translate("FinishDialogue", "Show Correlations", None)
        )
        self.showProbabilitiesFinishButton.setText(
            QCoreApplication.translate("FinishDialogue", "Show Probabilites", None)
        )

    # retranslateUi
