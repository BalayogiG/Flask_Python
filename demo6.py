# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 20:39:55 2018

@author: Dell
"""

from flask import Flask,request

app = Flask(__name__)

# @ is denoting decorator - a way to wrap a function and modify its behaviour
@app.route('/')
def index():
    return "Requested Method: %s" %request.method

@app.route('/bala', methods=['GET','POST'])
def bala():
	if request.method == 'POST':
		return "You using POST"
	else:
		return "You using GET"

if __name__ =="__main__":
    app.run(debug=True)