from config import app
from server.controllers import tours

app.add_url_rule('/tour', view_func=tours.tours, endpoint='tours:tours')