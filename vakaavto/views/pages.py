from flask import render_template

from vakaavto.app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/marks/')
def marks():
    return render_template('marks.html')


@app.route('/faq/')
def faq():
    return render_template('faq.html')


@app.route('/contacts/')
def contacts():
    return render_template('contact.html')


@app.route('/services/')
def services():
    return render_template('services.html')

@app.route('/calc/')
def calc():
    return render_template('calc.html')