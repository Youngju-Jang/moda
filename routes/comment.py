from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from . import routes

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://Minj:alswoqjffp45@cluster0.7597pmh.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@routes.route('/')
def comment():
    return render_template('comment.html')

@routes.route("/comment", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']
    user_receive = request.form['user_give']

    comment_list = list(db.comment.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num': count,
        'user' : user_receive,
        'comment': comment_receive,
        'done': 0
    }

    db.comment.insert_one(doc)

    return jsonify({'msg': '댓글 등록 완료!!'})

@routes.route("/comment/done", methods=["POST"])
def comment_done():
    cancel_receive = request.form['num_give']
    db.comment.delete_one({'num': int(cancel_receive)})

    return jsonify({'msg': '댓글 삭제 완료 !!'})

@routes.route("/comment", methods=["GET"])
def comment_get():
    comment_list = list(db.comment.find({}, {'_id': False}))

    return jsonify({'comment': comment_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)