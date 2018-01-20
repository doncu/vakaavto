from vakaavto.app import app

from vakaavto.admin import views
from vakaavto.views import ajax
from vakaavto.views import pages
from vakaavto.views import helpers
from vakaavto.views import sitemap


app.add_url_rule('/ajax/send/email/', methods=['POST'], view_func=ajax.send_email)

app.add_url_rule('/', view_func=pages.index)
app.add_url_rule('/help/', view_func=pages.help)
app.add_url_rule('/contacts/', view_func=pages.contacts)
app.add_url_rule('/uslugi/', view_func=pages.catalog)
app.add_url_rule('/uslugi/<alias>/', view_func=pages.catalog)
app.add_url_rule('/uslugi/<catalog_alias>/<service_alias>/', view_func=pages.service)

app.add_url_rule('/sitemap-index.xml', view_func=sitemap.sitemap_index)
app.add_url_rule('/sitemap.xml', view_func=sitemap.sitemap)
app.add_url_rule('/sitemap-catalog.xml', view_func=sitemap.sitemap_catalog)
app.add_url_rule('/sitemap-service.xml', view_func=sitemap.sitemap_service)

# helpers
app.add_url_rule('/img/<filename>', endpoint='image', view_func=helpers.image_view)
