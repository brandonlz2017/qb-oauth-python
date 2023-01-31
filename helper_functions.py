import pandas as pd
import smtplib
import yagmail

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

def transCat(value):
    transTable = pd.read_csv('trans_desc_key.csv')
    transDict = dict(zip(transTable['Key'].values, transTable['Value'].values))
    for key in transDict:
        if key in value:
            return transDict[key]

def send_email_attach(recipient, sender, app_key, attachment_name):
    yag = yagmail.SMTP(user=sender, password=app_key)
    yag.send(to=recipient, subject="Test with attachment", contents="Please see attached.", attachments=attachment_name)
    print('email sent')


