import sys
import backend

from PyQt5.QtWidgets import *

widgets = {"button1": [],
           "backbutton": [],
           "ticketbut": [],
           "flightbut": [],
           "airlinerbut": [],
           "userTable": []
           }

user_data = {'First Name': backend.firstname,
            'Last Name': backend.firstname,
            'User Name': backend.firstname,
            'Pass Word': backend.firstname,
            'Email': backend.firstname,
            'Address': backend.firstname,
            'Phone Number': backend.firstname,
            'Credit Card Number': backend.firstname}

ticket_data = {'Ticket Status': backend.ticketstatus,
                'Ticket ID': backend.ticketid_tr,
                'Price': backend.price,
                'Credit Card Number': backend.creditcardnumber_tr}

flight_data = {'Flight Status': backend.flightstatus,
            'Flight Number': backend.flightnumber_f,
            'Arrival Time': backend.arrivaltime,
            'Departure Time': backend.departuretime,
            'Departure Location': backend.departuretime,
            'Destination': backend.destination,
            'Ticket ID': backend.ticketid_f}

airliner_data = {'Plane Type': backend.planetype,
            'Airliner Name': backend.airlinername,
            'Flight Number': backend.flightnumber_a}

class TableView(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setData(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)

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
    clear_widgets()

    userTable = TableView(user_data, len(backend.firstname), len(user_data))
    backbutton = QPushButton("Back")

    grid.addWidget(userTable, 0, 0)
    grid.addWidget(backbutton, 1, 0)

    widgets["backbutton"].append(backbutton)
    widgets["userTable"].append(userTable)
    backbutton.clicked.connect(show_homepage)

def ticket_info():
    clear_widgets()

    userTable = TableView(ticket_data, len(backend.ticketstatus), len(user_data))
    backbutton = QPushButton("Back")

    grid.addWidget(userTable, 0, 0)
    grid.addWidget(backbutton, 1, 0)

    widgets["backbutton"].append(backbutton)
    widgets["userTable"].append(userTable)
    backbutton.clicked.connect(show_homepage)

def flight_info():
    clear_widgets()

    userTable = TableView(flight_data, len(backend.flightstatus), len(user_data))
    backbutton = QPushButton("Back")

    grid.addWidget(userTable, 0, 0)
    grid.addWidget(backbutton, 1, 0)

    widgets["backbutton"].append(backbutton)
    widgets["userTable"].append(userTable)
    backbutton.clicked.connect(show_homepage)

def airliner_info():
    clear_widgets()

    userTable = TableView(airliner_data, len(backend.planetype), len(user_data))
    backbutton = QPushButton("Back")

    grid.addWidget(userTable, 0, 0)
    grid.addWidget(backbutton, 1, 0)

    widgets["backbutton"].append(backbutton)
    widgets["userTable"].append(userTable)
    backbutton.clicked.connect(show_homepage)

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
    window.setFixedWidth(1000)

    grid = QGridLayout()
    homepage()

    window.setLayout(grid)

    window.show()

    sys.exit(app.exec()_)
