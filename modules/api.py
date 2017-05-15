from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adsinsights import AdsInsights

from collections import defaultdict
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
                  'cpm',
                  'relevance_score']
        #Need to create a new list for data
        data = []
    
        #Grab lifetime campaign stats to find start and end date of campaign and convert to datetime formate
        insights = campaign.get_insights(fields=fields, params={'date_preset':'lifetime'})
        date_begin = datetime.datetime.strptime(insights[0]['date_start'], "%Y-%m-%d")
        date_end = datetime.datetime.strptime(insights[0]['date_stop'], "%Y-%m-%d")
        date_diff = datetime.timedelta(days=25)
        new_date = date_begin + date_diff

        #Pass in these values to the api
        api_date_first = str(date_begin).split()[0]
        api_date_last = str(new_date).split()[0]

        #Strange API limitation where you can only grab 25 values at a time. 
        while date_begin < date_end:
            insights = campaign.get_insights(fields=fields, params={ 'time_range':{'since':api_date_first, 'until':api_date_last}, 'time_increment':1})
            insights = list(insights)
            date_begin = new_date 
            new_date = date_begin + date_diff
            api_date_first = api_date_last
            api_date_last = str(new_date).split()[0]
            data += insights

        return data
    
    def get_current_date_stats(self, campaign_id, curr_date):
        """Takes in a campaign id and returns all the required data for the current date"""
        campaign = Campaign(campaign_id)
        fields = ['account_name',
                  'campaign_name',
                  'clicks',
                  'cpc',
                  'reach',
                  'ctr',
                  'frequency',
                  'impressions',
                  'cpm',
                  'relevance_score']

        insights = campaign.get_insights(fields=fields, params={ 'time_range':{'since':curr_date, 'until':curr_date}, 'time_increment':1})
        return insights
