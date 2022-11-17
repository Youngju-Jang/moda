from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from . import routes

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.qaukrbc.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.moda


@routes.route('/comment')
def comment():
    num = request.args.get('num_give')
    return render_template('comment.html', num=num)

## 코멘트 입력값 가져오기
@routes.route("/comment/comment1", methods=["POST"])
def comment_post():

    comment_receive = request.form['comment_give']
    user_receive = request.form['user_give']
    num_receive = request.form['num_give']
    temp = db.comment.find_one({'write_num':int(num_receive)}, sort=[('comment_num', -1)])
    max_num = 0

    if temp is None:
        pass
    else:
        max_num = temp['comment_num']

    count = max_num + 1
    print(">>>>>>>>>>", temp)

    doc = {
        'write_num' : int(num_receive),
        'comment_num': count,
        'user' : user_receive,
        'comment': comment_receive,
    }

    db.comment.insert_one(doc)

    return jsonify({'msg': '댓글 등록 완료!!'})

## 코멘트 삭제 하기
@routes.route("/comment/done", methods=["POST"])
def comment_done():
    cancel_receive = request.form['num_give']
    db.comment.delete_one({'comment_num': int(cancel_receive)})

    return jsonify({'msg': '댓글 삭제 완료 !!'})


## 댓글 정보 요청하기
@routes.route("/comment/comment1", methods=["GET"])
def commment_get():
    num_receive = request.args.get('num_give')

    comment_list = list(db.comment.find({'write_num': int(num_receive)},{'_id':False}))


    return jsonify({'comment': comment_list})



# 게시물 정보 요청하기
@routes.route("/comment/comment2", methods=["GET"])
def text_get():
    num_receive = request.args.get('num_give')

    text_list = list(db.write.find({'write_num': int(num_receive)}, {'_id': False}))

    return jsonify({'text': text_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)