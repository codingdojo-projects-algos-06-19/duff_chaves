from flask import render_template, session
from config import app
from server.controllers import dashboard
from server.models.users import User

@app.errorhandler(404)
def page_not_found(error):
    if 'user_id' in session:
        return render_template('page_not_found.html',
        user_list=User.query.all(),
        logged_in_user=User.query.get(session['user_id'])
    ), 404
    else:
        return render_template('page_not_found.html',
    ), 404

app.add_url_rule('/', view_func=dashboard.index, endpoint='index')