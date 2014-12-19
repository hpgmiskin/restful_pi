"""
shared.py - Henry Miskin
This contains the shared helper functions that are used across the different
functions and objects in restful_pi 
"""

import urllib2,json

def loadJSON(filename):
  "loads the file which contains a JSON string as an object"

  content = loadFile(filename)

  if (content != ""):
    data = json.loads(content)
  else:
    data = {}

  return data

def saveJSON(filename,data):
  "saves the data object to the given file name as a JSON string"

  saveFile(filename,json.dumps(data))

def loadFile(filename):
  "Load a file with the given filename and return the content of the file"

  try:
    with open(filename,"r") as openFile:
      content = openFile.read()
  except:
    content = ""

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
  except urllib2.HTTPError, e:
    raise ValueError("HTTP Error: {}".format(e.code))
  except urllib2.URLError, e:
    raise ValueError('URLError: {}'.format(e.reason))
  except httplib.HTTPException, e:
    raise ValueError('HTTPException')
  except socket.timeout, e:
    raise ValueError("There was a time-out error: {}".format(e))

  return False