from modules.api import FacebookAPI




def calculate_ctc_score(campaign_stats):
    """Returns a ctc score from a given campaign"""
    print campaign_stats
    return


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
    for acc_name, acc_id in FacebookAdAccounts.items(): #iterate through all account names, ids
        acc_campaign_id = FacebookConnection.get_prospecting_campaign_id(acc_id) #Grab the prospecting campaign id
        campaign_stats = FacebookConnection.get_campaign_stats(acc_campaign_id) #Get all the necessary data points required to calculate score
        ctc_score = calculate_ctc_score(campaign_stats)




if __name__ == '__main__':
    main()
