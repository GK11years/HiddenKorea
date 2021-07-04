from flask import Flask, render_template, request, redirect, send_file
from module import rank_list as rl
app = Flask(__name__)


@app.route('/')
def hello_world():
    korea_list = rl.chart()['korea']
    japan_list = rl.chart()['japan']
    hidden_list = rl.chart()['hidden']

    return render_template("index.html", korea_list=korea_list, japan_list=japan_list, hidden_list=hidden_list)


app.run(host="0.0.0.0")
