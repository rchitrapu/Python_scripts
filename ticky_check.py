#! /usr/bin/env python3
import re
import operator
import csv

errordict = {}
userdict = {}

with open("syslog.log", encoding = "UTF-8") as  file:
  logs = [line.rstrip() for line in file]
  for line in logs:
    pattern = r"ticky: (\w*) (.*) \(([\w\.]*)\)$"
    result = re.search(pattern,line)
    if result :
      count = [0,0]
      if result[1] == "ERROR":
        if result[2] in errordict:
          errordict[result[2]] += 1
        else:
          errordict[result[2]] = 1
        if result[3] in userdict:
          count  = userdict[result[3]]
          count[1] += 1
          userdict[result[3]] =  count
        else: 
          count[1] += 1
          userdict[result[3]] =  count
      if result[1] == "INFO":
        if result[3] in userdict:
          count  = userdict[result[3]]
          count[0] += 1
          userdict[result[3]] =  count
        else:
          count[0] += 1
          userdict[result[3]] =  count       

errorlist=sorted(errordict.items(),key=operator.itemgetter(1),reverse=True)
userlist=sorted(userdict.items(),key=operator.itemgetter(0))

errorlist.insert(0,('Error','Count'))
with open("error_message.csv","w") as  file:
  writer = csv.writer(file)
  writer.writerows(errorlist)

userrep = []
for item in userlist :
   userrep.append([item[0],item[1][0],item[1][1]])
userrep.insert(0,["Username", "INFO", "ERROR"])


with open("user_statistics.csv","w") as  file:
  writer = csv.writer(file)
  writer.writerows(userrep)

