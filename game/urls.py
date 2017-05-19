from game.views import *

def setup_routes(app):
    app.router.add_get('/', index)