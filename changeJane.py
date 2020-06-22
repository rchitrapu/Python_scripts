#!/usr/bin/env python3

import sys
import subprocess

filelist = []
with open(sys.argv[1],'r') as  file:
  filelist = file.readlines()
  for line in filelist:
    oldfilename = line.strip()
    newfilename = oldfilename.replace("jane","jdoe")
    subprocess.run(['mv', oldfilename, newfilename])
  file.close() 
  
