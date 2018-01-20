from sqlalchemy import orm

from flask import url_for
from flask import render_template

from vakaavto import db
from vakaavto import models


def sitemap_index():
    urls = (
        url_for('sitemap'),
        url_for('sitemap_catalog'),
        url_for('sitemap_service'),
    )
    return render_template('sitemaps/urls.xml', urls=urls)


def sitemap():
    urls = (
        url_for('index'),
        url_for('help'),
        url_for('catalog'),
    )
    return render_template('sitemaps/urls.xml', urls=urls)


def sitemap_catalog():
    urls = []
    objects = db.session.query(models.Service).filter(models.Service.parent_id == None).all()
    for obj in objects:
        urls.append(url_for('catalog', alias=obj.alias))
    return render_template('sitemaps/urls.xml', urls=urls)


def sitemap_service():
    urls = []
    objects = db.session.query(models.Service).filter(
        models.Service.parent_id != None
    ).options(orm.joinedload('parent'))
    for obj in objects:
        urls.append(url_for('service', catalog_alias=obj.parent.alias, service_alias=obj.alias))
    return render_template('sitemaps/urls.xml', urls=urls)
