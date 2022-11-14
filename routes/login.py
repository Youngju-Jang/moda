from flask import Blueprint, Flask, render_template, request, jsonify
from . import routes


########### 로그인 ##########
@routes.route('/login')
def login():
    return render_template('login.html')


########### 로그인 ##########