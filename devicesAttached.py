import re

from shared import *

DUMMY = True

DUMMY_DEVICES_LIST = [
  ["HenryPhone","FF-FF-FF-FF-FF-FF-FA","wireless"],
  ["IlanPhone","FF-FF-FF-FF-FF-FF-FB","wireless"],
  ["StevePhone","FF-FF-FF-FF-FF-FF-FC","wireless"],
  ["RaspberryPi","FF-FF-FF-FF-FF-FF-FD","wired"]
]

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

    owners = loadJSON(filename)
    owners[mac] = owner
    saveJSON(filename,owners)

  def getOwner(self,mac):
    "looks up in the known mac address table to see if the owner is known"

    owners = loadJSON("owners.json")

    try:
      owner = owners[mac]
    except KeyError:
      owner = "unknown"

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
