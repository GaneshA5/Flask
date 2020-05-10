from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
	now=datetime.datetime.now()
	newyear= now.month == 1 and now.day == 1
	return render_template("index.html",newyear=newyear)

