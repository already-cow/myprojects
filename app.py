from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

## pymongo 사용코드
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 파일 연결
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


# 주문 목록보기(Read) API
@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)