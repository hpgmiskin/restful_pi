import os
from flask import Flask, request
from flask.ext.cors import CORS
from flask.ext.restful import Api, Resource, reqparse

from lightsGPIO import LightsGPIO
lightsGPIO = LightsGPIO()

class Lights(Resource):

	def get(self):
		"List outputs"
		
		return lightsGPIO.getLights()

class LightID(Resource):

	def get(self,lightID):
		"Return the given light"

		return lightsGPIO.getLight(lightID)

	def put(self,lightID):
		"Update given output"

		light = request.get_json()
		success = lightsGPIO.setLight(light)
			
		return True