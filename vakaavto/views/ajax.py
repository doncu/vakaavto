import logging
from flask import current_app, jsonify

from covador import opt
from covador import item
from covador.flask import json_body

from vakaavto.common import email


logger = logging.getLogger('ajax')


@json_body(
    service=opt(int),
    mark=opt(int),
    name=opt(str),
    model=opt(str),
    tel=item(str),
    text=opt(str)
)
def send_email(**kwargs):
    try:
        email.send(
            host=current_app.config['EMAIL_SERVER'],
            log_pass=(current_app.config['EMAIL_USER'], current_app.config['EMAIL_PASS']),
            subject='Новое обращение на сайте',
            from_=current_app.config['EMAIL_FROM'],
            to=current_app.config['EMAIL_TO'],
            template='email/resource.html',
            **kwargs
        )
    except Exception:
        logger.exception('Send mail error')
        return jsonify(result='error'), 500
    return jsonify(result='ok')
