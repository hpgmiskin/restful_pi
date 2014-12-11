import os
from flask import Flask, request, send_file, send_from_directory
from flask.ext.cors import CORS
from flask.ext.restful import Api, Resource, reqparse

from goproControl import GoProControl

goproControl = GoProControl()

class GoPro(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    
  def get(self):
    "List outputs"

    return send_from_directory(os.getcwd(), 'NewPhoto.JPG')

    #return send_file('NewPhoto.JPG',mimetype='image/jpg')

  def put(self):
    "List outputs"
    
    log = goproControl.updatePhoto()
    
    return {"fullLog":log}