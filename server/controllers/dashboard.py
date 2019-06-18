from flask import render_template, request, redirect, url_for, session, flash
from server.models.users import User

def page_not_found(error):
    return render_template('page_not_found.html',
        user_list=User.query.all(),
        logged_in_user=User.query.get(session['user_id'])
    ), 404

def index():
    if 'user_id' in session:
        return render_template(
            'index.html',
            user_list=User.query.all(),
            logged_in_user=User.query.get(session['user_id'])
        )
    else:
        return render_template('index.html')
