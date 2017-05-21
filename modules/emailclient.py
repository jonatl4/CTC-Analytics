import time
import smtplib
import datetime
import io
from shutil import copyfile
import os
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import win32com.client as win32

class Email:
    def __init__(self, values, ctc_scores, percentage_change):
        self.values = values #contain all the raw values
        self.ctc_scores = ctc_scores #contain all the values after standard deviation calculation
        self.percentage_change = percentage_change #contain all the values of percentage change between todays and yesterdays values

        #Merge dictionaries together to make it easier to iterate through the data
        self.tableData = dict(self.values)
        self.tableData.update(self.ctc_scores)
        self.tableData.update(self.percentage_change)

        self.EXCEL = win32.DispatchEx('Excel.Application')
        self.EXCEL.Visible = True
        self.date = datetime.date.today()
        self.templateFolder = os.path.join(os.getcwd(), 'template')
        self.exportFolder = os.path.join(os.getcwd(), 'sent')
        self.emailExport = os.path.join(self.exportFolder, self.values['account_name'])
        if not os.path.exists(self.emailExport):
            os.makedirs(self.emailExport)

        #Make a new copy of the email template
        self.copyEmail()
        self.exportPNG()
        self.replaceTerms()
        self.createEmail()
        self.sendEmail()


    def exportPNG(self):
        "Opens the excel workbook template and based on the value selects a certain worksheet (for color coding) and replaces the row with the ctc value"
        self.WB = self.EXCEL.Workbooks.Open(os.path.join(self.templateFolder, 'charts.xlsx'))
        ws_name = None

        ctc_final_score = round(self.tableData['ctc_final_score'], 2)
        if ctc_final_score >= 0.70:
            ws = self.WB.Worksheets("high")
            ws_name = "high"
        elif ctc_final_score <= 0.69 and ctc_final_score >= 0.50:
            ws = self.WB.Worksheets("medium")
            ws_name = "medium"
        elif ctc_final_score  <= 0.49:
            ws = self.WB.Worksheets("low")
            ws_name = "low"

        ws_range = ws.Range("A:B")
        ws_range.Offset(2,2).value = ctc_final_score
        self.imageExport(ws_name, "chart")
        self.WB.Save()
        self.EXCEL.Quit()
        return

    def imageExport(self, ws, filename):
        "Formats the data label to be in the right position and exports the chart into a png file"
        wb_path = self.EXCEL.ActiveWorkbook.Path + "\\"
        sheet = self.EXCEL.Sheets(ws)

        for i in range(1, sheet.ChartObjects().Count + 1):
            chart = sheet.ChartObjects(i).Activate()
            dlabels = self.EXCEL.ActiveChart.SeriesCollection(1)
            dlabels.HasLeaderLines = False
            for i in range(1, dlabels.Points().Count):
                labelcheck = dlabels.Points(i)
                if labelcheck.HasDataLabel:
                    label = labelcheck.DataLabel
                    label.Left = 240.218
                    label.Top = 210.987

        for i in range(1, sheet.ChartObjects().Count + 1):
            sheet.ChartObjects(i).Activate()
            fpath = self.emailExport + '\\' + filename + ".png"
            self.EXCEL.ActiveChart.Export(Filename=fpath)
        return

    def copyEmail(self):
        "Copies the template html file that is stored in the templates/report folder and creates a new html file in the template/export folder. You will need some sort of naming convention for new html files so maybe like {account_name}_{todays_date}.html"
        self.src_path = os.path.join(os.getcwd(), 'template\CTCEmail.txt')
        self.dst_path = os.path.join(self.emailExport, self.values['account_name'] + '_' + str(self.date) + '.txt')
        copyfile(self.src_path, self.dst_path)
        return

    def replaceTerms(self):
        "Reads the html file and looks for specific terms and replaces it with the appropriate value"
        self.file_read = open(self.dst_path, "r").read()
        for k,j in self.tableData.items():
            self.file_read = self.file_read.replace(k, str(j))
        
    def createEmail(self):
        "Create the email template to send to the client"
        mstRoot = MIMEMultipart('related')
        self.MESSAGE = MIMEMultipart('alternative')
        self.MESSAGE['subject'] = "CTC-Analytics: " + str(self.tableData['account_name']) + ' - ' + str(self.date)
        self.MESSAGE['To'] = 'wyassine@uci.edu'
        self.MESSAGE['From'] = 'analytics@commonthreatco.com'
        self.MESSAGE.preamble = """Here's an update on your ads' performance!"""
        HTML_BODY = MIMEText(self.file_read, 'html')
        self.MESSAGE.attach(HTML_BODY)
        img_data = open(os.path.join(self.emailExport, 'chart.png'),'rb').read()
        img = MIMEImage(img_data, 'png')
        img.add_header('Content-ID','<chart.png>')
        img.add_header('Content-Disposition', 'inline', filename='chart.png')
        self.MESSAGE.attach(img)
        return

    def sendEmail(self):
        "send the email to the client"
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.server.starttls()
        self.server.login("analytics@commonthreadco.com","C0mm0nthr3@d")
        self.server.sendmail("wyassine@uci.edu", ["wyassine@uci.edu"], self.MESSAGE.as_string())
        self.server.quit()
        return
