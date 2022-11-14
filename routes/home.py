from flask import Blueprint, Flask, render_template, request, jsonify
from . import routes

########### home ###########
@routes.route('/home')
def home():
    return render_template('home.html')


########### home ##########