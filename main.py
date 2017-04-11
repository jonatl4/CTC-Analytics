from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adset import AdSet

#Global variable for API Access 
my_app_id = '199864797164834'
my_app_secret = 'c793d8993eca253282938ce1e48a6bbd'
my_access_token = 'EAAC1xqY89SIBAEvs4ycf8tK3AUH3ZBNEs6ZBDDsfyBlu7jGBPfVf96xqBJ3VVE3VdihZAonHnzvu19ZC3TzsfV3ES6CLJ5bh6XZCGwXcmu2etypGsK7xiyH1wZBEZAFggyspSdfw7QNYLmew6sUBoORkfPZAuOEpasEZD'


def get_accounts():
    """Retrieves and displays a list of the user's ad accounts."""
    me = objects.AdUser(fbid='me')
    my_accounts = list(me.get_ad_accounts(fields=[
                'id',
                'name',
                'timezone_name',
                'amount_spent',
                'currency']))
    print my_accounts




























def main():
    FacebookAPI = FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    #print FacebookAPI
    get_accounts()






if __name__ == '__main__':
    main()
