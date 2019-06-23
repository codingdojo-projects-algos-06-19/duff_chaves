from config import app
from server.controllers import items

app.add_url_rule('/merch/items', view_func=items.items, endpoint='items:items')
app.add_url_rule('/admin/items', view_func=items.admin_items_list, endpoint='items:admin_items_list')
