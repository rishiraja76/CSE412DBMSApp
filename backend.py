import psycopg2
from psycopg2 import *

try:
    conn = psycopg2.connect(user="anthony",
                            host="localhost",
                            port="8888",
                            database="midterm")
    cursor = conn.cursor()

    postgresSQL_user = "SELECT * FROM users"
    cursor.execute(postgresSQL_user)
    user_records = cursor.fetchall()

    firstname = []
    lastname = []
    username = []
    password = []
    email = []
    address = []
    phonenumber = []
    creditcardnumber_u = []

    for row in user_records:
        firstname.append(row[0])
        lastname.append(row[1])
        username.append(row[2])
        password.append(row[3])
        email.append(row[4])
        address.append(row[5])
        phonenumber.append(row[6])
        creditcardnumber_u.append(row[7])

    postgresSQL_airliner = "SELECT * FROM airliner"
    cursor.execute(postgresSQL_airliner)
    airliner_records = cursor.fetchall()

    planetype = []
    airlinername = []
    flightnumber_a = []
    for row in airliner_records:
        planetype.append(row[0])
        airlinername.append(row[1])
        flightnumber_a.append(row[2])

    postgresSQL_ticket_reservation = "SELECT * FROM ticket_reservation"
    cursor.execute(postgresSQL_ticket_reservation)
    ticket_reservation_records = cursor.fetchall()

    ticketstatus = []
    ticketid_tr = []
    price = []
    creditcardnumber_tr = []

    for row in ticket_reservation_records:
        ticketstatus.append(row[0])
        ticketid_tr.append(row[1])
        price.append(row[2])
        creditcardnumber_tr.append(row[3])

    postgresSQL_flight = "SELECT * FROM flight"
    cursor.execute(postgresSQL_flight)
    flight_records = cursor.fetchall()

    flightstatus = []
    flightnumber_f = []
    arrivaltime = []
    departuretime = []
    departurelocation = []
    destination = []
    ticketid_f = []
    for row in flight_records:
        flightstatus.append(row[0])
        flightnumber_f.append(row[1])
        arrivaltime.append(row[2])
        departuretime.append(row[3])
        departurelocation.append(row[4])
        destination.append(row[5])
        ticketid_f.append(row[6])

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if(conn):
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")

