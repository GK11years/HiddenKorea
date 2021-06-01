from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def hello():
    with open('./data/naver_keyword.json', 'r', encoding='utf8') as f:
        naver_blog = json.load(f)
        print(naver_blog)
    return naver_blog

# @app.route('/user/<name>')
# def user(name):
# 	return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)