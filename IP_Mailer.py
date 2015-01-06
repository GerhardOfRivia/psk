#!/usr/bin/python3
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
ipaddr = socket.gethostbyname(socket.gethostname())
my_ip = 'Your ip is %s' %  ipaddr
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For Device on %s' % today.strftime('%b %d %Y')
msg['From'] = from_user
msg['To'] = to
smtpserver.sendmail(from_user, [to], msg.as_string())
smtpserver.quit()
