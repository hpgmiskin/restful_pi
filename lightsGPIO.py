"""
lightsGPIO.py - Henry Miskin
This provides the functionality to control remote plug sockets using the GPIO
for testing purposes the GPIO module does not have to successfully import
"""

#Import standard modules
import time
from shared import *

#Attempt to import GPIO module and configure to BCM mode
try:
  import RPi.GPIO as GPIO
  GPIO.setmode(GPIO.BCM)
  USE_GPIO = True
except ImportError:
  print "GPIO failed to import, disabling light functionality"
  USE_GPIO = False

#Define light names and on and off channels
LIGHTS = { 
  '1' : {'name' : 'TV Lamp',  'onChannel' : 22, 'offChannel' : 21},  
  '2' : {'name' : 'Standing Lamp',  'onChannel' : 27, 'offChannel' : 20},  
  '3' : {'name' : 'Reading Lamp', 'onChannel' : 17,  'offChannel' : 12}
}

class LightsGPIO():
  "LightsGPIO controls the interaction between the GPIO and the light remote"

  def __init__(self):
    "Set save file name for light name and state retention and load given file"
    self.filename = "lights.json"
    self.loadLights()

  def loadLights(self):
    "Load the save light states, if there is an error loading reset the light states"

    try:
      self.lights = loadJSON(self.filename)
    except IOError:
      self.resetLights()

  def saveLights(self):
    "Save the current light state"

    saveJSON(self.filename,self.lights)

  def resetLights(self):
    "Reset all lights to have a off state and save light states"

    self.lights = {}
    for lightID,light in LIGHTS.items():
      self.lights[lightID] = {
        'id' : lightID,
        'name' : light['name'],
        'state' : False
        }

    self.saveLights()

  def switch(self,channel):
    "Switch switches the given channel to output for a short period"
    
    #print "SWITCHING " + str(channel)
    if USE_GPIO: GPIO.setup(channel,GPIO.OUT)
    time.sleep(0.5)
    if USE_GPIO: GPIO.setup(channel,GPIO.IN)

  def getLights(self):
    "Loops through all lights and returns a list of lights"

    lights = []

    for light in self.lights.values():

      lights.append({
        'id' : light['id'],
        'name' : light['name'],
        'state' : light['state']
        })

    return lights

  def getLight(self,lightID):
    "Returns a single light object"

    return self.lights[str(lightID)]

  def setLight(self,light):
    "Sets the given light variables"

    lightID = light['id']

    if (self.lights[lightID]['name'] != light['name']):
      self.lights[lightID]['name'] = light['name']
      return True

    if (light['state'] == False):
      print "Turning off the " + light['name']
      self.switch(LIGHTS[lightID]['offChannel'])
    elif (light['state'] == True):
      print "Turning on the " + light['name']
      self.switch(LIGHTS[lightID]['onChannel'])
    else:
      return False

    self.lights[lightID]['state'] = light['state']
    self.saveLights()





