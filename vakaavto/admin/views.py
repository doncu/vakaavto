import os

from flask_admin.form import upload
from flask_admin.contrib import sqla

import wtforms
from wtforms import validators

from vakaavto import db
from vakaavto.app import app
from vakaavto.app import admin
from vakaavto.common import utils
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
    form_args = dict(title=dict(label='Название марки', validators=[validators.DataRequired()]))
    form_overrides = dict(title=wtforms.StringField)
    form_extra_fields = dict(
        image=upload.ImageUploadField(
            label='Картинка',
            base_path=os.path.join(app.config['IMG_PATH'], 'marks'),
            endpoint='image'
        )
    )


@register('Cервисы', 'Каталог', '/admin/catalog/', 'admin.catalog')
class Services(AdminModelView):
    __model__ = service.Service

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    column_list = ('title', )
    column_labels = dict(title='Заголовок')

    form_columns = ('title', 'glyphicon', 'image', )
    form_args = dict(
        title=dict(label='Название сервиса', validators=[validators.DataRequired()]),
        glyphicon=dict(label='Название иконочки', validators=[validators.DataRequired()]),
    )
    form_overrides = dict(title=wtforms.StringField, glyphicon=wtforms.StringField)
    form_extra_fields = dict(
        image=upload.ImageUploadField(
            label='Картинка',
            base_path=app.config['IMG_PATH'],
            endpoint='image',
            validators=[validators.DataRequired()]
        )
    )

    def on_model_change(self, form, model, is_created):
        super().on_model_change(form, model, is_created)
        model.alias = utils.transliterate(model.title)

    def get_query(self):
        query = super().get_query()
        return query.filter(self.model.parent_id == None)


@register('Cервисы', 'Сервисы', '/admin/services/', 'admin.services')
class Catalog(AdminModelView):
    __model__ = service.Service

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    column_list = ('title', 'parent')
    column_labels = dict(title='Заголовок', parent='Каталог')

    form_columns = ('title', 'parent', 'glyphicon', 'image', 'text')
    form_args = dict(
        title=dict(label='Название сервиса', validators=[validators.DataRequired()]),
        parent=dict(label='Каталог', validators=[validators.DataRequired()]),
        glyphicon=dict(label='Название иконочки', validators=[validators.DataRequired()]),
        text=dict(label='Описание сервиса', validators=[validators.DataRequired()])
    )
    form_overrides = dict(title=wtforms.StringField, glyphicon=wtforms.StringField, text=fields.CKTextAreaField)
    form_extra_fields = dict(
        image=upload.ImageUploadField(label='Картинка', base_path=app.config['IMG_PATH'], endpoint='image')
    )

    def on_model_change(self, form, model, is_created):
        super().on_model_change(form, model, is_created)
        model.alias = utils.transliterate(model.title)

    def get_query(self):
        query = super().get_query()
        return query.filter(self.model.parent_id != None)


@register(None, 'Как это работает', '/admin/howto/', 'admin.howto')
class HowTo(AdminModelView):
    __model__ = howto.HowTo

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    column_list = ('title', )
    column_labels = dict(title='Заголовок')

    form_args = dict(
        title=dict(label='Заголовок', validators=[validators.DataRequired()]),
        text=dict(label='Текст', validators=[validators.DataRequired()])
    )
    form_overrides = dict(title=wtforms.StringField, text=fields.CKTextAreaField)
