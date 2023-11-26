from PyQt6 import QtWidgets


class Sheet(QtWidgets.QWidget):
    def __init__(self, title, content={}):
        super().__init__()
        self.title = title
        self.content = content

        self.setWindowTitle(self.title)


    