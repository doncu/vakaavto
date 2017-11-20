from flask import url_for
from flask import render_template

from vakaavto.app import app


@app.route('/sitemaps.xml')
def sitemap_index():
    urls = (url_for('index'), )
    return render_template('sitemaps/index.xml', urls=urls)
