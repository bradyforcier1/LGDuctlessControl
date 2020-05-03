from random import randint
from time import strftime
from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'yeeeeeeee'


class Zone(object):
    def __init__(self,name=None, ip=None):
        self.name = name
        self.ip = ip

master_bedroom = Zone('master_bedroom', '123.456')
guest_bedroom = Zone('guest_bedroom', '123.456')
living_room = Zone('living_room', '123.456')

@app.route("/", methods=['GET', 'POST'])
def index():
    form = request.form
    return render_template('master_control.html', form=form)

@app.route("/temp", methods=['POST'])
def temp():
    form = request.form
    temp=request.form['temp']
    flash('Set temp to: {}'.format(temp))
    return redirect(url_for('index'))

@app.route("/sleep", methods=['POST'])
def sleep():
    form = request.form
    sleep=request.form['sleep']
    flash('Sleep to sleep in {} minutes'.format(sleep))
    return redirect(url_for('index'))

@app.route("/off", methods=["GET"])
def off():
    flash("Turning all zones off")
    return redirect(url_for('index'))

@app.route("/on", methods=["GET"])
def on():
    flash("Turning all zones on")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()

