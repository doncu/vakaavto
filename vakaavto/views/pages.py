import collections

from flask import render_template

from vakaavto import db
from vakaavto.models import auto
from vakaavto.models import service


def index():
    services = db.session.query(service.Service).filter(service.Service.parent_id is None).all()
    auto_marks = db.session.query(auto.AutoMark).all()
    return render_template('index.html', services=services, auto_marks=auto_marks)


def marks():
    auto_marks = db.session.query(auto.AutoMark).all()
    return render_template('marks.html', auto_marks=auto_marks)


def help():
    return render_template('help.html')


def contacts():
    return render_template('contact.html')


def services():
    parent_objects = db.session.query(service.Service).filter(service.Service.parent_id == None).all()
    child_objects = db.session.query(service.Service).filter(service.Service.parent_id != None).all()
    childs = collections.defaultdict(list)
    for obj in child_objects:
        childs[obj.parent_id].append(obj)
    result = [dict(obj=obj, childs=childs.get(obj.id, [])) for obj in parent_objects]
    return render_template('services.html', services=result)


def calc():
    return render_template('calc.html')
