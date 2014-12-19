import re

from shared import *
from secret import DUMMY_DEVICES_LIST

DUMMY = True

class DevicesAttached():

  def __init__(self,routerURL):
    self.routerURL = routerURL

  def splitDeviceString(self,devicesString):
    "Splits the given deviceString and returns a list of device lists"

    devices = []
    deviceList = string.split('<lf>')

    for deviceString in deviceList:
      device = deviceString.split(',')
      devices.append(device)

    return devices

  def getDevicesList(self):
    "returns a list of devices attached to the router who URL constructed class"

    routerContent = getURL(self.routerURL)

    pattern = re.compile(r"attach_dev = '(.*)';")
    matches = re.search(pattern, self.routerContent, flags=0)

    return self.splitDeviceString(matches.group(1))

  def setOwner(self,mac,owner):
    "Sets the given mac address to the given owner"

    filename = "owners.json"

    try:
      owners = loadJSON(filename)
    except IOError:
      owners = {}
      
    owners[mac] = owner
    saveJSON(filename,owners)

  def getOwner(self,mac):
    "looks up in the known mac address table to see if the owner is known"

    try:
      owners = loadJSON("owners.json")
    except IOError:
      owners = {}

    try:
      owner = owners[mac]
    except KeyError:
      owner = "other"

    return owner

  def setAttachedDevices(self):

    self.devices = []

    if DUMMY:
      devicesList = DUMMY_DEVICES_LIST
    else:
      devicesList = self.getDevicesList()

    for device in devicesList:
      [name,mac,connection] = device
      owner = self.getOwner(mac)

      self.devices.append({
        "name" : name,
        "owner" : owner,
        "mac" : mac,
        "connection" : connection
        })

  def getAttachedDevices(self):

    self.setAttachedDevices()
    return self.devices
