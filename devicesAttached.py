import re,json,urllib2

def getContentRouter():

  feed = urllib2.urlopen('http://192.168.0.1/')
  return feed.read()

def findAttachedDevices(routerPage):

  pattern = re.compile(r"attach_dev = '(.*)';")
  matches = re.search(pattern, routerPage, flags=0)

  return matches.group(1)

def splitDeviceString(string):

  devices = []
  deviceList = string.split('<lf>')

  for deviceString in deviceList:
    device = deviceString.split(',')
    devices.append(device)

  return devices

def getDevicesObject(deviceList):

  devicesObject = []

  for device in deviceList:
    devicesObject.append({
      "name" : device[0],
      "mac" : device[1],
      "connection" : device[2]
      })

  return devicesObject

def getAttachedDevices():
  routerPage = getContentRouter()
  attachedDevices = findAttachedDevices(routerPage)
  deviceList = splitDeviceString(attachedDevices)
  devicesObject = getDevicesObject(deviceList)

  return devicesObject

if (__name__ == "__main__"):
  print getAttachedDevices()