import sqlite3
import os


class Database:
    def __init__(self):
        "If the database already exists, initalize a connection. Otherwise create the database with the correct tables."
        if os.path.exists("database.db"):
            self.initalizeConnection()
        else:
            self.createDatabase()
    
    def createDatabase(self):
        "Creates a sqllite database if it does not already exist"
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE data (date datetime, account_id INT, account_name INT, clicks INT, cpc FLOAT, cpm FLOAT, ctr FLOAT, frequency FLOAT, reach INT, PRIMARY KEY(date, account_id))''')
    
    def initalizeConnection(self):
        "Initializes a connection with an already existing sqllite database"
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
    
    def close(self):
        "Closes a connection with the sqllite databsae"
        self.conn.close()