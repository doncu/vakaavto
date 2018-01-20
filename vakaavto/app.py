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


import vakaavto.urls
from vakaavto import db
from vakaavto import models

app.teardown_request(db.remove_session)
app.add_template_global(utils.chunks, name='chunks')
app.add_template_global(dt.datetime.now, name='now')
app.add_template_global(lambda: db.session.query(models.AutoMark).all(), name='auto_marks')
app.add_template_global(
    lambda: db.session.query(models.Service).filter(models.Service.parent_id != None).all(),
    name='services'
)
