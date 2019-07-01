from config import app
from server.controllers import orders

app.add_url_rule('/user/<id>/orders', view_func=orders.user_orders, endpoint='orders:user_orders')
app.add_url_rule('/user/process_checkout', view_func=orders.process_checkout, endpoint='orders:process_checkout')
app.add_url_rule('/user/process_quick_buy/<id>', view_func=orders.process_quick_buy, endpoint='orders:process_quick_buy')
app.add_url_rule('/user/receipt/<id>', view_func=orders.receipt, endpoint='orders:receipt')
app.add_url_rule('/admin/orders', view_func=orders.admin_orders_list, endpoint='orders:admin_orders_list')
