# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 20:39:55 2018

@author: Dell
"""

from flask import Flask

app = Flask(__name__)

# @ is denoting decorator - a way to wrap a function and modify its behaviour
@app.route('/')
def index():
    return "this is home page"

@app.route('/about')
def about():
    return "<h2>this is About page</h2>"

if __name__ =="__main__":
    app.run(debug=True)