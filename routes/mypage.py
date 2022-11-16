import json

from flask import Blueprint, Flask, render_template, request, jsonify
from . import routes
from pymongo import MongoClient
import pprint
from bson.son import SON
import certifi

ca = certifi.where()

client = MongoClient(
    'mongodb+srv://Minj:alswoqjffp45@cluster0.7597pmh.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@routes.route("/mypage", methods=["GET"])
def mypage():
    user = db.user.find_one({'id': '장영주'})
    return render_template('mypage.html', user=user)


###  임시_유저생성
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


###  임시_코멘트생성
@routes.route("/temp_comment", methods=["POST"])
def temp_commentMake():
    comment_receive = request.form['comment_give']
    temp = db.comment.find_one({}, sort=[('comment_num', -1)])
    if type(temp) != int:
        max_num = 0
    count = max_num + 1
    # max_num = 0

    # if type(temp) is not int:
    #     pass
    # else:
    #     max_num = temp['comment_num']
    # count = max_num + 1
    doc = {
            'write_num': 4,
            'text': comment_receive,
            'user': '테스투'
        }
    db.comment.insert_one(doc)
    return jsonify({'msg': ".."});

 ###  이미지변경
@ routes.route("/mypage", methods=["PATCH"])
def change_image():
    url_receive = request.form['url_give']

    # 로그인기능 생성 후 id 수정필요
    db.user.update_one({'id': "장영주"}, {'$set': {'url': url_receive}})

    return jsonify({'msg': ".."});


###  임시_글생성
@routes.route("/temp_makeDiray", methods=["POST"])
def temp_makeDiray():
    diary_receive = request.form['diary_give']
    max_num = 0
    temp = db.write.find_one({}, sort=[('write_num', -1)])
    if type(temp) is not int:
        pass
    else:
        max_num = db.write.find_one({}, sort=[('write_num', -1)])['write_num']

    count = max_num + 1

    doc = {
        'write_num': count,
        'user': "테스트",
        'text': diary_receive,
        'good': ["아무개"]
    }
    db.write.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


###  글가져오기
@routes.route("/temp_diary", methods=["GET"])
def diary_get():
    # 로그인 구현 후엔 user명 session에서 받아오도록 수정필요
    user = "장영주"
    diary_list = list(db.write.find({'user': user}, {'_id': False}))
    pipeline = [
        {
            "$lookup": {
                "from": "comment",
                "localField": "write_num",
                "foreignField": "write_num",
                "as": "commentInfo"
            },
        },
        {
            "$project": {
                "_id": 0,
                "user": 1,
                "text": 1,
                "good": 1,
                "write_num": 1,
                "commentInfo": 1,
            }
        }
    ]
    diary_comment_list = list(db.write.aggregate(pipeline))
    for diary_comment in diary_comment_list:
        for comment in diary_comment['commentInfo']:
            if comment.get("_id"):
                comment.pop("_id")
    return jsonify({'diary_comment_list': diary_comment_list})


###  글삭제
@routes.route("/mypage", methods=["DELETE"])
def delete_diary():
    write_num = request.form['num_give']
    user = "장영주"
    db.write.delete_one({'user': user, 'write_num': int(write_num)})
    return jsonify({'msg': '삭제 완료'})


###  좋아요
@routes.route("/mypage/good", methods=["PATCH"])
def good_update():
    good_receive = request.form['user_give']  # "장영주"
    write_num = request.form['num_give']
    good_give = request.form['good_give']  # t or f
    if good_give == 'true':
        db.write.update_one({'write_num': int(write_num)}, {"$push": {'good': good_receive}})
    else:
        db.write.update_one({'write_num': int(write_num)}, {"$pull": {'good': good_receive}})

    # 로그인기능 생성 후 id 수정필요
    # db.user.update_one({'id': "장영주"}, {'$set': {'url': }})

    return jsonify({'msg': ".."});
