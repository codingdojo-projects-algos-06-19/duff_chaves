from flask import render_template, request, redirect, session, url_for, flash
from config import desc
from server.models.users import User
from server.models.items import Item
import soundcloud

def records():
    items = Item.query.filter_by(category='Songs')
    if 'user_id' in session:
        logged_in_user = User.query.get(session['user_id'])
        items_of_user = logged_in_user.items_for_cart
        items_in_cart = len(items_of_user)
        for song  in items:
            print('SONG: ', song)
        return render_template('records.html', logged_in_user=logged_in_user, items_in_cart=items_in_cart, items_of_user=items_of_user, items=items)
    else:
        return render_template('records.html', items=items)

def play():
    client = soundcloud.Client(client_id='FvkgucGq5QyPAepKyYOUkjEQq2zLVKPb')
    track = client.get('/tracks/71267955')
    stream_url = client.get(track.stream_url, allow_redirects=False)
    player_html = stream_url.location
    return player_html
