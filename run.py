#!/usr/bin/env python3

 # run.py

import os
import requests
import json

def file_json(file):
  f = open(file, "r")
  data_set={}
  data_set["name"] = f.readline()
  data_set["weight"] = int(f.readline().split(' ')[0])
  data_set["description"] = f.readline()
  data_set["image_name"] = os.path.basename(file)[:-3] + "jpeg"
  json_dump = json.dumps(data_set)
  f.close()
  return json_dump

url = "http://localhost//fruits/"
path = os. getcwd() + "/supplier-data/descriptions/"
headers={'Content-type':'application/json', 'Accept':'application/json'}

for root, dirs, files  in os.walk(path):
  for file in files:
    if ".txt" in file:
      json_data = file_json(path + file)
      with open(path + file, 'rb') as opened:
        r = requests.post(url, data= json_data, headers=headers)
        print(file + str(r))



