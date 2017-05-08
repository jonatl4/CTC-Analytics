from modules.api import FacebookAPI
from modules.db import Database
from modules.algstats import pstdev, mean
import time



def calculate_ctc_score(campaign_data_set, curr_date_values):
    #campaign_data_set is going to be a set of dictionaries nested in to a list. It is going to have all the campaigns data
    #except for today. See bellow on how to grab the values out.
    for datum in campaign_data_set:
        print datum['date']
        print datum['account_id']
        print datum['account_name']
        print datum['clicks']
        print datum['cpc']
        print datum['cpm']
        print datum['ctr']
        print datum['frequency']
        print datum['reach']
    
    #curr_data_values is going to be todays values compared against campaign_data_set. Its only a dictionary. See below for grabbing the data
    print curr_date_values['date']
    print curr_date_values['account_id']
    print curr_date_values['account_name']
    print curr_date_values['clicks']
    print curr_date_values['cpc']
    print curr_date_values['cpm']
    print curr_date_values['ctr']
    print curr_date_values['frequency']
    print curr_date_values['reach']
    
    

def calculate_ctc_score_old(campaign_stats):
    """Returns a ctc score from a given campaign"""

    ctrScore, cpcScore, clickScore, frequencyScore, cpmScore, impressionsScore, reachScore = 0, 0, 0, 0, 0, 0, 0 
    ctr_history, cpc_history, click_history, frequency_history, cpm_history, impressions_history, reach_history = [], [], [], [], [], [], []
    numberOfFields = 7
    
    """generate history of data"""
   
    campaign_stat_list = list(campaign_stats)

    for keys in campaign_stat_list:
        for value in keys:
            if value == 'ctr':          ctr_history.append(float(keys[value]))
            if value == 'cpc':          cpc_history.append(float(keys[value]))
            if value == 'clicks':       click_history.append(int(keys[value]))
            if value == 'frequency':    frequency_history.append(float(keys[value]))
            if value == 'cpm':          cpm_history.append(float(keys[value]))
            if value == 'impressions':  impressions_history.append(int(keys[value]))
            if value == 'reach':        reach_history.append(int(keys[value]))
    

    
    for keys in campaign_stat_list:
        if keys.get("date_start") == "2017-05-01":
            for value in keys:
                
                
                if value == 'ctr':
                    field_mean = mean(ctr_history)
                    standard_deviation = pstdev(ctr_history)
                    if (float(keys[value]) > float(field_mean + standard_deviation*2)):
                        ctrScore += 1
                    if (float(keys[value]) > float(field_mean + standard_deviation)):
                        ctrScore += 0.75
                    elif (float(keys[value]) > float(field_mean - standard_deviation) and float(keys[value]) < float(field_mean + standard_deviation)):
                        ctrScore += 0.5
                    elif (float(keys[value]) < float(field_mean - standard_deviation)):
                        ctrScore += 0.25
                    elif (float(keys[value]) < float(field_mean - standard_deviation*2)):
                        ctrScore += 0
                        
                if value == "cpc":
                    field_mean = mean(cpc_history)
                    standard_deviation = pstdev(cpc_history)
                    if (float(keys[value]) > float(field_mean + standard_deviation*2)):
                        cpcScore += 1
                    elif (float(keys[value]) > float(field_mean + standard_deviation)):
                        cpcScore += 0.75
                    elif (float(keys[value]) > float(field_mean - standard_deviation) and float(keys[value]) < float(field_mean + standard_deviation)):
                        cpcScore += 0.5
                    elif (float(keys[value]) < float(field_mean - standard_deviation)):
                        cpcScore += 0.25
                    elif (float(keys[value]) < float(field_mean - standard_deviation*2)):
                        cpcScore += 0
                    
                        
                if value == 'clicks':
                    field_mean = mean(click_history)
                    standard_deviation = pstdev(click_history)
                    if (float(keys[value]) > float(field_mean + standard_deviation*2)):
                        clickScore += 1
                    elif (float(keys[value]) > float(field_mean + standard_deviation)):
                        clickScore += 0.75
                    elif (float(keys[value]) > float(field_mean - standard_deviation) and float(keys[value]) < float(field_mean + standard_deviation)):
                        clickScore += 0.5
                    elif (float(keys[value]) < float(field_mean - standard_deviation)):
                        clickScore += 0.25
                    elif (float(keys[value]) < float(field_mean - standard_deviation*2)):
                        clickScore += 0
                    
                        
                if value == "frequency":
                    field_mean = mean(frequency_history)
                    standard_deviation = pstdev(frequency_history)
                    if (float(keys[value]) > float(field_mean + standard_deviation*2)):
                        frequencyScore += 1
                    if (float(keys[value]) > float(field_mean + standard_deviation)):
                        frequencyScore += 0.75
                    elif (float(keys[value]) > float(field_mean - standard_deviation) and float(keys[value]) < float(field_mean + standard_deviation)):
                        frequencyScore += 0.5
                    elif (float(keys[value]) < float(field_mean - standard_deviation)):
                        frequencyScore += 0.25
                    elif (float(keys[value]) < float(field_mean - standard_deviation*2)):
                        frequencyScore += 0
                    
                        
                if value == "cpm":
                    field_mean = mean(cpm_history)
                    standard_deviation = pstdev(cpm_history)
                    if (float(keys[value]) > float(field_mean + standard_deviation*2)):
                        cpmScore += 1
                    elif (float(keys[value]) > float(field_mean + standard_deviation)):
                        cpmScore += 0.75
                    elif (float(keys[value]) > float(field_mean - standard_deviation) and float(keys[value]) < float(field_mean + standard_deviation)):
                        cpmScore += 0.5
                    elif (float(keys[value]) < float(field_mean - standard_deviation)):
                        cpmScore += 0.25
                    elif (float(keys[value]) < float(field_mean - standard_deviation*2)):
                        cpmScore += 0
                    
                        
                if value == "impressions":
                    field_mean = mean(impressions_history)
                    standard_deviation = pstdev(impressions_history)
                    if (float(keys[value]) > float(field_mean + standard_deviation*2)):
                        impressionsScore += 1
                    elif (float(keys[value]) > float(field_mean + standard_deviation)):
                        impressionsScore += 0.75
                    elif (float(keys[value]) > float(field_mean - standard_deviation) and float(keys[value]) < float(field_mean + standard_deviation)):
                        impressionsScore += 0.5
                    elif (float(keys[value]) < float(field_mean - standard_deviation)):
                        impressionsScore += 0.25
                    elif (float(keys[value]) < float(field_mean - standard_deviation*2)):
                        impressionsScore += 0
                    
                        
                if value == "reach":
                    field_mean = mean(reach_history)
                    standard_deviation = pstdev(reach_history)
                    if (float(keys[value]) > float(field_mean + standard_deviation*2)):
                        reachScore += 1
                    elif (float(keys[value]) > float(field_mean + standard_deviation)):
                        reachScore += 0.75
                    elif (float(keys[value]) > float(field_mean - standard_deviation) and float(keys[value]) < float(field_mean + standard_deviation)):
                        reachScore += 0.5
                    elif (float(keys[value]) < float(field_mean - standard_deviation)):
                        reachScore += 0.25
                    elif (float(keys[value]) < float(field_mean - standard_deviation*2)):
                        reachScore += 0
                    
                
                    
            
        
    """Score * (Weight) determines how much influence a specific field has on the algorithm.
    Score = a we come up with based on the data
    Weight = how important we think that field is in making a decision (out of 1)
    numberOfFields = the number of fields that will give us a number between 0 and 1 when divided
    """
    
    
    

    #print "ctrScore: " + str(ctrScore)
    #print "ctrScore:" + str(cpcScore)
    #print "clickScore: " + str(clickScore)
    #print "frequencyScore: " + str(frequencyScore)
    #print "cpmScore: " + str(cpmScore)
    #print "impressionsScore: " + str(impressionsScore)
    #print "reachScore: " + str(reachScore)
    
    
    finalAlgorithm = (ctrScore*(1) 
                      + cpcScore*(1) 
                      + clickScore*(1) 
                      + frequencyScore*(1) 
                      + cpmScore*(1) 
                      + impressionsScore*(1) 
                      + reachScore*(1)
                      )/ float(numberOfFields)
    
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
    db_account_ids = CTCDatabase.getListOfAccountIDs()
    curr_date = time.strftime("%Y-%m-%d")
    

    for acc_name, acc_id in FacebookAdAccounts.items(): #iterate through all account names, ids
        acc_campaign_id = FacebookConnection.get_prospecting_campaign_id(acc_id) #Grab the prospecting campaign id

        if acc_id not in db_account_ids: #Case when we have a new account id being added to the database.
            campaign_stats = FacebookConnection.get_campaign_stats(acc_campaign_id) #Get all the necessary data points required to calculate score
            CTCDatabase.insertCampaignData(campaign_stats, acc_id)
        else: #Case where we only want to grab and insert to the db todays values
            campaign_stats = FacebookConnection.get_current_date_stats(acc_campaign_id, curr_date)
            CTCDatabase.insertCampaignData(campaign_stats, acc_id)

        #Grab all the historical values and todays values
        campaign_data_set = CTCDatabase.getCampaignData(acc_id, curr_date)
        curr_date_values = CTCDatabase.getCurrentDateValues(acc_id, curr_date)
     
            
        ctc_score = calculate_ctc_score(campaign_data_set, curr_date_values)

if __name__ == '__main__':
    main()
