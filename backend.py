import psycopg2
from psycopg2 import *

try:
    conn = psycopg2.connect(user="pjbogdan",
                            host="localhost",
                            port="8888",
                            database="cse412_finalproj")
    cursor = conn.cursor()
    tmp = "airliner"
    postgresSQL_test_user = "SELECT * FROM {}".format(tmp)
    # print("PostgresSQL server information")
    # print(conn.get_dsn_parameters(), "\n")
    cursor.execute(postgresSQL_test_user)
    user_records = cursor.fetchall()

    # print("Displays each row and it's columns values")
    firstname = []
    for row in user_records:
        firstname.append(row[0])
        # print("Last Name: ", row[1])
        # print("username: ", row[2])
        # print("password: ", row[3])
        # print("email: ", row[4])
        # print("address: ", row[5])
        # print("phone number: ", row[6])
        # print("credit card number: ", row[7])
    print(firstname)
    # record = cursor.fetchone()
    # print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if(conn):
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")

