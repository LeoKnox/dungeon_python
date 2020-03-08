from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)

@app.route("/dungeon")
def dungeon():
    dungeonData = [{"dungeonID":"1111","name":"Entry","length":"4","width":"4","material":"stone"},
    {"dungeonID":"1112","name":"Storage","length":"6","width":"5","material":"wood"},
    {"dungeonID":"1113","name":"Tome","length":"5","width":"8","material":"stone"}]
    print(dungeonData)
    return render_template("dungeon.html", dungeonData=dungeonData, dungeon=True)

@app.route("/create")
def create():
    return render_template("create.html", create=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)