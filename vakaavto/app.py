import datetime as dt
import os

from flask import Flask
from flask_admin import Admin

from vakaavto import settings
from vakaavto.common import utils

conf = settings.SETTINGS_MAP[os.environ['SETTINGS']]
app = Flask(
    __name__,
    template_folder=conf.TEMPLATE_FOLDER,
    static_url_path=conf.STATIC_URL_PATH,
    static_folder=conf.STATIC_FOLDER
)
app.config.from_object(conf)

admin = Admin(app, name='admin')


@app.teardown_request
def remove_session(*args):
    from vakaavto import db
    db.session.rollback()
    db.session.remove()


app.add_template_filter(utils.transliterate, name='transliterate')
app.add_template_global(utils.chunks, name='chunks')
app.add_template_global(dt.datetime.now, name='now')

import vakaavto.urls