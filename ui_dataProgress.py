# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataProgress.ui'
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
    QLabel,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_FormDataWidget(object):
    def setupUi(self, FormDataWidget):
        if not FormDataWidget.objectName():
            FormDataWidget.setObjectName("FormDataWidget")
        FormDataWidget.resize(291, 197)
        self.layoutWidget = QWidget(FormDataWidget)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 271, 161))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.formProgressBar = QProgressBar(self.layoutWidget)
        self.formProgressBar.setObjectName("formProgressBar")
        self.formProgressBar.setValue(0)
        self.formProgressBar.setTextVisible(True)

        self.verticalLayout.addWidget(self.formProgressBar)

        self.estimatedTimeLabel = QLabel(self.layoutWidget)
        self.estimatedTimeLabel.setObjectName("estimatedTimeLabel")

        self.verticalLayout.addWidget(self.estimatedTimeLabel)

        self.startFormButton = QPushButton(self.layoutWidget)
        self.startFormButton.setObjectName("startFormButton")
        self.startFormButton.setEnabled(True)

        self.verticalLayout.addWidget(self.startFormButton)

        self.retranslateUi(FormDataWidget)

        QMetaObject.connectSlotsByName(FormDataWidget)

    # setupUi

    def retranslateUi(self, FormDataWidget):
        FormDataWidget.setWindowTitle(
            QCoreApplication.translate("FormDataWidget", "Form", None)
        )
        self.label.setText(
            QCoreApplication.translate("FormDataWidget", "Create Data", None)
        )
        self.estimatedTimeLabel.setText(
            QCoreApplication.translate("FormDataWidget", "Est time.", None)
        )
        self.startFormButton.setText(
            QCoreApplication.translate("FormDataWidget", "Start Form Input", None)
        )

    # retranslateUi
