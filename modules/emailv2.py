

class Email:
    def __init__(self, values, ctc_scores, percentage_change):
        self.values = values #contain all the raw values
        self.ctc_scores = ctc_scores #contain all the values after standard deviation calculation
        self.percentage_change = percentage_change #contain all the values of percentage change between todays and yesterdays values

        print self.values
        print self.ctc_scores
        print self.percentage_change
    
    def copyEmail(self):
        "Copies the template html file that is stored in the templates/report folder and creates a new html file in the template/export folder. You will need some sort of naming convention for new html files so maybe like {account_name}_{todays_date}.html"
        pass

    def replaceTerms(self):
        "Reads the html file and looks for specific terms and replaces it with the appropriate value"
        pass

    def sendEmail(self):
        "Once done replacing the terms, send the email to client"
        pass