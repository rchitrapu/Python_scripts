#!/usr/bin/env python3
import os, sys
from PIL import Image

def convertimage(infile):
  # converts the input file to JPEG format after rotation and resizing
  # saves the converted image in /opt/icons
  # removes the .jpg extension
  f, e = os.path.splitext(infile)
  outfile = "/opt/icons/" + f + ".jpg"
  savename = "/opt/icons/" + f
  if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.rotate(270).resize((128,128)).convert("RGB").save(outfile)
                os.rename(outfile,savename)
        except IOError:
            print("cannot convert", infile)
def main():
  directory = os.getcwd()
  for filename in os.listdir(directory):
    convertimage(filename)

if __name__ == "__main__":
    main()
    



