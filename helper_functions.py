import pandas as pd
import smtplib
from email.message import EmailMessage

def tableBuilder(data):
    array = []
    columns = ['Date', 'Account', 'Transaction Name', 'Category', 'Amount']
    for trans in range(len(data)):
        date_working = data[trans]['ColData'][0]['value']
        account = data[trans]['ColData'][6]['value']
        trans_name = data[trans]['ColData'][5]['value']
        category = data[trans]['ColData'][7]['value']
        amount = data[trans]['ColData'][8]['value']
        array.append([date_working, account, trans_name, category, amount])
    df = pd.DataFrame(array, columns=columns)
    return df
  
def send_email():
    email_address = "blob.automation.team@gmail.com"
    email_password: "qlbgsjfejjigjwkj"
    msg = EmailMessage()
    msg['Subject'] = "Test"
    msg['From'] = email_address
    msg['To'] = "brandonlz2017@gmail.com"
    msg.set_content("Testing! Please work.")
    with smtplib.SMTP_SSL("smtp.gmail.com", 587) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

send_email()
