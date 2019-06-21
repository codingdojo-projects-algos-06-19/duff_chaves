from flask import render_template, request, redirect, session, url_for, flash

def records():
    return render_template('records.html')