import os

from flask_admin.form import upload
from flask_admin.contrib import sqla

import wtforms

from vakaavto import db
from vakaavto.app import app
from vakaavto.app import admin
from vakaavto.admin import fields
from vakaavto.models import auto
from vakaavto.models import howto
from vakaavto.models import service


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
    column_labels = dict(title='Заголовок')

    form_columns = ('title', 'image', )
    form_args = dict(title=dict(label='Название марки'))
    form_overrides = dict(title=wtforms.StringField)
    form_extra_fields = dict(
        image=upload.ImageUploadField(
            label='Картинка',
            base_path=os.path.join(app.config['IMG_PATH'], 'marks'),
            endpoint='image'
        )
    )


@register(None, 'Сервисы', '/admin/services/', 'admin.services')
class Services(AdminModelView):
    __model__ = service.Service

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    column_list = ('title', )
    column_labels = dict(title='Заголовок')

    form_columns = ('title', 'parent', 'glyphicon', 'image', 'text')
    form_args = dict(
        title=dict(label='Название сервиса'),
        parent=dict(label='Каталог'),
        glyphicon=dict(label='Название иконочки'),
        text=dict(label='Описание сервиса')
    )
    form_overrides = dict(title=wtforms.StringField, glyphicon=wtforms.StringField, text=fields.CKTextAreaField)
    form_extra_fields = dict(
        image=upload.ImageUploadField(
            label='Картинка',
            base_path=os.path.join(app.config['IMG_PATH'], 'services'),
            endpoint='image'
        )
    )


@register(None, 'Как это работает', '/admin/howto/', 'admin.howto')
class HowTo(AdminModelView):
    __model__ = howto.HowTo

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    column_list = ('title', )
    column_labels = dict(title='Заголовок')

    form_overrides = dict(title=wtforms.StringField, text=fields.CKTextAreaField)
