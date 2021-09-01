# import flask
from flask import Flask, render_template, url_for
# create an instance of flask object
app = Flask(__name__)

# home page accessed with http://127.0.0.1:5000/
@app.route("/")
# map URL route for function below
def index():
    return render_template("index.html")
