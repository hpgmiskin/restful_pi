from flask import Flask
from flask.ext.restful import Api, Resource, reqparse
from gpioOut import GPIOOut

app = Flask(__name__)
api = Api(app)

#needs to be decoupled
pins = [25,24,23,18]
gpioOut = GPIOOut(pins)

#function for root
@app.route('/')
def hello():
	return "ROOT"

class Outputs(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()

	def get(self):
		"List outputs"
		
		output = gpioOut.getOutputs()
		return output

	def put(self):
		"Update outputs"

		arguments = self.reqparse.parse_args()

		for key, value in arguments.iteritems():
			print key,value

		return True

class OutputID(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()

	def get(self,pin):
		"Return state of given pin"
		print pin
		return gpioOut.getOutput(pin)

	def put(self,putObject):
		"Update given output"

		arguments = self.reqparse.parse_args()

		for key, value in arguments.iteritems():
			print key,value
			
		return True


if __name__ == '__main__':
	api.add_resource(Outputs, '/outputs')
	api.add_resource(OutputID, '/outputs/<int:pin>')
	app.run(host='0.0.0.0', port=80, debug=True)