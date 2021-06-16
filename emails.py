#!/usr/bin/env python3

 # emails.py

import os
import smtplib
from email.message import EmailMessage
import getpass


def generate_email():

  From = "automation@example.com"
  To =  getpass.getuser() + "@example.com"
  Subject = "Upload Completed - Online Fruit Store"
  Body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
  path = os.getcwd()
  Attachment = "/tmp/processed.pdf"

  msg = EmailMessage()
  
  msg['Subject'] = Subject
  msg['From'] = From
  msg['To'] = To
  msg.set_content(Body)
  s = path + Attachment
  with open(s, 'rb') as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype='application', subtype='pdf', filename='processed.pdf')

  return msg
  
def gen_mail_alert(Subject):
  From = "automation@example.com"
  To = getpass.getuser() + "@example.com"
  Body = "Please check your system and resolve the issue as soon as possible."

  msg = EmailMessage()
  msg['From'] = From
  msg['To'] = To
  msg['Subject'] = Subject
  msg.set_content(Body)
  
  return msg
  
def send_email(msg):
  # Send the message via our own SMTP server.
  s = smtplib.SMTP('localhost')
  s.send_message(msg)
  s.quit()

