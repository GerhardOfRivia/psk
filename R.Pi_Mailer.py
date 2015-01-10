#!/usr/bin/python
#This will email the IP for a Raspberry Pi.

import datetime
import subprocess
import smtplib
import sys

# Account information
to = 'EMAIL'
from_user = 'EMAIL'

smtpserver = smtplib.SMTP('smtp.EMAIL', 25)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
today = datetime.date.today()

# Get IP
try:
    ipaddr=subprocess.check_output(["hostname", "-I"])
except:
    print ("No hostname command runnable from path")
    print (sys.exc_info()[0])
    sys.exit()

# Linux Specific
try:
    my_ip = 'Your ip is %s' % ipaddr
    msg = MIMEText(my_ip)
    msg['Subject'] = 'IP For Device on %s' % today.strftime('%b %d %Y')
    msg['From'] = from_user
    msg['To'] = to
    smtpserver.sendmail(from_user, [to], msg.as_string())
    smtpserver.quit()
    print "Successfully sent email"
except SMTPException:
    print "Error: unable to send email"
