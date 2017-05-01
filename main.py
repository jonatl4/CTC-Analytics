from modules.api import FacebookAPI
from modules.db import Database




def calculate_ctc_score(campaign_stats):
    """Returns a ctc score from a given campaign"""

    ctrScore, cpcScore, clickScore, frequencyScore = 0, 0, 0, 0
    
    for keys in campaign_stats:
        for value in keys:
            
            """The percentage of times people saw your ad and performed a click"""              
            if value == 'ctr':
                if keys[value] < 1:
                    ctrScore = 0.2
                elif keys[value] > 1 and keys[value] < 3:
                    ctrScore = 0.4
                elif keys[value] > 3 and keys[value] < 6:
                    ctrScore = 0.65
                elif keys[value] > 6 and keys[value] < 8:
                    ctrScore = 0.85
                elif keys[value] > 8:
                    ctrScore = 1
                
            """The average cost for each click"""    
            if value == 'cpc':
                if keys[value] < 0.25:
                    cpcScore = 0.2
                elif keys[value] > 0.25 and keys[value] < 0.50:
                    cpcScore = 0.5
                elif keys[value] > 0.50:
                    cpcScore = 0.7     
                    
            """The number of clicks on your ads"""
            if value == 'clicks':
                if keys[value] < 1000:
                    clickScore = 0
                elif keys[value] > 1000 and keys[value] < 10000:
                    clickScore = 0.2
                elif keys[value] > 10000 and keys[value] < 50000:
                    clickScore = 0.3
                elif keys[value] > 50000 and keys[value] < 200000:
                    clickScore = 0.5
                elif keys[value] > 200000 and keys[value] < 300000:
                    clickScore = 0.7
                elif keys[value] > 300000 and keys[value] < 500000:
                    clickScore = 0.9
                elif keys[value] > 500000:
                    clickScore = 1
                  
            """The average number of times each person saw your ad"""  
            if value == 'frequency':
                if keys[value] < 1:
                    frequencyScore = 0.2
                elif keys[value] > 1 and keys[value] < 3:
                    frequencyScore = 0.6
                elif keys[value] > 3 and keys[value] < 6:
                    frequencyScore = 0.9
                elif keys[value] > 6 and keys[value] < 9:
                    frequencyScore = 1
                elif keys[value] > 9 and keys[value] < 12:
                    frequencyScore = 0.7
                elif keys[value] > 12:
                    frequencyScore = 0.4

        """Score * (Weight) determines how much influence a specific field has on the algorithm.
        Score = a we come up with based on the data
        Weight = how important we think that field is in making a decision (out of 1)
        numberOfFields = the number of fields that will give us a number between 0 and 1 when divided
        """
    numberOfFields = 4
    
    finalAlgorithm = (ctrScore*(.35) 
                      + cpcScore*(.30) 
                      + clickScore*(.25) 
                      + frequencyScore*(.10) 
                      )/ numberOfFields
    
    #print('CTC SCORE: {}'.format(finalAlgorithm))
    return finalAlgorithm




def create_structure(facebook_ad_accounts):
    """Returns a dictionary of the ad accounts with the following format {AccountName1: AccountID1, AccountName2: AccountID2...}"""
    ad_account_ids = ['1699751017001576'] #Axe Bat Account ID
    ad_account = {}
    for acc in facebook_ad_accounts:
        acc_strip = acc['id'].strip('act_')
        if acc_strip in ad_account_ids:
            ad_account[acc['name']] = acc['id']

    return ad_account



def main():
    """The controller of the entire program. It will handle initializing the facebook API connection, and call various modules in the program to perform tasks such as 
        grabbing the facebook ad accounts, storing values in the database, generating the html document and sending the html document to a list of clients"""
    FacebookConnection = FacebookAPI() # Create the facebook api object
    FacebookAdAccounts = create_structure(FacebookConnection.get_accounts()) #dictionary of account name, id
    CTCDatabase = Database()

    for acc_name, acc_id in FacebookAdAccounts.items(): #iterate through all account names, ids
        acc_campaign_id = FacebookConnection.get_prospecting_campaign_id(acc_id) #Grab the prospecting campaign id
        campaign_stats = FacebookConnection.get_campaign_stats(acc_campaign_id) #Get all the necessary data points required to calculate score
        ctc_score = calculate_ctc_score(campaign_stats)

if __name__ == '__main__':
    main()
