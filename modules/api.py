from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.campaign import Campaign

import datetime

#Global variable for API Access 
my_app_id = '199864797164834'
my_app_secret = 'c793d8993eca253282938ce1e48a6bbd'
my_access_token = 'EAAC1xqY89SIBANGlR56lthPzvV4jk0Gd0XwEZAsXYff0d6MQl1qd6FDS1yiOIFQ7ug7zhP6X1NdDU1ff3OvlqM49jSs5ZApFZBRmw5GPOahE53ikTCBwfWWhetohYiExJHORnxUFuZBTCsqkrl91f0mP2etXQoMZD'



class FacebookAPI:
    def __init__(self):
        FacebookAPI = FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

    def get_accounts(self):
        """Retrieves and displays a list of all user's ad accounts."""
        me = objects.AdUser(fbid="me")
        my_accounts = list(me.get_ad_accounts(fields=[
            'id',
            'name',
            'timezone_name',
            'amount_spent',
            'currency']))
        return my_accounts

    def get_prospecting_campaign_id(self, acc_id):
        """Takes in an account id and searches across the ad accounts campaigns looking for the campaign name Prospecting. If found, return the campaign id."""
        account = AdAccount(acc_id).get_campaigns()
        for camp in account:
            campaign =  Campaign(camp['id'])
            campaign.remote_read(fields=[
                Campaign.Field.name,
            ])
            if campaign['name'] == 'Prospecting':
                return camp['id']
    
    def get_campaign_stats(self,campaign_id):
        """Takes in a campaign id and returns all the required data points for the campaign"""
        campaign = Campaign(campaign_id)
        fields = ['account_name',
                  'campaign_name',
                  'clicks',
                  'cpc',
                  'reach',
                  'ctr',
                  'frequency',
                  'impressions',
                  'reach',
                  'cpm',
                  'relevance_score']
        date = datetime.datetime.strptime('2017-3-26', "%Y-%m-%d")
        time_diff = datetime.timedelta(days=25)
        new_date = date + time_diff
        print str(new_date).split()[0]
        insights = campaign.get_insights(fields=fields, params={ 'time_range':{'since':'2017-4-1', 'until':'2017-5-30'}, 'time_increment':1})
        #insights = campaign.get_insights(fields=fields, params={'date_preset':'lifetime', 'time_increment':1})
       # print insights
        return insights