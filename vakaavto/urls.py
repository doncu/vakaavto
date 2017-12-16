from vakaavto.app import app

from vakaavto.admin import views
from vakaavto.views import ajax
from vakaavto.views import pages
from vakaavto.views import helpers
from vakaavto.views import sitemap


app.add_url_rule('/ajax/search/mark/', methods=['POST'], view_func=ajax.search_mark)
app.add_url_rule('/ajax/send/email/', methods=['POST'], view_func=ajax.send_email)

app.add_url_rule('/', view_func=pages.index)
app.add_url_rule('/help/', view_func=pages.help)
app.add_url_rule('/contacts/', view_func=pages.contacts)
app.add_url_rule('/services/', view_func=pages.services)
app.add_url_rule('/services/<alias>/', view_func=pages.services)
app.add_url_rule('/calc/', view_func=pages.calc)

app.add_url_rule('/sitemaps.xml', view_func=sitemap.sitemap_index)

# helpers
app.add_url_rule('/img/<filename>', endpoint='image', view_func=helpers.image_view)
