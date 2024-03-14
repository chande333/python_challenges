import pymysql
import os
import json

def getVars():
    global db_config
    
    with open("internal_vars.json", "r") as file:
        data=json.load(file)
    
        db_config = {
            "host": data['mariadb_host'],
            "user": data['mariadb_user'],
            "password": os.environ.get("mariadb_pass"),
            "database": data['mariadb_dbnm']
        }

def connect_to_database():
    try:
        globconn = pymysql.connect(**db_config)
        if globconn.open:
            print("Connected to MySQL/MariaDB database")
            return globconn
    except pymysql.Error as e:
        print(f"Error connecting to MySQL/MariaDB database: {e}")
        return None


def close_connection(connection):
    if connection:
        connection.close()
        print("Connection to MySQL/MariaDB database closed")


getVars()