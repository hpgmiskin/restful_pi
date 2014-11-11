from flask import Flask
from flask.ext.basicauth import BasicAuth

from secret import USERNAME,PASSWORD

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = USERNAME
app.config['BASIC_AUTH_PASSWORD'] = PASSWORD

basic_auth = BasicAuth(app)

@app.route('/secret')
@basic_auth.required
def secret_view():
	return "Hello Auth!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)