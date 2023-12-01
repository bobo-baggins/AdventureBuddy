import PyQt6.QtCore as Qt
import PyQt6.QtWidgets as Pq
from sheet import Sheet

# Access to command line
import sys

#sys.argv allows cli for app, one QApp instance per application!
#
class Mwindow(Pq.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a layout to hold the sheets
        layout = Pq.QGridLayout()

        # Create some sheets
        sheet1 = Sheet("Sheet 1")
        sheet2 = Sheet("Sheet 2")

        #Create Splitters for run-time resize of sheets
        splitter1 = Pq.QSplitter(Qt.Qt.Orientation.Horizontal)
        splitter1.addWidget(sheet1)
        splitter1.addWidget(sheet2)

        # Add the sheets to the layout
        layout.addWidget(splitter1)

        # Create a widget to hold the layout
        widget = Pq.QWidget()
        widget.setLayout(layout)

        # Set the widget as the central widget of the main window
        self.setCentralWidget(widget)


app = Pq.QApplication(sys.argv)


#window = QPushButton("Touch Me")
window = Mwindow()
window.show()
#Windows are hidden by default


#Start event looP
app.exec()


