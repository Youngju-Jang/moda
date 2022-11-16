from flask import Blueprint, Flask, render_template, request, jsonify
from . import routes

import certifi
ca = certifi.where()

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.bckltib.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

########### home ###########
@routes.route('/home')
def home():
    return render_template('home.html')

@routes.route("/home", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']

    doc={
        'name': name_receive,
    }
    db.home.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})

@routes.route("/home", methods=["GET"])
def web_mars_get():
    order_list = list(db.home.find({}, {'_id': False}))
    return jsonify({'orders': order_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
########### home ##########