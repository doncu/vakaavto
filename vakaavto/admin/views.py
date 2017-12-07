from flask_admin.form import upload
from flask_admin.contrib import sqla

import wtforms

from vakaavto import db
from vakaavto.app import app
from vakaavto.app import admin
from vakaavto.models import auto


class AdminModelView(sqla.ModelView):
    def __init__(self, model=None, name=None, category=None, endpoint=None, url=None):
        super().__init__(model or self.__model__, db.session, name, category, endpoint, url)


def register(category=None, name=None, url=None, endpoint=None, **kwargs):
    def decorator(cls):
        view = cls(category=category, name=name, url=url, endpoint=endpoint, **kwargs)
        cls.instance = view
        admin.add_view(view)
        return cls
    return decorator


@register(None, 'Марки авто', '/admin/automarks/', 'admin.automarks')
class AutoMarks(AdminModelView):
    __model__ = auto.AutoMark

    column_list = ('title', )

    form_overrides = dict(title=wtforms.StringField)
    form_extra_fields = dict(image=upload.ImageUploadField(base_path=app.config['IMG_PATH'], endpoint='image'))


@register(None, 'Марки авто', '/admin/automarks/', 'admin.automarks')
class AutoMarks(AdminModelView):
    __model__ = auto.AutoMark

    column_list = ('title', )

    form_overrides = dict(title=wtforms.StringField)
    form_extra_fields = dict(image=upload.ImageUploadField(base_path=app.config['IMG_PATH'], endpoint='image'))
