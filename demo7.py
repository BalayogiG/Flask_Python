# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 20:39:55 2018

@author: Dell
"""

from flask import Flask, render_template

app = Flask(__name__)

# @ is denoting decorator - a way to wrap a function and modify its behaviour
@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


if __name__ =="__main__":
    app.run(debug=True)