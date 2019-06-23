from config import app
from server.controllers import orders

app.add_url_rule('/user/<id>/orders', view_func=orders.user_orders, endpoint='orders:user_orders')
app.add_url_rule('/admin/orders', view_func=orders.admin_orders_list, endpoint='orders:admin_orders_list')
