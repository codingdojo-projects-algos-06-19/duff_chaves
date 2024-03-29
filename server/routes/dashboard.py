from flask import render_template, session
from config import app
from server.controllers import dashboard
from server.models.items import Item
from server.models.users import User

@app.errorhandler(404)
def page_not_found(error):
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        item = Item.query.all()
        items_of_user = logged_in_user.items_for_cart
        items_in_cart = len(items_of_user)
        return render_template('page_not_found.html',
            user_list=User.query.all(),
            logged_in_user=logged_in_user,
            items_in_cart=items_in_cart,
            items_of_user=items_of_user
        ), 404
    else:
        return render_template('page_not_found.html',
    ), 404

app.add_url_rule('/404', view_func=dashboard.page_not_found, endpoint='dashboard:page_not_found')
app.add_url_rule('/', view_func=dashboard.index, endpoint='dashboard:index')
app.add_url_rule('/player', view_func=dashboard.player, endpoint='dashboard:player')