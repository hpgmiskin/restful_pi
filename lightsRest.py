import os
from flask import Flask, request
from flask.ext.cors import CORS
from flask.ext.restful import Api, Resource, reqparse

from lightsGPIO import LightsGPIO
lightsGPIO = LightsGPIO()

class Lights(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		
	def get(self):
		"List outputs"
		
		return lightsGPIO.getLights()

class LightID(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()

	def get(self,lightID):
		"Return the given light"

		return [light for light in lightsGPIO.getLights() if light.id == lightID][0]

	def put(self,lightID):
		"Update given output"

		light = request.get_json()
		print light
		success = lightsGPIO.setLight(light)
			
		return True