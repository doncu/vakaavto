import collections

from flask import abort
from flask import render_template

from vakaavto import db
from vakaavto import models


def index():
    catalog = db.session.query(models.Service).filter(models.Service.parent_id == None).all()
    return render_template('index.html', catalog=catalog)


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
    return render_template('catalog.html', alias=alias, catalogs=catalogs)


def service(catalog_alias, service_alias):
    catalog = db.session.query(models.Service).filter(models.Service.alias == catalog_alias).first()
    obj = db.session.query(models.Service).filter(models.Service.alias == service_alias).first()
    if not catalog or not obj:
        return abort(404)
    return render_template('service.html', catalog=catalog, service=obj)
