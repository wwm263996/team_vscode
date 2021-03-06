from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")


# 円の公式計算アプリ
@app.route("/circle")
def circle():
    return render_template("circle.html")

@app.route("/circle_2")
def circle_2():
    hankei = request.args.get("hankei")
    ensyu = float(hankei) * 2 * 3.14
    menseki = float(hankei) * float(hankei) * 3.14
    return render_template("circle_2.html",hankei=hankei, ensyu=ensyu, menseki=menseki)
    

# 給与計算アプリ
@app.route("/salary")
def salary():
    return render_template("salary.html")

@app.route("/salary_2")
def salary_2():
    time_money = request.args.get("time_money")
    time = request.args.get("time")

    all = int(time) * int(time_money)
    return render_template("salary_2.html",all=all)


if __name__ == "__main__":
    app.run(debug=True)