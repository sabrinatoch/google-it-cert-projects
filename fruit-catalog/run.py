#!/usr/bin/env python3

import os
import requests
import json

user = os.getenv('USER')
path = '/home/{}/supplier-data/descriptions/'.format(user)
url = "http://localhost/fruits/"
fruits = {}

for file in os.listdir(path):
    data = open(path + file)
    dataList = data.readlines()
    fruits["name"] = dataList[0].strip('\n')
    fruits["weight"] = int(dataList[1].strip('\n').strip('lbs'))
    fruits["description"] = dataList[2].strip('\n')
    fruits["image_name"] = file.strip('.txt')+'.jpeg'
    req = requests.post(url, json=fruits)
    data.close()