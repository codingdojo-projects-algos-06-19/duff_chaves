from config import app
from server.controllers import songs

app.add_url_rule('/listen', view_func=songs.records, endpoint='songs:records')