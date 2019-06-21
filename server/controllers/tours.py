from flask import render_template, request, redirect, session, url_for, flash
from server.models.tours import Tour

def tours():
    return render_template('tours.html')