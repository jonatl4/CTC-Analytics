from modules.api import FacebookAPI







def create_structure(facebook_ad_accounts):
    """Returns a dictionary of the ad accounts with the following format {AccountName1: AccountID1, AccountName2: AccountID2...}"""
    ad_account_ids = ['1647162208927124', '1656102788033066', '1699751017001576', '1379395989021046', '10100208564192664']
    ad_account = {}
    for acc in facebook_ad_accounts:
        acc_strip = acc['id'].strip('act_')
        if acc_strip in ad_account_ids:
            ad_account[acc['name']] = acc['id']

    return ad_account



def main():
    """The controller of the entire program. It will handle initializing the facebook API connection, and call various modules in the program to perform tasks such as 
        grabbing the facebook ad accounts, storing values in the database, generating the html document and sending the html document to a list of clients"""
    FacebookConnection = FacebookAPI()
    FacebookAdAccounts = create_structure(FacebookConnection.get_accounts())
    for acc_name, acc_id in FacebookAdAccounts.items():
        print acc_name
        #acc_campaign_id = FacebookConnection.get_prospecting_campaign_id(acc_id)





if __name__ == '__main__':
    main()
