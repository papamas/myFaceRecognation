import json

import mysql.connector
from numpy.distutils.fcompiler import none


class FaceMySQL:
    def __init__(self):
        self.host = "localhost"
        self.database = "api"
        self.user = "root"
        self.password = ""

        self.con = mysql.connector.connect(host=self.host, database=self.database, user=self.user,
                                           password=self.password)

        if self.con.is_connected():
            db_info = self.con.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            self.cursor = self.con.cursor()

    def setFace(self, pns, data):
        face_data = json.dumps(data.tolist())
        sql = "INSERT INTO face_register (pns_id, json) VALUES (%s, %s)"
        self.query(sql, (pns, face_data))
        print(self.cursor.rowcount, "record inserted")

    def getFace(self, pns):
        sql = "SELECT json FROM face_register WHERE pns_id= %s"
        self.query(sql, (pns,))

    def updateFace(self, pns, data):
        face_data = json.dumps(data.tolist())
        sql = "UPDATE face_register SET json=%s WHERE pns_id=%s"
        self.query(sql, (face_data, pns))
        print("record update")

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def num_rows(self):
        return self.cursor.rowcount

    def result(self):
        return self.cursor.fetchall()

    def row(self):
        return self.cursor.fetchone()

    def commit(self):
        self.con.commit()

    def close(self, commit=True):
        if commit:
            self.commit()

        if self.con.is_connected():
            self.cursor.close()
            self.con.close()
            print("MySQL connection is closed")
