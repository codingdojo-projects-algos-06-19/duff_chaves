from flask import render_template, request, redirect, session, url_for, flash
from server.models.items import Item

def items():
    print("We're here")
    return render_template('items_list.html')
