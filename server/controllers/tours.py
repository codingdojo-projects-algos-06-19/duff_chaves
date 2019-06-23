from flask import render_template, request, redirect, session, url_for, flash
from server.models.tours import Tour
from server.models.users import User

def tours():
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        tours = Tour.query.all()
        return render_template('tours.html', logged_in_user=logged_in_user, tours=tours)
    else:
        tours = Tour.query.all()
        return render_template('tours.html', tours=tours)

def admin_items_list():
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    else:
        logged_in_user = User.query.get(session['user_id'])
        if logged_in_user.approval_id == 9:
            tours = Tour.query.all()
            print('TOURS: ', tours)
            return render_template('admin_tours_list.html', 
                                    logged_in_user=logged_in_user,
                                    tours=tours
                                    )