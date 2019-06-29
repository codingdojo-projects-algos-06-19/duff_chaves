from config import app
from server.controllers import items

app.add_url_rule('/merch/items', view_func=items.items, endpoint='items:items')
app.add_url_rule('/admin/items', view_func=items.admin_items_list, endpoint='items:admin_items_list')
app.add_url_rule('/admin/add/items', view_func=items.admin_add_items, endpoint='items:admin_add_items')
app.add_url_rule('/admin/item/create', view_func=items.admin_item_create, methods=['POST'], endpoint='items:admin_item_create')
app.add_url_rule('/admin/item/<id>/edit', view_func=items.admin_item_edit, endpoint='items:admin_item_edit')
app.add_url_rule('/admin/item/update/<id>', view_func=items.admin_item_update, methods=['POST'], endpoint='items:admin_item_update')
app.add_url_rule('/admin/item/<id>/delete', view_func=items.admin_item_delete, methods=['POST'], endpoint='items:admin_item_delete')
# app.add_url_rule('/item/remove_from/<id>', view_func=items.remove_from,  methods=['POST'])
app.add_url_rule('/item/view/<id>', view_func=items.view, endpoint='items:view')
app.add_url_rule('/items/quick-buy', view_func=items.quick_buy, endpoint='items:quick_buy')