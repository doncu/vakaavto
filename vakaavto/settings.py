import os


class BaseSettings:
    DOMAIN = 'vaka-avto.ru'

    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    TEMPLATE_FOLDER = os.path.join(BASE_PATH, 'templates')

    STATIC_URL_PATH = ''
    STATIC_FOLDER = ''


class LocalSettings(BaseSettings):
    STATIC_URL_PATH = '/static'
    STATIC_FOLDER = os.path.join(os.path.dirname(BaseSettings.BASE_PATH), 'static')


class ProdSettings(BaseSettings):
    pass


SETTINGS_MAP = {
    'local': LocalSettings,
    'prod': ProdSettings
}