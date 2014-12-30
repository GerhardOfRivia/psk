#!/usr/bin/python
#This will email the IP adress.

import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime

# Account information
to = 'EMAIL'
from_user = 'EMAIL'

smtpserver = smtplib.SMTP('smtp.EMAIL', 25)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
today = datetime.date.today()

# Very Linux Specific
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
my_ip = 'Your ip is %s' %  ipaddr
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For Device on %s' % today.strftime('%b %d %Y')
msg['From'] = from_user
msg['To'] = to
smtpserver.sendmail(from_user, [to], msg.as_string())
smtpserver.quit()
