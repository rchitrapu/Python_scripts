#! /usr/bin/env python3
import re
import operator
import os

errordict = {}
userdict = {}

with open(os.path.expanduser('~')+ "/data/syslog.log", encoding = "ISO-8859-1") as  file:
  logs = [line.rstrip() for line in file]
  for line in logs:
    pattern = r"ubuntu20 (\w+).*WARN\](.*)"
    result = re.search(pattern,line)
    if result :
        print(result.groups())
        if result[2] in errordict:
          errordict[result[2]] += 1
        else:
          errordict[result[2]] = 1
errordict=sorted(errordict.items(),key=operator.itemgetter(1),reverse=True)
print(errordict)
