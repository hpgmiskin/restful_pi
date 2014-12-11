#import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM)

def switch(channel):
    
    print "SWITCHING " + str(channel)
    #GPIO.setup(channel,GPIO.OUT)
    time.sleep(0.5)
    #GPIO.setup(channel,GPIO.IN)

lights = { 
  1 : 
    {
    'name' : 'TV Lamp',
    'onChannel' : 22,
    'offChannel' : 21
    },
  2 :
    {
    'name' : 'Standing Lamp',
    'onChannel' : 27,
    'offChannel' : 20
    },
  3 : 
    {
    'name' : 'Reading Lamp',
    'onChannel' : 17,
    'offChannel' : 12
    }
}

class LightsGPIO():

  def __init__(self):
    self.lights = []

    for lightID,light in lights.items():
      #switch(light['offChannel'])

      self.lights.append({
        'id' : lightID,
        'name' : light['name'],
        'state' : False
        })

  def getLights(self):

    return self.lights

  def setLight(self,light):

    lightID = light['id']
    lightState = light['state']

    if (light['state'] == False):
      print "Turning off the " + light['name']
      switch(lights[lightID]['offChannel'])
    elif (light['state'] == True):
      print "Turning on the " + light['name']
      switch(lights[lightID]['onChannel'])
    else:
      return False

    for i in range(len(self.lights)):
      if (self.lights[i]['id'] == lightID):
        self.lights[i] = light
        return True





