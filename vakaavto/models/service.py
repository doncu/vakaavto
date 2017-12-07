import sqlalchemy as sa
from sqlalchemy import orm

from vakaavto import db


class Service(db.Base):
    __tablename__ = 'vakaavto_services'

    id = sa.Column(sa.Integer, primary_key=True)

    title = sa.Column(sa.Text, index=True)

    min_image = sa.Column(sa.Text, nullable=True, default=None)
    big_image = sa.Column(sa.Text, nullable=True, default=None)

    parent_id = sa.Column(sa.Integer, sa.ForeignKey('vakaavto_services.id'), nullable=True, default=None)
    parent = orm.relationship('Service')
