from flask import render_template, request, redirect, session, url_for, flash
from config import db, desc
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
        user_orders = Order.query.filter_by(fkey_order_user_id=session['user_id']).all()

        # print('USER_ORDERS: ', user_orders)
        # return ('/user/1/orders')
        # order = Order.query.join(Item, Order.fkey_order_item_id==Item.id).add_columns(Order.id, Order.name, Order.description, Order.img_url, Order.price, Item.first_name, Item.last_name, Order.created_at, Order.updated_at).order_by(desc(Order.id))

        return render_template('user_orders.html', items_of_user=items_of_user, items_in_cart=items_in_cart, logged_in_user=logged_in_user, orders=user_orders)

def admin_orders_list():
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    else:
        logged_in_user = User.query.get(session['user_id'])
        items_of_user = logged_in_user.items_for_cart
        items_in_cart = len(items_of_user)
        if logged_in_user.approval_id == 9:
            orders = Order.query.join(User, Order.fkey_order_user_id==User.id).add_columns(Order.id, Order.amount, User.first_name, User.last_name, Order.created_at, Order.updated_at).order_by(desc(Order.id))
            # orders = Order.query.order_by(desc(Order.id)).all()
            print('ORDERS', orders)
            return render_template('admin_orders_list.html', 
                                    logged_in_user=logged_in_user,
                                    items_in_cart=items_in_cart,
                                    items_of_user=items_of_user,
                                    orders=orders,
                                    )

def process_checkout():
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        # Grab the order id
        create_new_order = Order(fkey_order_user_id=session['user_id'])
        db.session.add(create_new_order)
        db.session.commit()
        last_order = Order.query.order_by(desc(Order.id)).all()
        # Appends the items to the order
        items_of_user = logged_in_user.items_for_cart
        for item in items_of_user:
            last_order.items_for_orders.append(item)
        db.session.commit()
        # Clears the Cart
        logged_in_user.items_for_cart.clear()
        logged_in_user.items_for_cart = []
        db.session.commit()
        return redirect("user/receipt/"+last_order.id)
    else:
        return render_template('page_not_found.html')

def receipt(id):
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        items_of_user = logged_in_user.items_for_cart
        items_in_cart = len(items_of_user)
        current_order = Order.query.get(id)
        items_in_order = current_order.items_for_orders

        # sum_items_in_order = 0
        # for item in items_in_order:
        #     sum_items_in_order += item.price

        order = Order.query.get(id)

        # order_details = Order.query.join(User, Order.fkey_order_user_id==User.id).join(Item, Order.fkey_order_user_id=).add_columns(Order.id, Order.created_at, User.first_name, User.last_name, User.address1, User.address2, User.city, User.country, User.state, User.postal_code).order_by(desc(Order.id))

        return render_template('receipt.html', logged_in_user=logged_in_user, items_of_user=items_of_user, items_in_cart=items_in_cart, items_in_order=items_in_order, order=order)

def process_quick_buy(id):
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        items_of_user = logged_in_user.items_for_cart
        items_in_cart = len(items_of_user)
        if id == 9:
            # Grab the order id
            create_new_order = Order(fkey_order_user_id=session['user_id'], amount=25)
            db.session.add(create_new_order)
            db.session.commit()
            last_order = Order.query.order_by(desc('id')).first()
            # Appends the items to the order
            item = Item.query.get(9)
            last_order.items_for_orders.append(item)
            db.session.commit()
            return redirect("/user/receipt/"+str(last_order.id))
        else:
            logged_in_user = User.query.get(session['user_id'])
            # Grab the order id
            create_new_order = Order(fkey_order_user_id=session['user_id'], amount=50)
            db.session.add(create_new_order)
            db.session.commit()
            last_order = Order.query.order_by(desc('id')).first()
            # Appends the items to the order
            item = Item.query.get(10)
            last_order.items_for_orders.append(item)
            db.session.commit()
            return redirect("/user/receipt/"+str(last_order.id))

    else:
        return render_template('page_not_found.html')
