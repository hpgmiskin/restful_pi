import os
from flask import Flask, request
from flask.ext.cors import CORS
from flask.ext.restful import Api, Resource, reqparse

from devicesAttached import DevicesAttached
devicesAttached = DevicesAttached("http://192.168.0.1/")

class Devices(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		
	def get(self):
		"List outputs"
		
		return devicesAttached.getAttachedDevices()

class DevicesMAC(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		
	def put(self,deviceMAC):
		"Update given output"

		device = request.get_json()

		if (deviceMAC != device["mac"]):
			return False

		devicesAttached.setOwner(device["mac"],device["owner"])
			
		return True