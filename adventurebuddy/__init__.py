import os
import sys

from PySide6.QtWidgets import QApplication

from . import ui


def run():
    app = QApplication(sys.argv)
    ftw = ui.FileTreeWidget(os.getcwd())
    ftw.show()
    sys.exit(app.exec())
