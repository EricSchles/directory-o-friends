from flask import Flask, render_template,redirect

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET","POST"])
def signup():
    return render_template("signup.html")
    

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/directory/<username>")
def directory(username):
    return render_template("directory.html",username=username)

@app.route("/info/<username>/<person>")
def info(username,person):
    return render_template("info.html",username=username,person=person)
