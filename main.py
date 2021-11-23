import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import psycopg2

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.setCentralWidget(button)

try:
    conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
except:
    print("I am unable to connect to the database")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()