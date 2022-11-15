from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://Minj:alswoqjffp45@cluster0.7597pmh.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('comment.html')

@app.route("/comment", methods=["POST"])
def bucket_post():
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

    return jsonify({'msg': 'POST(기록) 연결 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST(완료) 연결 완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)