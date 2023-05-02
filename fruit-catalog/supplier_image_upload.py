#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
user = os.getenv('USER')
path = '/home/{}/supplier-data/images/'.format(user)

for file in os.listdir(path):
    if 'jpeg' in file:
        full_path = path + file
        with open(full_path, 'rb') as op:
            req = requests.post(url, files={'file': op})