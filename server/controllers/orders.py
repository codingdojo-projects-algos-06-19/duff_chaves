from flask import render_template, request, redirect, session, url_for, flash
from server.models.orders import Order
from server.models.users import User
from server.models.items import Item

def user_orders(id):
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    else:
        logged_in_user = User.query.get(session['user_id'])
        items_of_user = logged_in_user.items_for_cart
        items_in_cart = len(items_of_user)
        user_orders = Order.query.get(1)
        total = 100
        paid = 0
        subtotal = total - paid
        return render_template('user_orders.html', items_of_user=items_of_user, items_in_cart=items_in_cart, logged_in_user=logged_in_user, total=total, paid=paid, subtotal=subtotal)

def admin_orders_list():
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    else:
        logged_in_user = User.query.get(session['user_id'])
        items_of_user = logged_in_user.items_for_cart
        items_in_cart = len(items_of_user)
        if logged_in_user.approval_id == 9:
            orders = Order.query.all()
            print('ORDERS', orders)
            total = 100
            paid = 0
            subtotal = total - paid
            return render_template('admin_orders_list.html', 
                                    logged_in_user=logged_in_user,
                                    items_in_cart=items_in_cart,
                                    items_of_user=items_of_user,
                                    orders=orders,
                                    total=total, 
                                    paid=paid, 
                                    subtotal=subtotal
                                    )
