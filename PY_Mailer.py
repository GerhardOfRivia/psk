#!/usr/bin/python3
import subprocess
import smtplib
import sys

sender = 'EMAIL'
receivers = ['EMAIL']

try:
    host_output=subprocess.check_output(["/bin/hostname", "-I"])
except:
    print ("No hostname command runnable from path")
    print (sys.exc_info()[0])
    sys.exit()


message = """From: From EMAIL <EMAIL>
To: To EMAIL <EMAIL>
Subject:
IP: """+host_output.decode()


try:
   smtpObj = smtplib.SMTP('smtp.EMAIL')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except smtplib.SMTPException:
   print ("Error: unable to send email")
