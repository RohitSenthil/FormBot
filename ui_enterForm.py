# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enterForm.ui'
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
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_FormWidget(object):
    def setupUi(self, FormWidget):
        if not FormWidget.objectName():
            FormWidget.setObjectName("FormWidget")
        FormWidget.resize(540, 91)
        self.verticalLayout = QVBoxLayout(FormWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLabel = QLabel(FormWidget)
        self.formLabel.setObjectName("formLabel")

        self.horizontalLayout.addWidget(self.formLabel)

        self.formLineEdit = QLineEdit(FormWidget)
        self.formLineEdit.setObjectName("formLineEdit")

        self.horizontalLayout.addWidget(self.formLineEdit)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.submitButton = QPushButton(FormWidget)
        self.submitButton.setObjectName("submitButton")

        self.verticalLayout.addWidget(self.submitButton)

        self.retranslateUi(FormWidget)

        QMetaObject.connectSlotsByName(FormWidget)

    # setupUi

    def retranslateUi(self, FormWidget):
        FormWidget.setWindowTitle(
            QCoreApplication.translate("FormWidget", "Form", None)
        )
        self.formLabel.setText(
            QCoreApplication.translate("FormWidget", "Enter form link:", None)
        )
        self.submitButton.setText(
            QCoreApplication.translate("FormWidget", "Submit", None)
        )

    # retranslateUi
