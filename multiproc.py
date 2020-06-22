#!/usr/bin/env python3
import sys, subprocess
import os, string
from multiprocessing import Pool

def back_up(subdir):
  # Do something with task here
  src = os.path.expanduser("~/scripts/") + subdir + "/"
  dest = os.path.expanduser("~/scripts_bkup/") + subdir + "/"
  subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":

  os.chdir(os.path.expanduser("~/scripts/"))
  path = '.'
  path = os.path.normpath(path)
  res = []
  for root,dirs,files in os.walk(path, topdown=True):
    depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
    #print(depth)
    if depth == 0:
      res += [d for d in dirs]
      dirs[:] = [] # Don't recurse any deeper
  print(res)
  print(len(res))
  #Create a pool of specific number of CPUs
  p = Pool(len(res))
  # Start each task within the pool
  p.map(back_up, res)
 
  sys.exit()
