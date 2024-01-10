import io
import os
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from mainWindow import MainWindow

basedir = os.path.dirname(__file__)
buffer = io.StringIO()
sys.stdout = buffer
sys.stderr = buffer
try:
    from ctypes import windll

    myappid = "formbot v2.0"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setWindowIcon(QIcon(os.path.join(basedir, "RobotIcon.ico")))
    window.show()
    sys.exit(app.exec())
