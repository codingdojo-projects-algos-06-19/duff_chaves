from config import app
from server.controllers import tours

app.add_url_rule('/tour', view_func=tours.tours, endpoint='tours:tours')
app.add_url_rule('/admin/tours', view_func=tours.admin_items_list, endpoint='tours:admin_items_list')
