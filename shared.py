"""
shared.py - Henry Miskin
This contains the shared helper functions that are used across the different
functions and objects in restful_pi 
"""

import csv,urllib2,json,time

from dropboxAPI import DropboxAPI

def saveErrorLog(exception):
  "saveLog"

  #Add error to data
  data = {"error":str(exception)}

  #Obtain local time and 
  timeStruct = time.localtime()
  [year,month,day,hour,minute,second,weekDay,yearDay,isDes] = timeStruct
  data["timestamp"] = "{:02d}:{:02d}:{:02d}".format(hour,minute,second)

  #Save file with date name
  filename = "error_log_{:02d}_{:02d}_{:02d}.csv".format(day,month,year)
  saveRow(filename,data)
  
  try:
    DropboxAPI().saveFile(filename)
  except Exception as exception:
    print str(exception)

def loadJSON(filename):
  "loads the file which contains a JSON string as an object"

  content = loadFile(filename)
  data = json.loads(content)

  return data

def saveJSON(filename,data):
  "saves the data object to the given file name as a JSON string"

  saveFile(filename,json.dumps(data))

def loadFile(filename):
  "Load a file with the given filename and return the content of the file"

  with open(filename,"r") as openFile:
    content = openFile.read()

  return content

def saveFile(filename,content):
  "Save a file with the given filename and content"

  with open(filename,"w") as openFile:
    openFile.write(content)

def getURL(url):
  "Returns the content of the given URL and if there is an error raises"

  try:
    feed = urllib2.urlopen(url, timeout=1)
    return feed.read()
  except Exception as exception:
    saveErrorLog(exception)

  return False

def saveRow(filename,data):
    "saveRow saves a row of data to a existing csv file"

    sortedData = sorted(data.items(), key=lambda i: i[0])

    try:
      temp = open(filename, 'r')
      temp.close()
    except IOError:
      with open(filename, 'w') as csvFile:
        csvWriter = csv.writer(csvFile, dialect="excel")
        csvWriter.writerow([key for (key,value) in sortedData])


    with open(filename, 'a') as csvFile:
        csvWriter = csv.writer(csvFile, dialect="excel")
        csvWriter.writerow([value for (key,value) in sortedData])
