from flask import render_template, request, redirect, session, url_for, flash
from server.models.users import User
from config import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def register():
    if 'user_id' not in session:
        return render_template('register.html')
    else:
        return redirect('/')

def create():
    # @A1aaaaa
    alerts = User.validate(request.form)
    if len(alerts) > 0:
        print(len(alerts))
        if len(alerts) == 5:
            print(len(alerts))
            flash('All fields are required!')
            # return redirect('/user/register')
            return render_template('/partials/alerts.html'), 500   
        else:
            print(len(alerts))
            for alert in alerts:
                flash(alert)
            # return redirect('/user/register') 
            return render_template('/partials/alerts.html'), 500
    else:
        user_id = User.create(request.form)
        session['user_id'] = user_id
        return redirect('/user/thankyou')

def thankyou():
    if 'user_id' not in session:
        return render_template('register.html')
    else:
        return render_template('thankyou.html', 
        user_list=User.query.all(), 
        logged_in_user=User.query.get(session['user_id'])
        )

def login():
    if 'user_id' in session:
        print('SESSION_ID: ', session['user_id'])
        return render_template('welcome.html', 
        user_list=User.query.all(), 
        logged_in_user=User.query.get(session['user_id'])
        )
    else:
        return render_template('login.html')

def my_account():
    if 'user_id' not in session:
        return render_template('login.html', 
        user_list=User.query.all())
    else:
        return render_template('my_account.html', 
        user_list=User.query.all(), 
        logged_in_user=User.query.get(session['user_id'])
        )

def process_login():
    alerts=[]
    # @A1aaaaa
    if len(request.form['email']) < 1:
        alerts.append('Please enter a email address')
    elif not EMAIL_REGEX.match(request.form['email']):
        alerts.append('Invalid email address!')
    if len(request.form['password']) < 1:
        alerts.append('Please enter a password')

    if len(alerts) > 0:
        for alert in alerts:
            flash(alert)
            print(alert)
        # return redirect('/user/login')
        return render_template('/partials/alerts.html'), 500

    get_user_by_email = User.query.filter_by(email=request.form['email']).first()
    #print('get_user_by_email', get_user_by_email)
    if get_user_by_email  != None:
        user = get_user_by_email
        if bcrypt.check_password_hash(user.password,request.form['password']):
            session['user_id'] = user.id
            session['user_full_name'] = user.first_name + ' ' + user.last_name
            logged_in_user = User.query.get(session['user_id'])
            return redirect('/user/welcome')
            # return render_template('welcome.html', 
            #         user_list=User.query.all(), 
            #         logged_in_user=logged_in_user)
                #return redirect('/welcome')
    flash('The email or password is incorrect!')
    # return redirect('/user/login')
    return render_template('/partials/alerts.html'), 500

def welcome():
    if 'user_id' not in session:
       return redirect('/user/login')
    print('session user id: ', session['user_id'])
    return render_template('welcome.html', 
    user_list=User.query.all(), 
    logged_in_user=User.query.get(session['user_id']))

def logout():
    alerts = []
    session.pop('user_id', None)
    #alerts = flash('Thanks for using our site!')
    return redirect('login')

