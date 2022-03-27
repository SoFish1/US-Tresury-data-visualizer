
from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from os import environ
from time import sleep

db_host_name = environ["DB_HOST_NAME"]
db_name = environ["DB_NAME"]
db_password = environ["DB_PASSWORD"]
db_user = environ["DB_USER"]
db_port = environ["DATABASE_PORT"]

while True:
    try:
        conn =connect(host=db_host_name,\
                database=db_name,\
                user=db_user,\
                password=db_password,\
                cursor_factory= RealDictCursor) 
        cursor=conn.cursor()
        print("Database connection is succesful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        sleep(2)
        break


