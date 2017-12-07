import sqlalchemy as sa

from vakaavto import db


class AutoMark(db.Base):
    __tablename__ = 'vakaavto_auto_mark'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text, index=True)
    image = sa.Column(sa.Text)


class AutoModel(db.Base):
    __tablename__ = 'vakaavto_auto_model'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text, index=True)

    auto_mark_id = sa.Column(sa.Integer, sa.ForeignKey('vakaavto_auto_mark.id'))
