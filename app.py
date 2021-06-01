from flask import Flask, render_template, request, redirect, send_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

# @app.route("/report")
# def report():
#     word = request.args.get('word')
#     if word:
#         a==1
#     else:
#         return redirect("/")
#     return render_template("report.html", searchingBy=word, reultsNumber=len(jobs), jobs=jobs, i = 1)

# @app.route("/export")
# def export():
#     try:
#         word = request.args.get('word')
#         if not word:
#             raise Exception()
#         word = word.lower()
#         jobs = db.get(word)
#         if not jobs:
#             raise Exception()
#         save_to_file(jobs)
#         return send_file("jobs.csv")
#     except:
#         return redirect("/")


app.run(host="0.0.0.0")
