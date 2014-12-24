import os
from flask import Flask, request
from flask.ext.cors import CORS
from flask.ext.restful import Api, Resource, reqparse

from devicesAttached import DevicesAttached
devicesAttached = DevicesAttached("http://192.168.0.1/")

class Devices(Resource):
	"Devices provides the interface to interact with all network devices"
		
	def get(self):
		"Return a list of all attached devices on the network"
		
		return devicesAttached.getAttachedDevices()

class DevicesMAC(Resource):
	"DevicesMAC provides an interface to interact with a device with a given MAC address"
		
	def put(self,deviceMAC):
		"Set the owner of the device with given MAC address as per the device object"

		device = request.get_json()

		if (deviceMAC != device["mac"]):
			return False

		devicesAttached.setOwner(device["mac"],device["owner"])
			
		return True