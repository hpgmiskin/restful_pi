from flask import Flask, request
from flask.ext.cors import CORS
from flask.ext.restful import Api, Resource, reqparse

from lights import Lights

app = Flask(__name__, static_folder='/Users/miskinh/Code/angular_pi', static_url_path='')
api = Api(app)
cors = CORS(app, headers='Content-Type')

lights = Lights()

#function for root
@app.route('/')
def index():
	return app.send_static_file('index.html')


class Outputs(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		
	def get(self):
		"List outputs"
		
		return lights.getLights()

class OutputID(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()

	def put(self,lightID):
		"Update given output"

		light = request.get_json()
		print light
		success = lights.setLight(light)
			
		return True


if __name__ == '__main__':
	api.add_resource(Outputs, '/lights')
	api.add_resource(OutputID, '/lights/<int:lightID>')
	app.run(port=80, debug=True)