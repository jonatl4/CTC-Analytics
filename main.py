from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adsinsights import AdsInsights

import datetime

#Global variable for API Access 
my_app_id = '199864797164834'
my_app_secret = 'c793d8993eca253282938ce1e48a6bbd'
my_access_token = 'EAAC1xqY89SIBANGlR56lthPzvV4jk0Gd0XwEZAsXYff0d6MQl1qd6FDS1yiOIFQ7ug7zhP6X1NdDU1ff3OvlqM49jSs5ZApFZBRmw5GPOahE53ikTCBwfWWhetohYiExJHORnxUFuZBTCsqkrl91f0mP2etXQoMZD'
    
def get_ad_insights():
    
    ### Set up user and read obj from server
    me = objects.AdUser(fbid='me')
    my_accounts = me.get_ad_accounts(fields=[
                'id',
                'name'])

    ### Iterate through all ad accounts
    for account in my_accounts:
        print(account)
        
        for ad in account.get_ad_sets():
            
            ### Set the period of time (Default = 1 week)
            today = datetime.date.today()
            start_time = str(today - datetime.timedelta(weeks=40))
            end_time = str(today)
            fields = ['account_name',
                      'ad_name',
                      'adset_name',
                      'campaign_name',
                      'clicks',
                      'cpc',
                      'ctr',
                      'frequency',
                      'impressions',
                      'reach',
                      'cpm',
                      'relevance_score']
            
            params = {
                'time_range': {
                    'since': start_time,
                    'until': end_time,
                },
                'level': AdsInsights.Level.ad

            }
            
            insights = ad.get_insights(fields = fields, params = params)
            print(insights)




def main():
    FacebookAPI = FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    #print FacebookAPI
    get_ad_insights()





if __name__ == '__main__':
    main()