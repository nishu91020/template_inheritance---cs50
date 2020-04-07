from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("first_page.html")

@app.route("/second_page")
def more():
    return render_template("second_page.html")
