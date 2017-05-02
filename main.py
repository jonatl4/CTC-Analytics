from modules.api import FacebookAPI
from modules.db import Database
from modules.algstats import pstdev, mean




def calculate_ctc_score(campaign_stats):
    """Returns a ctc score from a given campaign"""

<<<<<<< HEAD
    ctrScore, cpcScore, clickScore, frequencyScore, cpmScore, impressionsScore, reachScore = 0, 0, 0, 0, 0, 0, 0 
    ctr_history, cpc_history, click_history, frequency_history, cpm_history, impressions_history, reach_history = [], [], [], [], [], [], []
    numberOfFields = 7
    
    """generate history of data"""
    
    #shows populated list
    print campaign_stats
   
    
=======
    ctrScore, cpcScore, clickScore, frequencyScore = 0, 0, 0, 0
   
>>>>>>> origin/master
    for keys in campaign_stats:
        for value in keys:
            if value == 'ctr':          ctr_history.append(float(keys[value]))
            if value == 'cpc':          cpc_history.append(float(keys[value]))
            if value == 'clicks':       click_history.append(int(keys[value]))
            if value == 'frequency':    frequency_history.append(float(keys[value]))
            if value == 'cpm':          cpm_history.append(float(keys[value]))
            if value == 'impressions':  impressions_history.append(int(keys[value]))
            if value == 'reach':        reach_history.append(int(keys[value]))
    
    


    #shows empty list!
    print campaign_stats

    
    
    for keys in campaign_stats:
        if keys.get("date_start") == "2017-04-25":
            for value in keys:
                
                
                if value == 'ctr':
                    field_mean = mean(ctr_history)
                    standard_deviation = pstdev(ctr_history)
                    if keys[value] > field_mean + standard_deviation:
                        ctrScore += 1
                        
                if value == "cpc":
                    field_mean = mean(cpc_history)
                    standard_deviation = pstdev(cpc_history)
                    if keys[value] > field_mean + standard_deviation:
                        cpcScore += 1
                        
                if value == 'clicks':
                    field_mean = mean(click_history)
                    standard_deviation = pstdev(click_history)
                    if keys[value] > field_mean + standard_deviation:
                        clickScore += 1
                        
                if value == "frequency":
                    field_mean = mean(frequency_history)
                    standard_deviation = pstdev(frequency_history)
                    if keys[value] > field_mean + standard_deviation:
                        frequencyScore += 1
                        
                if value == "cpm":
                    field_mean = mean(cpm_history)
                    standard_deviation = pstdev(cpm_history)
                    if keys[value] > field_mean + standard_deviation:
                        cpmScore += 1
                        
                if value == "impressions":
                    field_mean = mean(impressions_history)
                    standard_deviation = pstdev(impressions_history)
                    if keys[value] > field_mean + standard_deviation:
                        impressionsScore += 1
                        
                if value == "reach":
                    field_mean = mean(reach_history)
                    standard_deviation = pstdev(reach_history)
                    if keys[value] > field_mean + standard_deviation:
                        reachScore += 1
                
                    
            
        
    """Score * (Weight) determines how much influence a specific field has on the algorithm.
    Score = a we come up with based on the data
    Weight = how important we think that field is in making a decision (out of 1)
    numberOfFields = the number of fields that will give us a number between 0 and 1 when divided
    """
    
    
    finalAlgorithm = (ctrScore*(1) 
                      + cpcScore*(1) 
                      + clickScore*(1) 
                      + frequencyScore*(1) 
                      )/ numberOfFields
    
    print('CTC SCORE: {}'.format(finalAlgorithm))
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
	#print campaign_stats
        #campaign_dict = FacebookConnection.create_campaign_stats(campaign_stats)
        ctc_score = calculate_ctc_score(campaign_stats)

if __name__ == '__main__':
    main()
