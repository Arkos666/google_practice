#!/usr/bin/env python3

 # report_email.py

import reports
import os
import datetime
import emails


def process_data(file):
  f = open(file, "r")
  data_set={}
  data_set["name"] = "name: " + f.readline()
  data_set["weight"] = "weight: " + (f.readline().split(' ')[0]) + " lbs\n"
  data_set["description"] = f.readline().rstrip("\n")
  f.close()
  
  data = data_set["name"] + data_set["weight"] + "\n"
  return data
  
  
path = os. getcwd() + "/supplier-data/descriptions/"
data =  ""
for root, dirs, files  in os.walk(path):

  for file in files:
    if ".txt" in file:
      data = data + process_data(path + file)

#print (data)
attachment = os.getcwd() + "/tmp/processed.pdf"
title = "Processed Update on " + str(datetime.date.today().strftime("%B %d, %Y"))
paragraph = data
reports.generate_report(attachment, title, paragraph)
msg = emails.generate_email()
emails.send_email(msg)
