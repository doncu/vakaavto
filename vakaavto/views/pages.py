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
