from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")


# 円の公式計算アプリ
@app.route("/circle")
def circle():
    return render_template("circle.html")


# 給与計算アプリ
def salary():
    return render_template("salary.html")


if __name__ == "__main__":
    app.run(debug=True)