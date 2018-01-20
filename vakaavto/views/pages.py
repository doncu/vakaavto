import collections

from flask import abort
from flask import render_template

from vakaavto import db
from vakaavto import models


def index():
    services = db.session.query(models.Service).filter(models.Service.parent_id == None).all()
    auto_marks = db.session.query(models.AutoMark).all()
    return render_template('index.html', services=services, auto_marks=auto_marks)


def help():
    objects = db.session.query(models.HowTo).all()
    return render_template('help.html', objects=objects)


def contacts():
    return render_template('contact.html')


def catalog(alias=None):
    catalogs = db.session.query(models.Service).filter(models.Service.parent_id == None).all()
    service_objects = db.session.query(models.Service).filter(models.Service.parent_id != None).all()
    childs = collections.defaultdict(list)
    for obj in service_objects:
        childs[obj.parent_id].append(obj)
    catalogs = [dict(obj=obj, services=childs.get(obj.id, [])) for obj in catalogs]
    return render_template('services.html', alias=alias, catalogs=catalogs)


def service(catalog_alias, service_alias):
    catalog = db.session.query(models.Service).filter(models.Service.alias == catalog_alias).first()
    obj = db.session.query(models.Service).filter(models.Service.alias == service_alias).first()
    auto_marks = db.session.query(models.AutoMark).all()
    if not catalog or not obj:
        return abort(404)
    return render_template('connect.html', catalog=catalog, service=obj, auto_marks=auto_marks)
