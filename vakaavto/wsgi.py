from werkzeug.middleware.proxy_fix import ProxyFix

from vakaavto.app import app

app = ProxyFix(app)
