from flask import render_template, request, redirect, session, url_for, flash
from server.models.items import Item
from server.models.users import User
from config import db, desc, IntegrityError
from sqlalchemy.sql import func

# def shopping_cart():
#     if 'user_id' in session:
#         logged_in_user = User.query.get(session['user_id'])
#         items_of_user = logged_in_user.items_for_cart
#         items_in_cart = len(items_of_user)
#         return render_template('shopping_cart.html', items_in_cart=items_in_cart, logged_in_user=logged_in_user, items_of_user=items_of_user)
#     else:
#         return render_template('shopping_cart.html')

def add_to_cart(id):
    alerts = []
    logged_in_user = User.query.get(session['user_id'])
    # item = Item.query.get(id)
    item = Item.query.filter_by(id=request.form["add-cart-item-id"]).first_or_404()
    items_of_user = logged_in_user.items_for_cart
    item.users_for_cart.append(logged_in_user)
    url_referrer = request.referrer
    try:
        db.session.commit()
        hide_add_button = 'none'

        # for item in items_of_user:
        #     if items_of_user.id == id:
        #         print('== id',request.form["add-cart-item-id"], item)
        #         hide_add_button = 'none'
        #         hide_remove_button = 'block'
        #     else:
        #         print('items of user != id', item)
        #         hide_add_button = 'none'
        #         hide_remove_button = 'block'
        alerts.append('Item added to cart!')
        if url_referrer == 'http://localhost:5000/listen':
            return redirect('/listen')
        return redirect('/item/view/'+id)
        # return render_template('/partials/alerts-info.html')
        # return redirect(url_for('items:view', id=id, hide_add_button=hide_add_button))
        # return url_for('items:view', hide_add_button=hide_add_button)   #edirect('/item/view/'+id)
    except IntegrityError:
        db.session.rollback()
        return redirect('/item/view/'+id)
        # return render_template('/partials/alerts.html')
        


def remove_from_cart(id):
    logged_in_user = User.query.get(session['user_id'])
    removeItem = Item.query.get(id)
    logged_in_user.items_for_cart.remove(removeItem)
    url_referrer = request.referrer
    try:
        db.session.commit()
        # return render_template('/partials/alerts-info.html')
        if url_referrer == 'http://localhost:5000/items/checkout':
            return redirect('/items/checkout')
        elif url_referrer == 'http://localhost:5000/listen':
            return redirect('/listen')
        return redirect('/item/view/'+id)
    except IntegrityError:
        db.session.rollback()
        return render_template('/partials/alerts.html')


def shopping_cart():
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        items = Item.query.join(User, Item.fkey_item_user_id==User.id).add_columns(Item.id, Item.name, Item.description, Item.img_url, Item.price, User.first_name, User.last_name, Item.created_at, Item.updated_at).order_by(desc(Item.id))
        items_of_user = logged_in_user.items_for_cart
        items_in_cart = len(items_of_user)
        sum_items_in_cart = 0
        for item in items_of_user:
            sum_items_in_cart += item.price
        return render_template('shopping_cart.html', items_of_user=items_of_user, items_in_cart=items_in_cart, logged_in_user=logged_in_user, items=items, sum_items_in_cart=sum_items_in_cart)
    else:
        return render_template('page_not_found.html')
