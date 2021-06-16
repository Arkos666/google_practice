#!/usr/bin/env python3

 # changeImage.py

from PIL import Image
import os

path = os. getcwd() + "/supplier-data/images/"

for root, dirs, files  in os.walk(path):

  for file in files:
    #print(os.path.join(root, name))
    if ".tiff" in file:
      img = Image.open(path + file)
      new_im = img.resize((600, 400)).convert("RGB").save(path + file[:-4] +"jpeg")

