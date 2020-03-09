from application import app, db
from flask import render_template, request, json, Response, redirect, flash
from application.models import dungeon, monster, populate
from application.forms import LoginForm, PopulateForm

dungeonData = [{"dungeonID":"1111","name":"Entry","length":"4","width":"4","material":"stone"},
{"dungeonID":"1112","name":"Storage","length":"6","width":"5","material":"wood"},
{"dungeonID":"1113","name":"Tome","length":"5","width":"8","material":"stone"}]

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)

@app.route("/dungeon")
@app.route("/dungeon/<dungeonName>")
def dungeon(dungeonName="Generic"):
    return render_template("dungeon.html", dungeonData=dungeonData, dungeon=True, dungeonName = dungeonName)

@app.route("/create")
def create():
    return render_template("create.html", create=True)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(request.form.get("monster_id"))
        if request.form.get("monster_id") == "1":
            flash("You are monstered.", "good")
            return redirect("/index")
        else:
            flash("Sorry, epic fail", "bad")
    return render_template("login.html", form=form, title="Login", login=True)

@app.route("/make", methods=["GET", "POST"])
def make():
    id = request.form.get('dungeonID')
    name = request.form.get('name')
    return render_template("make.html",data={"id":id, "name":name})

@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = dungeonData
    else:
        jdata = dungeonData[int(idx)]
    
    return Response(json.dumps(jdata), mimetype="application/json")

@app.route("/room")
def room():
    #Dungeon(dungeonID=1, name="Boss Room", length=9, width=9).save()
    #Dungeon(dungeonID=2, name="King Room", length=7, width=7).save()
    dungeons = Dungeon.objects.all()
    return render_template("room.html", dungeons=dungeons)