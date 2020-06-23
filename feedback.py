#!/usr/bin/env python3
import os
import requests
import datetime

def listfeedback(directory):
  feedbacklist=[]
  for filename in os.listdir(directory):
    f,e = os.path.splitext(filename)
    if e == ".txt":
      with open(directory+filename,'r') as file:
        feedbackitem = { "title": "", "name": "", "date": "", "feedback": ""}
        for position, line in enumerate(file):
          if position == 0 :
            feedbackitem["title"] = line.rstrip()
          if position == 1 :
            feedbackitem["name"] = line.rstrip()
          if position == 2 :
            feedbackitem["date"] = datetime.datetime.strptime(line.rstrip(),'%Y-%m-%d').strftime('%b %d,%Y')
          if position == 3 :
            feedbackitem["feedback"] = line.rstrip()
          if position > 3:
            break
        feedbacklist.append(feedbackitem)
  return(feedbacklist)

if __name__ == "__main__":
  directory = "/data/feedback/"
  feedbacklist = listfeedback(directory)
  print(feedbacklist)

