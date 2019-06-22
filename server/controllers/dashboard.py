from flask import render_template, request, redirect, url_for, session, flash
from server.models.users import User
import soundcloud

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

def player():
    # #Widget
    # # create a client object with your app credentials
    # client = soundcloud.Client(client_id='mwf9M1cPL64iKzy3wUUKSwTDmEyJshra')

    # # get a tracks oembed data
    # track_url = 'https://soundcloud.com/forss/flickermood'
    # embed_info = client.get('/oembed', url=track_url)

    # # print the html for the player widget
    # print (embed_info['html'])
    # player_html = embed_info['html']
    # return player_html

    # create a client object with your app credentials
    client = soundcloud.Client(client_id='FvkgucGq5QyPAepKyYOUkjEQq2zLVKPb')
    # fetch track to stream
    track = client.get('/tracks/71267955')
    #track = client.get('/sets/casting-crows')
    # get the tracks streaming URL
    stream_url = client.get(track.stream_url, allow_redirects=False)
    # print the tracks stream URL
    # print (stream_url.location)
    player_html = stream_url.location

    return player_html
