from flask import Flask
from flask.ext import restful
from gpioOut import GPIOOut

app = Flask(__name__)
api = restful.Api(app)

#needs to be decoupled
pins = [25,24,23,18]
gpioOut = GPIOOut(pins)

class Outputs(restful.Resource):
	def get(self):
		"List outputs"
		
		output = gpioOut.getOutputs()
		return output

	def put(self,putObject):
		"Update outputs"

		print putObject
		return True

class Output(restful.Resource):

	def get(self,pin):
		"Return state of given pin"
		print pin
		return gpioOut.getOutput(pin)

	def put(self,putObject):
		"Update given output"
		print putObject
		return True


if __name__ == '__main__':
	api.add_resource(Outputs, '/outputs')
	api.add_resource(Output, '/outputs/<int:pin>')
	app.run(host='0.0.0.0', port=80, debug=True)