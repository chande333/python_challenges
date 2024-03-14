import vertica_python
import os
import json

def getVars():
    global conn_info
    
    with open("internal_vars.json", "r") as file:
        data=json.load(file)

        conn_info = {
            "host": data['vertica_host'],
            "port": data['vertica_port'],
            "user": data['vertica_user'],
            "password": os.environ.get("zmypass"),
            "database": data['vertica_dbnm']
        }

def connect_to_vertica():
    global conn_info    
    connection = vertica_python.connect(**conn_info)
    return connection

getVars()