import json

from flask import Blueprint, Flask, render_template, request, jsonify
from . import routes
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.qaukrbc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@routes.route('/users')
def users():
    return render_template('users.html')

@routes.route("/mypage", methods=["GET"])
def mypage():
    user = db.user.find_one({'id': '장영주'})
    print("/mypage GET >>>>>>>>>>" , user)
    return render_template('mypage.html', user=user)

@routes.route("/mypage", methods=["POST"])
def temp_usermake():
    url_receive = request.form['url_give']
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    doc = {'url': url_receive,
           'id': id_receive,
           'pw': pw_receive}

    db.user.insert_one(doc)
    return render_template('mypage.html')

@routes.route("/mypage", methods=["PATCH"])
def change_image():
    url_receive = request.form['url_give']

    # 로그인기능 생성 후 id 수정필요
    db.user.update_one({'id': "장영주"}, {'$set': {'url': url_receive}})

    return jsonify({'msg':".."});