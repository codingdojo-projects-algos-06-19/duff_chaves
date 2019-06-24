from flask import render_template, request, redirect, session, url_for, flash
from server.models.users import User
from server.models.addresses import Address
from config import bcrypt, db
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
        if len(alerts) == 5:
            flash('All fields are required!')
            # return redirect('/user/register')
            return render_template('/partials/alerts.html'), 500   
        else:
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
        logged_in_user=User.query.get(session['user_id'])
        )

def update(id):
    alerts = []
    current_user = User.query.get(session['user_id'])
    print('CURRENT_USER: ', current_user.email)
    # Check if email is different from database
    if current_user.email == request.form['email']:
        if len(request.form['fname']) < 1:
            alerts.append('The first name field is required!')
        elif request.form['fname'].isalpha() != True:
            alerts.append('Only letters are allowed in the first name field!')

        if len(request.form['lname']) < 1:
            alerts.append('The last name field is required!')
        elif request.form['lname'].isalpha() != True:
            alerts.append('Only letters are allowed in the last name field!')

        if len(request.form['password']) > 0:
            if len(request.form['password']) < 8:
                alerts.append('The password needs to be at least 8 characters')
            elif not re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", request.form['password']):
                alerts.append('The confirmed password must contain a number, a special character, upper and lowercase!')

            if len(request.form['password2']) < 1:
                alerts.append('The confirmed password cannot be blank!')

            if request.form['password'] != request.form['password2']:
                alerts.append('Both passwords should match')
    else:
        get_user_by_email = User.query.filter_by(email=request.form['email']).first()
        if get_user_by_email != None:
            alerts.append('This email address already exists! Please use a different one.')
        else:
            if len(request.form['fname']) < 1:
                alerts.append('The first name field is required!')
            elif request.form['fname'].isalpha() != True:
                alerts.append('Only letters are allowed in the first name field!')

            if len(request.form['lname']) < 1:
                alerts.append('The last name field is required!')
            elif request.form['lname'].isalpha() != True:
                alerts.append('Only letters are allowed in the last name field!')
                
            if len(request.form['email']) < 1:
                alerts.append('The email address field is required!')
            elif not EMAIL_REGEX.match(request.form['email']):
                alerts.append('Invalid email address!')

    if len(alerts) > 0:
        if len(alerts) == 5:
            flash('All fields are required!')
            # return redirect('/user/register')
            return render_template('/partials/alerts.html'), 500   
        else:
            for alert in alerts:
                flash(alert)
            # return redirect('/user/register') 
            return render_template('/partials/alerts.html'), 500
    else:
        user = User.query.get(id)
        # user_address = Address.query.get(user.fkey_user_address_id)
        # print('user_address: ', user_address)
        user.first_name = request.form['fname']
        user.last_name = request.form['lname']
        user.email = request.form['email']

        db.session.commit()
        alerts.append('Your account has been updated!')
        for alert in alerts:
            flash(alert)
            print('ALERTS: ', alert)
        # return redirect('/user/my_account')
        return render_template('/partials/alerts.html', alerts=alerts)


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

def user_list():
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    logged_in_user = User.query.get(session['user_id'])
    user_list = User.query.all()
    if logged_in_user.approval_id == 9:
        return render_template('users_list.html', logged_in_user=logged_in_user, user_list=user_list)
    else:
        return render_template('page_not_found.html', logged_in_user=logged_in_user, user_list=user_list)

def admin_edit(id):
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    logged_in_user = User.query.get(session['user_id'])
    user_to_update = User.query.get(id)
    if logged_in_user.approval_id == 9:
        return render_template('admin_user_edit.html', logged_in_user=logged_in_user, user=user_to_update)
    else:
        return render_template('page_not_found.html', logged_in_user=logged_in_user, user_list=user_list)

def admin_update(id):
    alerts = []
    user_to_update = User.query.get(id)
    print('users_to_update: ', user_to_update )
    # return ('/admin/users')

    # Check if email is different from database
    if user_to_update.email == request.form['email']:
        print('1user_to_update.email: ', user_to_update.email, '||', request.form['email'])
        if len(request.form['fname']) < 1:
            alerts.append('The first name field is required!')
        elif request.form['fname'].isalpha() != True:
            alerts.append('Only letters are allowed in the first name field!')

        if len(request.form['lname']) < 1:
            alerts.append('The last name field is required!')
        elif request.form['lname'].isalpha() != True:
            alerts.append('Only letters are allowed in the last name field!')

        if len(alerts) > 0:
            if len(alerts) == 5:
                flash('All fields are required!')
                # return redirect('/user/register')
                return render_template('/partials/alerts.html'), 500   
            else:
                for alert in alerts:
                    flash(alert)
                #return redirect('/admin/users') 
                return render_template('/partials/alerts.html'), 500
        else:
            print('2user_to_update.email: ', user_to_update.email, '||', request.form['email'])
            user = User.query.get(id)
            user.first_name = request.form['fname']
            user.last_name = request.form['lname']
            user.email = request.form['email']
            db.session.commit()
            # flash('Saving the user account!')
            # for alert in alerts:
            #     flash(alert)
            # return redirect('/admin/users')
            return render_template('/partials/alerts.html', alerts=alerts)

    else:
        get_user_by_email = User.query.filter_by(email=request.form['email']).first()
        if get_user_by_email != None:
            alerts.append('The email address already exists!')
        else:
            if len(request.form['fname']) < 1:
                alerts.append('The first name field is required!')
            elif request.form['fname'].isalpha() != True:
                alerts.append('Only letters are allowed in the first name field!')

            if len(request.form['lname']) < 1:
                alerts.append('The last name field is required!')
            elif request.form['lname'].isalpha() != True:
                alerts.append('Only letters are allowed in the last name field!')
                
            if len(request.form['email']) < 1:
                alerts.append('The email address field is required!')
            elif not EMAIL_REGEX.match(request.form['email']):
                alerts.append('Invalid email address!')

    if len(alerts) > 0:
        if len(alerts) == 5:
            flash('All fields are required!')
            # return redirect('/user/register')
            return render_template('/partials/alerts.html'), 500   
        else:
            for alert in alerts:
                flash(alert)
            #return redirect('/admin/users') 
            return render_template('/partials/alerts.html'), 500
    else:
        alerts=[]
        user = User.query.get(id)
        user.first_name = request.form['fname']
        user.last_name = request.form['lname']
        user.email = request.form['email']
        db.session.commit()
        # alerts.append('The user account has been updated!')
        # for alert in alerts:
        #     flash(alert)
        return render_template('/partials/alerts.html', alerts=alerts)
        # return redirect('/admin/users')


