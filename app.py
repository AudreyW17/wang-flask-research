# Coded By:  Audrey Wang
# Filename:  app.py
# Purpose: Flask app for Research Website
from flask import Flask, render_template, url_for, request, jsonify
from datetime import datetime
import pyrebase

app = Flask(__name__)

config = {}

key = 0 # If recording data over time, keys should be seconds or milliseconds from 0.

# Notes:
# 1. The @app.route parameter (in parantheses) should match the name of the page to which it routes, without the ".html"
#    Ex. If routing to signIn.html: @app.route("/signIn") -- You need to add the forward slash before the parameter
#    The only exception is the @app.route for the index page: @app.route("/")
# 2. When linking to index.html from other html pages when using Flask, use {{url_for('index')}}. The name of the python function (_name_) is used as the endpoint, unless you specify the endpoint argument explicitly.
#    Ex. {{url_for('index')}} will redirect the user to index.html because "index" is the name of the defined route function


@app.route("/") # Landing Page
def index():
    return render_template("index.html", title="Landing")

@app.route("/authors") # Account Registration Page
def authors():
    return render_template("authors.html", title="Authors")

@app.route("/procedure") # Sign In Page
def procedure():
    return render_template("procedure.html", title = "Procedures")

@app.route("/results") # Account Home Page
def results():
    return render_template("results.html", title="Results")


# Run server on local IP address on port 5000
# Replace the: ***,***,*** between the quotes with your laptop's IP address
# If you see the error: "The requested address is not valid in its context" it means the 
# IP address specified for the host is incorrect.

if __name__ == "__main__":
    app.run(debug=False, host='10.76.23.131', port=5000)
