from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
	return '<h5>Hello world</h5>'


@app.route('/greet/<name>')
def greet(name):
	return f'Hello, {ne}'
