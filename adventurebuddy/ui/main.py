import PySide6.QtCore as Qt
import PySide6.QtWidgets as pq

import sys  # Access to command line

#sys.argv allows cli for app, one QApp instance per application!
#
class Mwindow(pq.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = pq.QPushButton("Touch Me!")

        self.setCentralWidget


app = pq.QApplication(sys.argv)


#window = QPushButton("Touch Me")
window = Mwindow()
window.show()
#Windows are hidden by default


#Start event looP
app.exec()
