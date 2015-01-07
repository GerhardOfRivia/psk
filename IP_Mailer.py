#!/usr/bin/python
#This will email the IP.

import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import fcntl
import struct

# Account information
to = 'EMAIL'
from_user = 'EMAIL'

smtpserver = smtplib.SMTP('smtp.EMAIL', 25)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
today = datetime.date.today()

# Get IP
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

print get_ip_address('INTERFACE')
ipaddr = get_ip_address('INTERFACE')

# Very Linux Specific
my_ip = 'Your ip is %s' %  ipaddr
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For Device on %s' % today.strftime('%b %d %Y')
msg['From'] = from_user
msg['To'] = to
smtpserver.sendmail(from_user, [to], msg.as_string())
smtpserver.quit()
