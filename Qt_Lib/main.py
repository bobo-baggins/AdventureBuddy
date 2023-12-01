import PyQt6.QtCore as Qt
import PyQt6.QtWidgets as Pq

# Access to command line
import sys

#sys.argv allows cli for app, one QApp instance per application!
#
class Mwindow(Pq.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = Pq.QPushButton("Touch Me!")

        self.setCentralWidget
    

app = Pq.QApplication(sys.argv)


#window = QPushButton("Touch Me")
window = Mwindow()
window.show()
#Windows are hidden by default


#Start event looP
app.exec()


