from flask import render_template, request, redirect, session, url_for, flash
from server.models.items import Item
from server.models.users import User

def items():
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        return render_template('items_list.html', logged_in_user=logged_in_user)
    else:
        return render_template('items_list.html')
    
def admin_items_list():
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    else:
        logged_in_user = User.query.get(session['user_id'])
        if logged_in_user.approval_id == 9:
            items = Item.query.all()
            print('ITEMS: ', items)
            return render_template('admin_items_list.html', 
                                    logged_in_user=logged_in_user,
                                    items=items
                                    )