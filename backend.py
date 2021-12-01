import psycopg2
from psycopg2 import *

try:
    conn = psycopg2.connect(user="pjbogdan",
                            host="localhost",
                            port="8888",
                            database="cse412_finalproj")
    cursor = conn.cursor()

    print("PostgresSQL server information")
    print(conn.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version();")

    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if(conn):
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")

