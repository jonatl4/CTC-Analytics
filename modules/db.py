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
        self.cursor.execute('''CREATE TABLE data (date text, account_id text, account_name text, clicks INT, cpc FLOAT, cpm FLOAT, impressions FLOAT, ctr FLOAT, frequency FLOAT, reach INT, PRIMARY KEY(date, account_id))''')
        self.cursor.execute('''CREATE TABLE scores (date text, account_id text, account_name text, ctc_final_score FLOAT,  ctr_score FLOAT, cpc_score FLOAT, click_score FLOAT, frequency_score FLOAT, cpm_score FLOAT, impression_score FLOAT, reach_score FLOAT, PRIMARY KEY(date, account_id))''')
        self.cursor.execute(''' CREATE TABLE percent (date text, account_id text, account_name text, ctr_change text, cpc_score FLOAT, click_change text, frequency_change text, cpm_change text, impression_change text, reach_score text, PRIMARY KEY (date, account_id))''')

    
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
                self.cursor.execute("INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?,?)", (datum['date_start'], acc_id, datum['account_name'], datum['clicks'], datum['cpc'], datum['cpm'], datum['impressions'], datum['ctr'], datum['frequency'], datum['reach']))
            except Exception, e:
                pass
                
        self.conn.commit()
        return
    
    def insertScores(self, data, acc_name, acc_id, date):
        try:
            self.cursor.execute("INSERT INTO scores VALUES (?,?,?,?,?,?,?,?,?,?,?)", (date, acc_id, acc_name, data['ctc_final_score'], data['ctr_score'], data['cpc_score'], data['click_score'], data['frequency_score'], data['cpm_score'], data['impression_score'], data['reach_score']))
        except Exception, e:
            pass

        self.conn.commit()
        return
    
    def insertPerChange(self, data, acc_name, acc_id, date):
        try:
            self.cursor.execute("INSERT INTO percent VALUES (?,?,?,?,?,?,?,?,?,?)", (date, acc_id, acc_name, data['ctr_change'], data['cpc_change'], data['click_change'], data['frequency_change'], data['cpm_change'], data['impression_change'], data['reach_change']))
        
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
    
    def checkForPastScore(self, acc_id, date):
        query = """
                SELECT *
                FROM scores
                WHERE account_id = '{%account_id%}' and date = '{%date%}'
                """
        query = query.replace("{%account_id%}", acc_id)
        query = query.replace("{%date%}", date)
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        if len(data) == 0:
            return True
        
        return False
    
    
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
            datum['clicks_value'] = d[3]
            datum['cpc_value'] = d[4]
            datum['cpm_value'] = d[5]
            datum['impressions_value'] = d[6]
            datum['ctr_value'] = d[7]
            datum['frequency_value'] = d[8]
            datum['reach_value'] = d[9]
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
        return_data['clicks_value'] = data[3]
        return_data['cpc_value'] = data[4]
        return_data['cpm_value'] = data[5]
        return_data['impressions_value'] = data[6]
        return_data['ctr_value'] = data[7]
        return_data['frequency_value'] = data[8]
        return_data['reach_value'] = data[9]
        

        return return_data