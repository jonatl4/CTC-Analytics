from modules.api import FacebookAPI
from modules.db import Database
from modules.emailclient import Email
from modules.algstats import pstdev, mean
import time
from datetime import date, timedelta



def calculate_ctc_score(campaign_data_set, curr_date_values):
    #campaign_data_set is going to be a set of dictionaries nested in to a list. It is going to have all the campaigns data
    #except for today. See bellow on how to grab the values out.
    calculation_return = {}
    
    ctrScore, cpcScore, clickScore, frequencyScore, cpmScore, impressionsScore, reachScore = 0, 0, 0, 0, 0, 0, 0 
    ctr_history, cpc_history, click_history, frequency_history, cpm_history, impressions_history, reach_history = [], [], [], [], [], [], []
    numberOfFields = 7
    
  
    for datum in campaign_data_set:
        ctr_history.append(datum['ctr_value'])
        cpc_history.append(datum['cpc_value'])
        click_history.append(datum['clicks_value'])
        frequency_history.append(datum['frequency_value'])
        cpm_history.append(datum['cpm_value'])
        impressions_history.append(datum['impressions_value'])
        reach_history.append(datum['reach_value'])
    
    field_mean = mean(ctr_history)
    standard_deviation = pstdev(ctr_history)
    
    if (curr_date_values['ctr_value'] > (field_mean + standard_deviation*2)):
        ctrScore += 1
    if (curr_date_values['ctr_value'] > (field_mean + standard_deviation)):
        ctrScore += 0.75
    elif (curr_date_values['ctr_value'] > (field_mean - standard_deviation) and curr_date_values['ctr_value'] < (field_mean + standard_deviation)):
        ctrScore += 0.5
    elif (curr_date_values['ctr_value'] < (field_mean - standard_deviation)):
        ctrScore += 0.25
    elif (curr_date_values['ctr_value'] < (field_mean - standard_deviation*2)):
        ctrScore += 0
    
    field_mean = mean(cpc_history)
    standard_deviation = pstdev(cpc_history)
    if (curr_date_values['cpc_value'] > (field_mean + standard_deviation*2)):
        cpcScore += 1
    elif (curr_date_values['cpc_value'] > (field_mean + standard_deviation)):
        cpcScore += 0.75
    elif (curr_date_values['cpc_value'] > (field_mean - standard_deviation) and curr_date_values['cpc_value'] < (field_mean + standard_deviation)):
        cpcScore += 0.5
    elif (curr_date_values['cpc_value'] < (field_mean - standard_deviation)):
        cpcScore += 0.25
    elif (curr_date_values['cpc_value'] < (field_mean - standard_deviation*2)):
        cpcScore += 0
    
    field_mean = mean(click_history)
    standard_deviation = pstdev(click_history)
    if (curr_date_values['clicks_value'] > (field_mean + standard_deviation*2)):
        clickScore += 1
    elif (curr_date_values['clicks_value'] > (field_mean + standard_deviation)):
        clickScore += 0.75
    elif (curr_date_values['clicks_value'] > (field_mean - standard_deviation) and curr_date_values['clicks_value'] < (field_mean + standard_deviation)):
        clickScore += 0.5
    elif (curr_date_values['clicks_value'] < (field_mean - standard_deviation)):
        clickScore += 0.25
    elif (curr_date_values['clicks_value'] < (field_mean - standard_deviation*2)):
        clickScore += 0
    
    field_mean = mean(frequency_history)
    standard_deviation = pstdev(frequency_history)
    if (curr_date_values['frequency_value'] > (field_mean + standard_deviation*2)):
        frequencyScore += 1
    if (curr_date_values['frequency_value'] > (field_mean + standard_deviation)):
        frequencyScore += 0.75
    elif (curr_date_values['frequency_value'] > (field_mean - standard_deviation) and curr_date_values['frequency_value'] < (field_mean + standard_deviation)):
        frequencyScore += 0.5
    elif (curr_date_values['frequency_value'] < (field_mean - standard_deviation)):
        frequencyScore += 0.25
    elif (curr_date_values['frequency_value'] < (field_mean - standard_deviation*2)):
        frequencyScore += 0
    
    field_mean = mean(cpm_history)
    standard_deviation = pstdev(cpm_history)
    if (curr_date_values['cpm_value'] > (field_mean + standard_deviation*2)):
        cpmScore += 1
    elif (curr_date_values['cpm_value'] > (field_mean + standard_deviation)):
        cpmScore += 0.75
    elif (curr_date_values['cpm_value'] > (field_mean - standard_deviation) and curr_date_values['cpm_value'] < (field_mean + standard_deviation)):
        cpmScore += 0.5
    elif (curr_date_values['cpm_value'] < (field_mean - standard_deviation)):
        cpmScore += 0.25
    elif (curr_date_values['cpm_value'] < (field_mean - standard_deviation*2)):
        cpmScore += 0
    
    field_mean = mean(impressions_history)
    standard_deviation = pstdev(impressions_history)
    if (curr_date_values['impressions_value'] > (field_mean + standard_deviation*2)):
        impressionsScore += 1
    elif (curr_date_values['impressions_value'] > (field_mean + standard_deviation)):
        impressionsScore += 0.75
    elif (curr_date_values['impressions_value'] > (field_mean - standard_deviation) and curr_date_values['impressions_value'] < (field_mean + standard_deviation)):
        impressionsScore += 0.5
    elif (curr_date_values['impressions_value'] < (field_mean - standard_deviation)):
        impressionsScore += 0.25
    elif (curr_date_values['impressions_value'] < (field_mean - standard_deviation*2)):
        impressionsScore += 0   
               
    field_mean = mean(reach_history)
    standard_deviation = pstdev(reach_history)
    if (curr_date_values['reach_value'] > (field_mean + standard_deviation*2)):
        reachScore += 1
    elif (curr_date_values['reach_value'] > (field_mean + standard_deviation)):
        reachScore += 0.75
    elif (curr_date_values['reach_value'] > (field_mean - standard_deviation) and curr_date_values['reach_value'] < (field_mean + standard_deviation)):
        reachScore += 0.5
    elif (curr_date_values['reach_value'] < (field_mean - standard_deviation)):
        reachScore += 0.25
    elif (curr_date_values['reach_value'] < (field_mean - standard_deviation*2)):
        reachScore += 0
     

    """Score * (Weight) determines how much influence a specific field has on the algorithm.
    Score = a we come up with based on the data
    Weight = how important we think that field is in making a decision (out of 1)
    numberOfFields = the number of fields that will give us a number between 0 and 1 when divided
    """
#     print "ctrScore: " + str(ctrScore)
#     print "ctrScore:" + str(cpcScore)
#     print "clickScore: " + str(clickScore)
#     print "frequencyScore: " + str(frequencyScore)
#     print "cpmScore: " + str(cpmScore)
#     print "impressionsScore: " + str(impressionsScore)
#     print "reachScore: " + str(reachScore)
    
    finalAlgorithm = (ctrScore*(1) 
                      + cpcScore*(1) 
                      + clickScore*(1) 
                      + frequencyScore*(1) 
                      + cpmScore*(1) 
                      + impressionsScore*(1) 
                      + reachScore*(1)
                      )/ float(numberOfFields)
    
    #print('CTC SCORE: {}'.format(finalAlgorithm))
    
    #Append all the data to a dictionary to then add to the database
    calculation_return['ctc_final_score'] = finalAlgorithm
    calculation_return['ctr_score'] = ctrScore
    calculation_return['cpc_score'] = cpcScore
    calculation_return['click_score'] = clickScore
    calculation_return['frequency_score'] = frequencyScore
    calculation_return['cpm_score'] = cpmScore
    calculation_return['impression_score'] = impressionsScore
    calculation_return['reach_score'] = reachScore

    return calculation_return



def create_structure(facebook_ad_accounts):
    """Returns a dictionary of the ad accounts with the following format {AccountName1: AccountID1, AccountName2: AccountID2...}"""
    ad_account_ids = ['1699751017001576'] #Axe Bat Account ID
    ad_account = {}
    for acc in facebook_ad_accounts:
        acc_strip = acc['id'].strip('act_')
        if acc_strip in ad_account_ids:
            ad_account[acc['name']] = acc['id']

    return ad_account


def calculate_percentage_change(curr_values, second_values):
    perc_change = {}
    perc_change['ctr_change'] = round(((curr_values['ctr_value'] - second_values['ctr_value'])/second_values['ctr_value']) * 100,2)
    perc_change['cpc_change'] = round(((curr_values['cpc_value'] - second_values['cpc_value'])/second_values['cpc_value']) * 100, 2)
    perc_change['click_change'] = round((float(curr_values['clicks_value']) - float(second_values['clicks_value']))/float(second_values['clicks_value']) * 100, 2)
    perc_change['frequency_change'] = round(((curr_values['frequency_value'] - second_values['frequency_value'])/second_values['frequency_value']) * 100, 2)
    perc_change['cpm_change'] = round(((curr_values['cpm_value'] - second_values['cpm_value'])/second_values['cpm_value']) * 100, 2)
    perc_change['impression_change'] = round(((curr_values['impressions_value'] - second_values['impressions_value'])/second_values['impressions_value']) * 100, 2)
    perc_change['reach_change'] = round((float(curr_values['reach_value']) - float(second_values['reach_value']))/float(second_values['reach_value']) * 100, 2)
    return perc_change

def main():
    """The controller of the entire program. It will handle initializing the facebook API connection, and call various modules in the program to perform tasks such as 
        grabbing the facebook ad accounts, storing values in the database, generating the html document and sending the html document to a list of clients"""
    FacebookConnection = FacebookAPI() # Create the facebook api object
    FacebookAdAccounts = create_structure(FacebookConnection.get_accounts()) #dictionary of account name, id
    CTCDatabase = Database()
    db_account_ids = CTCDatabase.getListOfAccountIDs()
    curr_date = time.strftime("%Y-%m-%d")
    yesterday = (date.today() - timedelta(1)).strftime("%Y-%m-%d") 

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
        yesterday_values = CTCDatabase.getCurrentDateValues(acc_id, yesterday)
        ctc_score = calculate_ctc_score(campaign_data_set, curr_date_values)
        check_past = CTCDatabase.checkForPastScore(acc_id, yesterday)

        if check_past == True: #This if statement is meant for brand new clients. We need to do a comparision from yesterdays date.
            yesterday_campaign_values = CTCDatabase.getCampaignData(acc_id, yesterday)
            yesterday_ctc_score = calculate_ctc_score(campaign_data_set, curr_date_values)
            CTCDatabase.insertScores(yesterday_ctc_score, curr_date_values['account_name'], curr_date_values['account_id'], yesterday)
        
        percentage_change = calculate_percentage_change(curr_date_values, yesterday_values) #calculate percentage change between todays and yesterdays values
        CTCDatabase.insertScores(ctc_score, curr_date_values['account_name'], curr_date_values['account_id'], curr_date)
        CTCDatabase.insertPerChange(percentage_change, curr_date_values['account_name'], curr_date_values['account_id'], curr_date)

        #The rest of the code will be dedicated to email creation
        print "Sending email for account: " + str(acc_name)
        email = Email(curr_date_values, ctc_score, percentage_change)



if __name__ == '__main__':
    main()
