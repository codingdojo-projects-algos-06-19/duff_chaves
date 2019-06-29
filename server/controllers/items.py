from flask import render_template, request, redirect, session, url_for, flash
from config import db, IntegrityError, desc
from server.models.items import Item
from server.models.users import User
import stripe

def items():
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        items = Item.query.join(User, Item.fkey_item_user_id==User.id).add_columns(Item.id, Item.name, Item.description, Item.img_url, Item.price, User.first_name, User.last_name, Item.created_at, Item.updated_at).order_by(desc(Item.id))
        items_of_user = logged_in_user.items_for_cart
        items_in_cart = len(items_of_user)
        return render_template('items_list.html', logged_in_user=logged_in_user, items=items, items_in_cart=items_in_cart, items_of_user=items_of_user)
    else:
        return render_template('items_list.html')

def quick_buy():
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        items = Item.query.join(User, Item.fkey_item_user_id==User.id).add_columns(Item.id, Item.name, Item.description, Item.img_url, Item.price, User.first_name, User.last_name, Item.created_at, Item.updated_at).order_by(desc(Item.id))
        items_of_user = logged_in_user.items_for_cart
        items_in_cart = len(items_of_user)
        return render_template('quick_buy.html', logged_in_user=logged_in_user, items=items, items_in_cart=items_in_cart, items_of_user=items_of_user)
    else:
        flash('Please sign-in or register to proceed!')
        return render_template('/quick-buy')

# def remove_from(id):
#     removeUser = User.query.get(session['user_id'])
#     removeItem = Item.query.get(id)
#     removeUser.items_for_cart.remove(removeItem)
#     try:
#         db.session.commit()
#         # return render_template('/partials/alerts-info.html')
#         return redirect('/item/view/'+id)
#     except IntegrityError:
#         db.session.rollback()
#         return render_template('/partials/alerts.html')

def view(id):
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        item = Item.query.get(id)
        # item_in_cart = logged_in_user.items_for_cart
        # item_in_cart = User.query.filter(User.items_for_cart.any(id=id)).filter_by()
        items_of_user = logged_in_user.items_for_cart
        items_in_cart = len(items_of_user)

        return render_template('item_view.html', logged_in_user=logged_in_user, item=item, items_of_user=items_of_user, items_in_cart=items_in_cart)
    else:
        return render_template('item_view.html') 

def admin_items_list():
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    else:
        logged_in_user = User.query.get(session['user_id'])
        items_of_user = logged_in_user.items_for_cart
        items_in_cart = len(items_of_user)
        if logged_in_user.approval_id == 9:
            itemList = Item.query.join(User, Item.fkey_item_user_id==User.id).add_columns(Item.id, Item.name, Item.description, Item.img_url, Item.price, User.first_name, User.last_name, Item.created_at, Item.updated_at).order_by(desc(Item.id))
            # items = User.query.join(Item.fkey_item_user_id)
            # print('ITEMS: ', itemList)
            # for item in itemList:
            #     print(item)
            return render_template('admin_items_list.html', 
                                    logged_in_user=logged_in_user,
                                    items=itemList,
                                    items_of_user=items_of_user,
                                    items_in_cart=items_in_cart
                                    )

def admin_add_items():
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    logged_in_user = User.query.get(session['user_id'])
    items_of_user = logged_in_user.items_for_cart
    items_in_cart = len(items_of_user)
    if logged_in_user.approval_id == 9:
        return render_template('admin_add_items.html', items_of_user=items_of_user, logged_in_user=logged_in_user, items_in_cart=items_in_cart)
    else:
        return render_template('page_not_found.html', items_of_user=items_of_user, logged_in_user=logged_in_user, items_in_cart=items_in_cart)

def admin_item_create():
    alerts = []
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    logged_in_user = User.query.get(session['user_id'])
    items_of_user = logged_in_user.items_for_cart
    items_in_cart = len(items_of_user)
    if logged_in_user.approval_id == 9:
        if len(request.form['name']) < 1:
            alerts.append('Please enter an item name!')

        if len(request.form['category']) < 1:
            alerts.append('Please choose a category!')
        
        if len(request.form['price']) < 1:
            alerts.append('Please enter a price!')

        if len(request.form['description']) < 1:
            alerts.append('Please enter an item description!')

        if len(request.form['img_url']) < 1:
            alerts.append('Please enter the image URL!')

        if len(alerts) > 0:
            if len(alerts) == 5:
                flash('All fields are required!')
                return render_template('/partials/alerts.html'), 500   
            else:
                for alert in alerts:
                    flash(alert)
                return render_template('/partials/alerts.html'), 500
    
        new_item = Item(
            name = request.form['name'],
            category = request.form['category'],
            price = request.form['price'],
            description = request.form['description'],
            img_url = request.form['img_url'],
            fkey_item_user_id = request.form['admin_user_id']
        )
        print(new_item)
        db.session.add(new_item)
        db.session.commit()
        # flash('The item has been added!')
        return render_template('/partials/alerts.html', alerts=alerts, items_of_user=items_of_user,items_in_cart=items_in_cart)
    else:  
        return render_template('page_not_found.html', logged_in_user=logged_in_user)

def admin_item_edit(id):
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    logged_in_user = User.query.get(session['user_id'])
    items_of_user = logged_in_user.items_for_cart
    items_in_cart = len(items_of_user)
    if logged_in_user.approval_id == 9:
        item = Item.query.get(id)
        return render_template('admin_item_edit.html', logged_in_user=logged_in_user, item=item, items_of_user=items_of_user, items_in_cart=items_in_cart)
    else:
        return render_template('page_not_found.html', items_in_cart=items_in_cart, logged_in_user=logged_in_user, items_of_user=items_of_user)

def admin_item_update(id):
    alerts = []
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    logged_in_user = User.query.get(session['user_id'])
    if logged_in_user.approval_id == 9:
        if len(request.form['name']) < 1:
            alerts.append('Please enter a item name!')

        if len(request.form['category']) < 1:
            alerts.append('Please choose a category!')
        
        if len(request.form['price']) < 1:
            alerts.append('Please enter a price!')

        if len(request.form['description']) < 1:
            alerts.append('Please enter a item description!')
        
        if len(alerts) > 0:
            if len(alerts) == 5:
                flash('All fields are required!')
                return render_template('/partials/alerts.html'), 500   
            else:
                for alert in alerts:
                    flash(alert)
                return render_template('/partials/alerts.html'), 500

        item = Item.query.get(id)
        print(request.form['category'])
        item.name = request.form['name']
        item.category = request.form['category']
        item.price = request.form['price']
        item.description = request.form['description']
        item.img_url = request.form['img_url']
        db.session.commit()

        # alerts.append('The item has been updated!')
        # for alert in alerts:
        #     flash(alert)
        #     print('ALERTS: ', alert)
        return render_template('/partials/alerts-info.html')
    else:
        return render_template('page_not_found.html', logged_in_user=logged_in_user)

def admin_item_delete(id):
    item_instance_to_delete = Item.query.get(id)
    db.session.delete(item_instance_to_delete)
    db.session.commit()
    # flash('The tour record has been deleted!')
    # return redirect('/admin/tours')
    return render_template('/partials/alerts-info.html')


    