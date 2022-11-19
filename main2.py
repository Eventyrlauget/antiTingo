from flask import Flask
import os

app = Flask(__name__)
if not os.path.exists("counterFile.txt"):
	file = open(counterFile.txt,xrw)
else: 
	file = open(counterFile.txt,rw)


@app.route("/")
def index():
	return "Hello World!"

def addItem(name):
	file.

app.run()

