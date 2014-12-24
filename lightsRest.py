import os
from flask import Flask, request
from flask.ext.cors import CORS
from flask.ext.restful import Api, Resource, reqparse

from lightsGPIO import LightsGPIO
lightsGPIO = LightsGPIO()

class Lights(Resource):
	"Lights provides the interface to interact with all lights"

	def get(self):
		"Returns a list of all lights in there current state"
		
		return lightsGPIO.getLights()

class LightID(Resource):
	"LightID provides the interface to interact with a single light"

	def get(self,lightID):
		"Return the given light"

		return lightsGPIO.getLight(lightID)

	def put(self,lightID):
		"Update the given light state"

		light = request.get_json()
		success = lightsGPIO.setLight(light)
			
		return success