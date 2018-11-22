#!/usr/bin/python3

import smtplib

sender = 'prasad@sl.local'
receivers = ['administrator@sl.local']

message = """From: Prasad Ragashetti <prasad.ragashetti@sl.local>
To: Administrator <Administrator@sl.local>
Subject: SMTP e-mail test

This is a File Difference Report.
"""


try:
   smtpObj = smtplib.SMTP('lonex201600.sl.local')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
