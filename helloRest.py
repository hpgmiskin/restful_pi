from flask import Flask
from flask.ext.restful import Api, Resource
from flask.ext.httpauth import HTTPBasicAuth

from secret import USERNAME,PASSWORD

app = Flask(__name__)
api = Api(app)

auth = HTTPBasicAuth()

@auth.get_password
def getPassword(username):
    if username == USERNAME:
    	return PASSWORD
    return None

class HelloWorld(Resource):
	decorators = [auth.login_required]
	def get(self):
		return {'hello': 'rest'}

if __name__ == '__main__':
	api.add_resource(HelloWorld, '/')
	app.run(host='0.0.0.0', port=80, debug=True)