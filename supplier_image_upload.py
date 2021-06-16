#!/usr/bin/env python3

 # supplier_image_upload.py

import requests
import os


# This example shows how a file can be uploaded using
# The Python Requests module
url = "http://localhost/upload/"
path = os. getcwd() + "/supplier-data/images/"

for root, dirs, files  in os.walk(path):
  for file in files:
    if ".jpeg" in file:
      with open(path + file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
        print(file + str(r))
