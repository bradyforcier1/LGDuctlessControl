from random import randint
from time import strftime
from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

import subprocess

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'yeeeeeeee'


@app.route("/temp", methods=['GET'])
def temp():
    temp=request.args['temp']
    print ('Set temp to: {}'.format(temp))
    return '', 200

@app.route("/sleep", methods=['GET'])
def sleep():
    sleep=request.args['sleep']
    print ('Going to sleep in {}'.format(sleep))
    return '', 200 

@app.route("/off", methods=["GET"])
def off():
    print ("Turning off")
    subprocess.call("./on.sh")
    return '', 200 

@app.route("/on", methods=["GET"])
def on():
    print ("Turning on")
    subprocess.call("./on.sh")
    return '', 200 

if __name__ == "__main__":
    app.run()

