
from flask import json
from numpy.distutils.fcompiler import none
import mysql.connector
from errno import errorcode


import mysql.connector
from mysql.connector import Error

#create connection
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def face_register(pns, data):
    # Pickle the list into a string
    # face_pickled_data = pickle.dumps(json)
    face_pickled_data = json.dumps(data.tolist())

    # defining the Query
    query = "INSERT INTO face_register (pns_id, json) VALUES (%s, %s)"

    # storing values in a variable
    # values = ("A8ACA79748773912E040640A040269BB", face_pickled_data)

    # executing the query with values
    cursor.execute(query, (pns, face_pickled_data))

    # to make final output we have to run the 'commit()' method of the database object
    db.commit()

    return print(cursor.rowcount, "record inserted")


def face_data(pns):
    query = "SELECT json FROM face_register WHERE pns_id= %s"
    cursor.execute(query, (pns,))
    row = cursor.fetchone()
    # face = pickle.loads(row[0])
    face = json.loads(row[0])
    return face
