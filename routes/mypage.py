from flask import Blueprint, Flask, render_template, request, jsonify
from . import routes

@routes.route('/users')
def users():
    return render_template('users.html')

@routes.route("/mypage", methods=["GET"])
def mypage():
    return render_template('mypage.html')

@routes.route("/mypage", methods=['PATCH'])
def change_image():
    print(">>>>>>>>>>>>>>", request.form)
    form_receive = request.form['form_give']
    print(form_receive)
    return render_template('mypage.html')