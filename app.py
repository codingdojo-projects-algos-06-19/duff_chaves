from config import app, db
from server.routes import users, dashboard, items, tours, songs, orders, shopping_cart
# from server.models import items, orders, users, addresses, tours, orders_items


if __name__ == "__main__":
    app.run(debug=True)