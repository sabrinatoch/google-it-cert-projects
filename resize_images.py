#!/usr/bin/env python3
import glob
from PIL import Image

for file in glob.glob("ic_*"):
    im = Image.open(file).convert('RGB')
    im.rotate(270).resize((128,128)).save("/opt/icons/" + file, "JPEG")
