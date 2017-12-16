import base64
import logging
from flask import jsonify

from covador import opt
from covador import item
from covador.flask import json_body
from covador.flask import query_string

from vakaavto import db
from vakaavto.models import auto


logger = logging.getLogger('ajax')


@query_string(query=item(str))
def search_mark(query):
    objects = db.session.query(auto.AutoMark).filter(auto.AutoMark.title.ilike(query))
    return jsonify(result=[dict(id=obj.id, title=obj.title) for obj in objects])


@json_body(service=opt(int), mark=item(int), model=item(str), tel=item(str) | base64.decode)
def send_email(mark, model, tel):
    try:
        pass
    except Exception:
        logger.exception('Send mail error')
    return jsonify(result='ok')
