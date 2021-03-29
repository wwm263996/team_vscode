from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")


# 円の公式計算アプリ
@app.route("/circle")
def circle():
    return render_template("circle.html")

@app.route("/circle.result")
def circle_result():
    hankei = request.args.get("hankei")
    ensyu = float(hankei) * 2 * 3.14
    menseki = float(hankei) * float(hankei) * 3.14
    return render_template("circle_result.html", hankei=hankei, ensyu=ensyu, menseki=menseki)


# 給与計算アプリ
@app.route("/salary")
def salary():
    return render_template("salary.html")


if __name__ == "__main__":
    app.run(debug=True)