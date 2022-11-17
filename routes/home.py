from flask import Blueprint, Flask, render_template, request, jsonify
from . import routes

import certifi
ca = certifi.where()

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.qaukrbc.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.moda

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

########### home ###########
@routes.route('/home')
def home():
    return render_template('home.html')

@routes.route("/home", methods=["POST"])
def web_mars_post():
    text_receive = request.form['text_give']
    user_receive = request.form['user_give']

    max_num = 0
    temp = db.write.find_one({}, sort=[('write_num', -1)])
    if temp is None:
        pass
    else:
        max_num = db.write.find_one({}, sort=[('write_num', -1)])['write_num']

    count = max_num + 1


    doc={
        'text': text_receive,
        'write_num': count,
        'user': user_receive,
        'good': []

    }
    db.write.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})

@routes.route("/home2", methods=["GET"])
def web_mars_get():
    order_list = list(db.write.find({}, {'_id': False}))
    return jsonify({'orders': order_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
########### home ##########