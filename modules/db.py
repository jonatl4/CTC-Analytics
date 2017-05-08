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
        self.cursor.execute('''CREATE TABLE data (date text, account_id text, account_name text, clicks INT, cpc FLOAT, cpm FLOAT, ctr FLOAT, frequency FLOAT, reach INT, PRIMARY KEY(date, account_id))''')
    
    def initalizeConnection(self):
        "Initializes a connection with an already existing sqllite database"
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
    
    def close(self):
        "Closes a connection with the sqllite databsae"
        self.conn.close()

    def insertCampaignData(self, data, acc_id):
        date_set = set()
        for datum in data:
            try:
                self.cursor.execute("INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?)", (datum['date_start'], acc_id, datum['account_name'], datum['clicks'], datum['cpc'], datum['cpm'], datum['ctr'], datum['frequency'], datum['reach']))
            except Exception, e:
                pass
                
        self.conn.commit()
        return


    def getListOfAccountIDs(self):
        "Grab a unique list of account ids"
        query = """
                SELECT DISTINCT account_id
                FROM data
                """
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        if len(data) != 0:
            data = data[0]

        return data
    
    
    def getCampaignData(self, acc_id, today):
        "Given an account id and the current date, grab all the data except whatever is today's date."
        query = """
                SELECT *
                FROM data
                WHERE account_id = '{%account_id%}' and date != '{%date%}'
                """
        query = query.replace("{%account_id%}", acc_id)
        query = query.replace("{%date%}", today)
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        #Create a list of dictionaries. This will make it easier to grab the data later.
        return_data = []
        for d in data:
            datum = {}
            datum['date'] = d[0]
            datum['account_id'] = d[1]
            datum['account_name'] = d[2]
            datum['clicks'] = d[3]
            datum['cpc'] = d[4]
            datum['cpm'] = d[5]
            datum['ctr'] = d[6]
            datum['frequency'] = d[7]
            datum['reach'] = d[8]
            return_data.append(datum)

        return return_data
        
    def getCurrentDateValues(self, acc_id, today):
        "Given an account id and the current date, grab that current's date value"
        query = """
                SELECT *
                FROM data
                WHERE account_id = '{%account_id%}' and date = '{%date%}'
                """
        query = query.replace("{%account_id%}", acc_id)
        query = query.replace("{%date%}", today)
        self.cursor.execute(query)
        data = self.cursor.fetchall()[0]

        #Create a dictionary with the values. This will make it easier to grab the data later
        return_data = {}
        return_data['date'] = data[0]
        return_data['account_id'] = data[1]
        return_data['account_name'] = data[2]
        return_data['clicks'] = data[3]
        return_data['cpc'] = data[4]
        return_data['cpm'] = data[5]
        return_data['ctr'] = data[6]
        return_data['frequency'] = data[7]
        return_data['reach'] = data[8]
        

        return return_data