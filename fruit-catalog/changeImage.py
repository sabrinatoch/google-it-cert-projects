#!/usr/bin/env python3
import os, sys
from PIL import Image

user = os.getenv('USER')
path = '/home/{}/supplier-data/images/'.format(user)

for file in os.listdir(path):
    if 'tiff' in file:
        full_path = path + file
        new_path = '{}/jpeg'.format(os.path.splitext(full_path))
        im = Image.open(full_path).convert('RGB')
        im.resize((600,400)).save(new_path, "JPEG")