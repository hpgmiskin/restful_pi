from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
	def get(self):
		return {'hello': 'world'}

if __name__ == '__main__':
	api.add_resource(HelloWorld, '/')
	app.run(host='0.0.0.0', port=80, debug=True)