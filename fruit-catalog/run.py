#!/usr/bin/env python3

import os, glob
import requests

url = "http://localhost/fruits"
for file in glob.glob('/supplier-data/descriptions/*'):
    data = open(file)
    dataList = data.read().split('\n')
    w = dataList[1]
    intweight = int(w[0:w.index(" ")])


    dict = {
        "name":dataList[0],
        "weight":intweight,
        "description":dataList[2],
        "image_name":dataList[3]
    }

    response = requests.post(url, json=dict)
    data.close()