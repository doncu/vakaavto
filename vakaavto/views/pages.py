import collections

from flask import render_template

from vakaavto import db
from vakaavto.models import auto
from vakaavto.models import howto
from vakaavto.models import service


def index():
    services = db.session.query(service.Service).filter(service.Service.parent_id == None).all()
    auto_marks = db.session.query(auto.AutoMark).all()
    return render_template('index.html', services=services, auto_marks=auto_marks)


def help():
    objects = db.session.query(howto.HowTo).all()
    return render_template('help.html', objects=objects)


def contacts():
    return render_template('contact.html')


def services():
    catalogs = db.session.query(service.Service).filter(service.Service.parent_id == None).all()
    service_objects = db.session.query(service.Service).filter(service.Service.parent_id != None).all()
    childs = collections.defaultdict(list)
    for obj in service_objects:
        childs[obj.parent_id].append(obj)
    catalogs = [dict(obj=obj, services=childs.get(obj.id, [])) for obj in catalogs]
    return render_template('services.html', catalogs=catalogs)


def calc():
    return render_template('calc.html')
