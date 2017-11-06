import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import json

sys.path.append('somepath') #input correct config file path

with open('secretsantaconfig.json') as json_data_file:
    data = json.load(json_data_file)
	
kidList = data['other']['kidList']
spouseDict = data['spouseDict']
emailDict = data['emailDict']
gmail_user = data['gmailconfig']['gmail_user']
gmail_password = data['gmailconfig']['gmail_password']

def genSecretSanta(nkidList,nspouseDict):
    santaList=[]
    santaDict={}
    for each in kidList:
        eachList = [kid for kid in nkidList if kid != each and kid not in santaList and kid != nspouseDict[each]]
        if eachList == []:
            kid = each
        else:
            kid = np.random.choice(eachList,replace='False')
        santaList.append(kid)
        santaDict[each]=kid
        
    return santaDict

santaDict = genSecretSanta(kidList,spouseDict)

FROM = gmail_user
SUBJECT = "Secret Santa Test"

for i in range(len(emailDict.keys())):
    TO = emailDict[emailDict.keys()[i]]
    BODY = '%s %s, your Secret Santa Gift Recipient is:  %s' %(emailDict.keys()[i],emailDict[emailDict.keys()[i]],santaDict[emailDict.keys()[i]])

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = TO
    
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(BODY, 'text')
    msg.attach(part1)
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(FROM, TO, msg.as_string())
        server.close()

        print 'Email sent!'
    except:  
        print 'Something went wrong...'