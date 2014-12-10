import os
from flask import Flask, request
from flask.ext.cors import CORS
from flask.ext.restful import Api, Resource, reqparse

#Local Imports
from lightsRest import *
from devicesRest import *

currentPath = os.getcwd()
basePath = os.path.split(currentPath)[0]
staticPath = os.path.join(basePath,'angular_pi')

app = Flask(__name__, static_folder=staticPath, static_url_path='')
api = Api(app)
cors = CORS(app, headers='Content-Type')

#static index file
@app.route('/')
def index():
  return app.send_static_file('index.html')

if __name__ == '__main__':

  api.add_resource(Devices, '/devices')

  api.add_resource(Lights, '/lights')
  api.add_resource(LightID, '/lights/<int:lightID>')

  app.run(host='0.0.0.0', port=80, debug=True)