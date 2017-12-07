#!/usr/bin/env python3

import os
import click

from flask.cli import FlaskGroup


@click.group(cls=FlaskGroup)
@click.option('--debug/--no-debug', default=True, help='Enable/disable debug mode')
def cli(debug):
    os.environ['SETTINGS'] = 'local'
    os.environ['FLASK_APP'] = 'vakaavto/app.py'
    os.environ['FLASK_DEBUG'] = '1' if debug else '0'


@cli.command(with_appcontext=False)
def initdb():
    from vakaavto import app
    from vakaavto import db
    db.import_models()


if __name__ == '__main__':
    cli()
