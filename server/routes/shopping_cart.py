from config import app
from server.controllers import shopping_cart

app.add_url_rule('/item/add_to_cart/<id>', view_func=shopping_cart.add_to_cart, methods=['POST'])
app.add_url_rule('/item/remove_from_cart/<id>', view_func=shopping_cart.remove_from_cart,  methods=['POST'], endpoint='shopping_cart:remove_from_cart')
app.add_url_rule('/items/checkout', view_func=shopping_cart.checkout, endpoint='shopping_cart:checkout')
app.add_url_rule('/shopping_cart', view_func=shopping_cart.shopping_cart, endpoint='shopping_cart:shopping_cart')