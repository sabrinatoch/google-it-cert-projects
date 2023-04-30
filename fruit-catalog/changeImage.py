#!/usr/bin/env python3
import os, glob
from PIL import Image

for file in glob.glob("/supplier-data/images/*"):
    im = Image.open(file).convert('RGB')
    im.resize((600,400)).save("/supplier-data/images/" + file, "JPEG")