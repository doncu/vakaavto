from vakaavto.app import app

from vakaavto.admin import views
from vakaavto.views import ajax
from vakaavto.views import pages
from vakaavto.views import helpers
from vakaavto.views import sitemap


app.add_url_rule('/ajax/search/mark/', view_func=ajax.search_mark)
app.add_url_rule('/ajax/search/model/', view_func=ajax.search_model)

app.add_url_rule('/', view_func=pages.index)
app.add_url_rule('/marks/', view_func=pages.marks)
app.add_url_rule('/help/', view_func=pages.help)
app.add_url_rule('/contacts/', view_func=pages.contacts)
app.add_url_rule('/services/', view_func=pages.services)
app.add_url_rule('/calc/', view_func=pages.calc)

app.add_url_rule('/sitemaps.xml', view_func=sitemap.sitemap_index)

# helpers
app.add_url_rule('/img/<filename>', view_func=helpers.image_view)