from flask import render_template

from vakaavto.app import app


@app.route('/')
def index():
    return render_template('index.html')
