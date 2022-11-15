from flask import Flask, render_template, request, jsonify
from routes import *
app = Flask(__name__)
app.register_blueprint(routes)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.qaukrbc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def login():
    return render_template('index.html')



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


