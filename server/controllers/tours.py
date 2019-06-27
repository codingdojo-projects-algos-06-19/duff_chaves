from flask import render_template, request, redirect, session, url_for, flash
from config import db, IntegrityError, desc, func
from server.models.tours import Tour
from server.models.users import User
from datetime import datetime

def tours():
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        tours = Tour.query.all()
        return render_template('tours.html', logged_in_user=logged_in_user, tours=tours)
    else:
        tours = Tour.query.all()
        return render_template('tours.html', tours=tours)

def admin_tours_list():
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    else:
        logged_in_user = User.query.get(session['user_id'])
        if logged_in_user.approval_id == 9:
            tours = Tour.query.order_by(desc(Tour.id))
            print('TOURS: ', tours)
            return render_template('admin_tours_list.html', 
                                    logged_in_user=logged_in_user,
                                    tours=tours
                                    )
def admin_add_tours():
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    logged_in_user = User.query.get(session['user_id'])
    if logged_in_user.approval_id == 9:
        return render_template('admin_add_tours.html', logged_in_user=logged_in_user)
    else:
        return render_template('page_not_found.html', logged_in_user=logged_in_user)

def admin_tour_create():
    alerts = []
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    logged_in_user = User.query.get(session['user_id'])
    if logged_in_user.approval_id == 9:
        if len(request.form['event_date']) < 1:
            alerts.append('Please enter an event date!')

        if len(request.form['venue_name']) < 1:
            alerts.append('Please enter a venue name!')
        
        if len(request.form['venue_phone']) < 1:
            alerts.append('Please enter a phone number!')

        if len(request.form['venue_address']) < 1:
            alerts.append('Please enter an address!')
        
        if len(request.form['venue_city']) < 1:
            alerts.append('Please enter a city!')

        if len(request.form['venue_state']) < 1:
            alerts.append('Please enter a state!')

        if len(request.form['venue_country']) < 1:
            alerts.append('Please choose a country!')

        if len(request.form['event_img']) < 1:
            alerts.append('Please enter the image URL!')
        
        if len(alerts) > 0:
            if len(alerts) == 6:
                flash('All fields are required!')
                return render_template('/partials/alerts.html'), 500   
            else:
                for alert in alerts:
                    flash(alert)
                return render_template('/partials/alerts.html'), 500
        event_date = request.form['event_date']
        event_date = datetime.strptime(event_date, "%Y-%m-%d")
        # print('EVENT_DATE: ', request.form['event_date'])
        # y, m, d = event_date.split('-')
        # event_date = datetime.datetime(int(y), int(m), int(d))
        
        new_tour = Tour(
            event_date = event_date,
            venue_phone = request.form['venue_phone'],
            venue_name = request.form['venue_name'],
            venue_address = request.form['venue_address'],
            venue_city = request.form['venue_city'],
            venue_state = request.form['venue_state'],
            venue_country = request.form['venue_country'],
            event_img = request.form['event_img']
        )
        print(new_tour)
        db.session.add(new_tour)
        db.session.commit()
        return render_template('/partials/alerts.html', alerts=alerts)
    else:
        return render_template('page_not_found.html', logged_in_user=logged_in_user)

def admin_tour_edit(id):
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    logged_in_user = User.query.get(session['user_id'])
    if logged_in_user.approval_id == 9:
        tour = Tour.query.get(id)
        return render_template('admin_tour_edit.html', logged_in_user=logged_in_user, tour=tour)
    else:
        return render_template('page_not_found.html', logged_in_user=logged_in_user)

def admin_tour_update(id):
    alerts = []
    if 'user_id' not in session:
        return render_template('page_not_found.html')
    logged_in_user = User.query.get(session['user_id'])
    if logged_in_user.approval_id == 9:
        if len(request.form['event_date']) < 1:
            alerts.append('Please enter an event date!')

        if len(request.form['venue_name']) < 1:
            alerts.append('Please enter a venue name!')
        
        if len(request.form['venue_phone']) < 1:
            alerts.append('Please enter a phone number!')

        if len(request.form['venue_address']) < 1:
            alerts.append('Please enter an address!')
        
        if len(request.form['venue_city']) < 1:
            alerts.append('Please enter a city!')

        if len(request.form['venue_state']) < 1:
            alerts.append('Please enter a state!')

        if len(request.form['venue_country']) < 1:
            alerts.append('Please choose a country!')

        if len(request.form['event_img']) < 1:
            alerts.append('Please enter the image URL!')        
        if len(alerts) > 0:
            if len(alerts) == 5:
                flash('All fields are required!')
                return render_template('/partials/alerts.html'), 500   
            else:
                for alert in alerts:
                    flash(alert)
                return render_template('/partials/alerts.html'), 500
        # event_date = request.form['event_date']
        # event_date = datetime.strptime(event_date, "%Y-%m-%d %H:%M:%S").date()
        event_date = request.form['event_date']
        event_date = func.datetime.strptime(event_date, "%Y-%m-%d %M:%S:")
        # event_time = request.form['event_time']
        # event_date = datetime.strptime(event_date,"%Y-%m-%d %H:%M:%S")

        # print('EVENT_DATE: ', event_date, request.form)
        tour = Tour.query.get(id)
        tour.venue_phone = request.form['venue_phone'],
        tour.venue_name = request.form['venue_name'],
        tour.event_date = event_date,
        tour.venue_address = request.form['venue_address'],
        tour.venue_city = request.form['venue_city'],
        tour.venue_state = request.form['venue_state'],
        tour.venue_country = request.form['venue_country'],
        tour.event_img = request.form['event_img']
        db.session.commit()

        # alerts.append('The tour has been updated!')
        # for alert in alerts:
        #     flash(alert)
        #     print('ALERTS: ', alert)
        return render_template('/partials/alerts-info.html')
    else:
        return render_template('page_not_found.html', logged_in_user=logged_in_user)

def admin_tour_delete(id):
    tour_instance_to_delete = Tour.query.get(id)
    db.session.delete(tour_instance_to_delete)
    db.session.commit()
    # flash('The tour record has been deleted!')
    # return redirect('/admin/tours')
    return render_template('/partials/alerts-info.html')