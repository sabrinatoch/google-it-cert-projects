#!/usr/bin/env python3

import requests
import os, glob

url = "http://localhost/upload"
for file in glob.glob("/supplier-data/images/*"):
    with open(file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})