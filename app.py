from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.qaukrbc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

########### 로그인 ##########
@app.route('/login')
def home():
    return render_template('login.html')


########### 로그인 ##########
########### home ##########
@app.route('/home')
def home():
    return render_template('home.html')


########### home ##########
########### 마이페이지 ##########
@app.route("/mypage", methods=["GET"])
def movie_get():
    movie_list = list(db.movies.find({},{'_id':False}))
    # return jsonify({'movies': movie_list})
    return render_template('mypage.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)