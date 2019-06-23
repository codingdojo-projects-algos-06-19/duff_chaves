from flask import render_template, request, redirect, session, url_for, flash
from server.models.users import User

def records():
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        return render_template('records.html', logged_in_user=logged_in_user)
    else:
        return render_template('records.html')
