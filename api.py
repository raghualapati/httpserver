import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	query_parameters = request.args
	action = query_parameters.get('action')
	if action:
		out=perform_action ("hello world",action)
		return out
	else:
		return "hello world"
	
@app.route('/hello', methods=['GET'])
def hello():
	query_parameters = request.args
	action = query_parameters.get('action')
	if action:
		out=perform_action ("hello",action)
		return out
	else:
		return "hello"
	
@app.route('/world', methods=['GET'])
def world():
	query_parameters = request.args
	action = query_parameters.get('action')
	if action:
		out=perform_action ("world",action)
		return out
	else:
		return "world"

def perform_action(string,action):
	if action == "uppercase":
		out_string = string.upper()
	elif action == "reverse":
		out_string = string[::-1]
	return out_string

app.run(host="0.0.0.0",port=8090)
