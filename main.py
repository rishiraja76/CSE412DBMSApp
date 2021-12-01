import sys
import backend

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


widgets = {"button1": [],
           "backbutton": [],
           "ticketbut": [],
           "flightbut": [],
           "airlinerbut": []
           }


def homepage():
    # user information button widget
    button1 = QPushButton("User Information")
    widgets["button1"].append(button1)
    button1.clicked.connect(user_info)
    grid.addWidget(widgets["button1"][-1], 0, 0)

    # ticket information button
    ticketbut = QPushButton("Ticket Information")
    widgets["ticketbut"].append(ticketbut)
    ticketbut.clicked.connect(ticket_info)
    grid.addWidget(widgets["ticketbut"][-1], 1, 0)

    flightbut = QPushButton("Flight Information")
    widgets["flightbut"].append(flightbut)
    flightbut.clicked.connect(flight_info)
    grid.addWidget(widgets["flightbut"][-1], 2, 0)

    airlinerbut = QPushButton("Airliner Information")
    widgets["airlinerbut"].append(airlinerbut)
    airlinerbut.clicked.connect(airliner_info)
    grid.addWidget(widgets["airlinerbut"][-1], 3, 0)


def user_info():
    # clears previous widgets
    clear_widgets()

    # back button to return to home
    backbutton = QPushButton("Back")
    # backbutton.setAlignment(QtCore.Qt.AlignRight)
    grid.addWidget(backbutton, 0, 0)
    widgets["backbutton"].append(backbutton)
    backbutton.clicked.connect(show_homepage)
    grid.addWidget(widgets["backbutton"][-1], 0, 0)


def ticket_info():
    # clears previous wdgets
    clear_widgets()

    # back button to go to homeapge
    backbutton = QPushButton("Back")
    # backbutton.setAlignment(QtCore.Qt.AlignRight)
    grid.addWidget(backbutton, 0, 0)
    widgets["backbutton"].append(backbutton)
    backbutton.clicked.connect(show_homepage)
    grid.addWidget(widgets["backbutton"][-1], 0, 0)


def flight_info():
    # clears previous wdgets
    clear_widgets()

    # back button to go to homeapge
    backbutton = QPushButton("Back")
    # backbutton.setAlignment(QtCore.Qt.AlignRight)
    grid.addWidget(backbutton, 0, 0)
    widgets["backbutton"].append(backbutton)
    backbutton.clicked.connect(show_homepage)
    grid.addWidget(widgets["backbutton"][-1], 0, 0)


def airliner_info():
    # clears previous wdgets
    clear_widgets()

    # back button to go to homeapge
    backbutton = QPushButton("Back")
    # backbutton.setAlignment(QtCore.Qt.AlignRight)
    grid.addWidget(backbutton, 0, 0)
    widgets["backbutton"].append(backbutton)
    backbutton.clicked.connect(show_homepage)
    grid.addWidget(widgets["backbutton"][-1], 0, 0)


def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


def show_homepage():
    clear_widgets()
    homepage()


def next_tab():
    clear_widgets()
    user_info()


if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Flight Information")
    # test = QPushButton('test')
    # window.move(2700, 200)
    window.setFixedWidth(1000)

    grid = QGridLayout()
    homepage()
    # test = QPushButton('test')
    #  grid.addWidget(test, 0, 0)

    window.setLayout(grid)

    # hbox = QHBoxLayout(window)
    window.show()

    sys.exit(app.exec_())
