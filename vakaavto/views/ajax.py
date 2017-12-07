from flask import jsonify

from covador import item
from covador.flask import query_string

from vakaavto import db
from vakaavto.models import auto


@query_string(query=item(str))
def search_mark(query):
    objects = db.session.query(auto.AutoMark).filter(auto.AutoMark.title.ilike(query))
    return jsonify(result=[dict(id=obj.id, title=obj.title) for obj in objects])


@query_string(mark_id=item(int), query=item(str))
def search_model(mark_id, query):
    objects = db.session.query(auto.AutoMark).filter(
        auto.AutoModel.title.ilike(query),
        auto.AutoModel.auto_mark_id == mark_id
    )
    return jsonify(result=[dict(id=obj.id, title=obj.title) for obj in objects])
