#!/usr/bin/env python3

import os
import requests

path = '/data/feedback/'
url = 'http://34:31:61:220/feedback/'
txt_files = os.listdir(path)

for txt in txt_files:
    with open(path + txt) as file:
        lines = file.read().split('\n')
        feedback = {
            "title":lines[0], 
            "name":lines[1], 
            "date":lines[2], 
            "feedback":lines[3]
        }
        response = requests.post(url, json=feedback)

print(response.status_code)
