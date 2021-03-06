import os


class BaseSettings:
    DOMAIN = 'vakaavto.ru'

    SECRET_KEY = 'adsttasdasdoasd0as98d0am4m35048m90mcw4fum3h4650439875n4354'

    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    TEMPLATE_FOLDER = os.path.join(BASE_PATH, 'templates')

    STATIC_URL_PATH = ''
    STATIC_FOLDER = ''

    DATABASE_URI = ''
    IMG_PATH = ''

    EMAIL_SERVER = 'smtp.mail.ru:465'
    EMAIL_FROM = 'no-replay@vakaavto.ru'
    EMAIL_TO = 'no-replay@vakaavto.ru'
    EMAIL_USER = os.environ.get('EMAIL_USER')
    EMAIL_PASS = os.environ.get('EMAIL_PASS')


class LocalSettings(BaseSettings):
    STATIC_URL_PATH = '/static'
    STATIC_FOLDER = os.path.join(os.path.dirname(BaseSettings.BASE_PATH), 'static')

    DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BaseSettings.BASE_PATH, '..', 'vakaavto.db'))
    IMG_PATH = os.path.join(os.path.dirname(BaseSettings.BASE_PATH), 'img')


class ProdSettings(BaseSettings):
    STATIC_URL_PATH = '/static'

    DATABASE_URI = os.environ.get('DATABASE_URI')
    IMG_PATH = os.environ.get('IMG_PATH')


SETTINGS_MAP = {
    'local': LocalSettings,
    'prod': ProdSettings
}

