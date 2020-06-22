#!/usr/bin/env python3
import string
import os
os.chdir(os.path.expanduser("~/scripts/.git"))
path = '.'
path = os.path.normpath(path)
res = []
for root,dirs,files in os.walk(path, topdown=True):
    depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
    print(depth)
    if depth == 0:
        # We're currently two directories in, so all subdirs have depth 3
        res += [d for d in dirs]
        dirs[:] = [] # Don't recurse any deeper
print(res)
