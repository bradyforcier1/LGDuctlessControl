from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'yeeeeeeee'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    surname = TextField('Surname:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def control():
    form = ReusableForm(request.form)

    if request.method == 'POST':
        name=request.form['name']
        surname=request.form['surname']
        email=request.form['email']
        password=request.form['password']
        if form.validate():
            flash('Hello: {} {}'.format(name, surname))
        else:
            flash('Error: All Fields are Required')
    return render_template('master_control.html', form=form)

if __name__ == "__main__":
    app.run()

