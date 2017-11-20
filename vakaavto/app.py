import os
import datetime as dt

from flask import Flask

from vakaavto import settings


conf = settings.SETTINGS_MAP[os.environ['SETTINGS']]
app = Flask(
    __name__,
    template_folder=conf.TEMPLATE_FOLDER,
    static_url_path=conf.STATIC_URL_PATH,
    static_folder=conf.STATIC_FOLDER
)
app.config.from_object(conf)

app.add_template_global(dt.datetime.now, name='now')


import vakaavto.views.pages
import vakaavto.views.sitemap
