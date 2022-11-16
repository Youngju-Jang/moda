from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from . import routes

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://Minj:alswoqjffp45@cluster0.7597pmh.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@routes.route('/comment')
def comment():
    return render_template('comment.html')

## 코멘트 입력값 가져오기
@routes.route("/comment/comment1", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']
    user_receive = request.form['user_give']

    write_num = db.comment.find_one({'num': 'bobby'})
    max_num = db.comment_test.find_one({}, sort=[('comment_num', -1)])['comment_num']

    # max_num = 0
    #
    # if type(num) is not int:
    #     pass
    # else:
    #     max_num = num['comment_num']

    # count = max_num + 1
    if len(max_num) == 0:
        max_num = 0
    count = max_num + 1

    # max_num = 0
    # temp = db.comment_test.find_one({}, sort=[('comment_num', -1)])
    # if type(temp) is not int:
    #     pass
    # else:
    #     max_num = db.comment_test.find_one({}, sort=[('comment_num', -1)])['comment_num']
    #
    # count = int(max_num) + 1

    doc = {
        # 'write_num' : num,
        'comment_num': count,
        'user' : user_receive,
        'comment': comment_receive,
    }

    db.comment_test.insert_one(doc)

    return jsonify({'msg': '댓글 등록 완료!!'})

## 코멘트 삭제 하기
@routes.route("/comment/done", methods=["POST"])
def comment_done():
    cancel_receive = request.form['num_give']
    db.comment_test.delete_one({'comment_num': int(cancel_receive)})

    return jsonify({'msg': '댓글 삭제 완료 !!'})


## 댓글 정보 요청하기
@routes.route("/comment/comment1", methods=["GET"])
def commment_get():

    comment_list = list(db.comment_test.find({},{'_id':False}))


    return jsonify({'comment': comment_list})


## 게시물 정보 요청하기
@routes.route("/comment/comment2", methods=["GET"])
def text_get():

    text_list = list(db.comment.find({}, {'_id': False}))

    return jsonify({'text': text_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)