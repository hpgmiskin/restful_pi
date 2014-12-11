import re,socket,httplib,urllib2,time
from secret import GOPRO_PASSWORD
from shared import *

class GoProControl(object):
  """docstring for GoProControl"""

  def getURL(self,url):

    self.log += "URL: {}\n".format(url)

    try:
      feed = urllib2.urlopen(url)
      return feed.read()
    except urllib2.HTTPError, e:
      self.log += 'HTTPError = ' + str(e.code) + '\n'
    except urllib2.URLError, e:
      self.log += 'URLError = ' + str(e.reason) + '\n'
    except httplib.HTTPException, e:
      self.log += 'HTTPException' + '\n'
    except socket.timeout, e:
      self.log += "There was a timeout error: {}\n".format(e) 

    return False

  def getFile(self,saveName=None,fileType='JPG'):

    order = {'OldestFiles':'d',"NewestFirst":'D'}

    url = "http://10.5.5.9:8080/videos/DCIM/100GOPRO/?order={}".format(order["NewestFirst"])
    indexContent = self.getURL(url)

    if not indexContent:
      return

    pattern = re.compile(r'<a class="link" href="G[0-9]*.{}">(G[0-9]*.{})</a>'.format(fileType,fileType))
    matches = re.search(pattern, indexContent, flags=0)
    #find all to get all photos

    fileName = matches.group(1)
    print fileName
    fileURL = "http://10.5.5.9:8080/videos/DCIM/100GOPRO/{}".format(fileName)
    fileContent = self.getURL(fileURL)

    if not fileContent:
      return

    if (saveName != None):
      fileName = saveName

    saveFile(fileName,fileContent)

  def runCommand(self,command):
    "Turns on the GoPro"

    print command
    self.log += "Command: {}\n".format(command)

    commandDict = {
      #Power
      'PowerOn':('bacpac','PW','01'),
      'PowerOff':('bacpac','PW','00'),
      'PreviewOn': ('camera','PV','02'),
      'PreviewOff': ('camera','PV','00'),
      #Shutter
      'Shutter' : ('bacpac','SH','01'),
      'Stop' : ('bacpac','SH','00'),
      #Mode
      'TimelapseMode' : ('camera','CM','00'), 
      'BurstMode' : ('camera','CM','01'), 
      'PhotoMode' : ('camera','CM','02'), 
      'VideoMode' : ('camera','CM','03')
      }

    url = "http://10.5.5.9/{}/{}?t={}&p=%{}".format(
      commandDict[command][0],
      commandDict[command][1],
      GOPRO_PASSWORD,
      commandDict[command][2]
      )

    #print url
    self.getURL(url)

  def takePhoto(self):

    runCommand('PowerOn')
    time.sleep(1)
    runCommand('PhotoMode')
    time.sleep(1)
    runCommand('Shutter')
    time.sleep(1)
    runCommand('PowerOff')


  def downloadPhoto(self):

    runCommand('PowerOn')
    time.sleep(1)
    getFile("NewPhoto.JPG")
    time.sleep(1)
    runCommand('PowerOff')


  def updatePhoto(self):

    self.log = ""

    self.runCommand('PowerOn')
    time.sleep(1)
    self.runCommand('PhotoMode')
    time.sleep(1)
    self.runCommand('Shutter')
    time.sleep(1)
    self.getFile("NewPhoto.JPG")
    time.sleep(1)
    self.runCommand('PowerOff')

    print self.log

    return self.log