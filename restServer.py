"""
restServer.py - Henry Miskin
Combines the rest functionality of a number of different elements to run a single
rest interface where the url endpoints are connected to imported Classes
"""

#library imports
import os

#Flask imports
from flask import Flask, request
from flask.ext.cors import CORS
from flask.ext.restful import Api, Resource, reqparse

#Local Rest Server Imports
from lightsRest import *
from devicesRest import *
from goproRest import *

#Local Utility Imports
from taskScheduler import getScheduler
from shared import saveErrorLog

#Return Scheduler
scheduler = getScheduler()

#Find static path from relative path
currentPath = os.getcwd()
basePath = os.path.split(currentPath)[0]
staticPath = os.path.join(basePath,'angular_pi')

#Define static folder path
app = Flask(__name__, static_folder=staticPath, static_url_path='')
api = Api(app)
cors = CORS(app, headers='Content-Type')

@app.route('/')
def index():
  "Index file to run the front end components through angular JS"
  return app.send_static_file('index.html')

if __name__ == '__main__':

  #Add GoPro Resource
  api.add_resource(GoPro, '/gopro')

  #Add Devices Resources
  api.add_resource(Devices, '/devices')
  api.add_resource(DevicesMAC, '/devices/<string:deviceMAC>')

  #Add Lights Resources
  api.add_resource(Lights, '/lights')
  api.add_resource(LightID, '/lights/<int:lightID>')

  #Start Scheduler 
  scheduler.start()

  #Run Server on port 0.0.0.0
  try:
    app.run(host='0.0.0.0', port=80, debug=False)
  except Exception as exception:
    saveErrorLog(exception)
    scheduler.shutdown()