from application import app, db
from flask import render_template, request, json, Response, redirect, flash
from application.models import dungeonx, monster, populate
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
    dungeons = dungeonx.objects.order_by("name")
    print(dungeons)
    return render_template("dungeon.html", dungeonData=dungeons, dungeon=True, dungeonName = dungeonName)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        monster_id = form.monster_id.data
        called = form.called.data

        monsterone = monster.objects(monster_id=monster_id).first()
        print(called)
        if monsterone and monsterone.get_called(called) == monsterone.monster_id:
            flash(f"{monsterone.called}! You are monstered.", "good")
            return redirect("/index")
        else:
            flash("Sorry, epic fail", "bad")
    return render_template("login.html", form=form, title="Login", login=True)

@app.route("/create", methods=["POST", "GET"])
def create():
    form = PopulateForm()
    if form.validate_on_submit():
        monster_id  =   monster.objects.count()
        monster_id  += 1
        print(monster_id)

        called      =   form.called.data
        monster_type =  form.monster_type.data
        damage      =   form.damage.data

        monsterone = monster(monster_id = monster_id, called = called, monster_type = monster_type, damage = damage)
        monsterone.set_called(called)
        monsterone.save()
        flash('monster made')
        return redirect("index")
    return render_template("create.html", form=form, title="Create", create=True)

@app.route("/make", methods=["GET", "POST"])
def make():
    dungeonID = request.form.get('dungeonID')
    dungeonName = request.form.get('name')
    monster_id = 1

    if dungeonID:
        if populate.objects(monster_id=monster_id,dungeonID=dungeonID):
            flash(f"already made {dungeonName}", "bad")
            return redirect(url_for("dungeon"))
        else:
            populate(monster_id=monster_id,dungeonID=dungeonID)
            flash(f"made {dungeonName}", "good")
    dungeons = list( monster.objects.aggregate()*[
            {
                '$lookup': {
                    'from': 'populate', 
                    'localField': 'monster_id', 
                    'foreignField': 'monster_id', 
                    'as': 'r1'
                }
            }, {
                '$unwind': {
                    'path': '$r1', 
                    'includeArrayIndex': 'r1_id', 
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$lookup': {
                    'from': 'dungeonx', 
                    'localField': 'r1.dungeonID', 
                    'foreignField': 'dungeonID', 
                    'as': 'r2'
                }
            }, {
                '$unwind': {
                    'path': '$r2', 
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$match': {
                    'monster_id': monster_id
                }
            }, {
                '$sort': {
                    'dungeonID': 1
                }
            }
        ])
    return render_template("make.html", make=True, title="Maked", population = population)

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
    dungeons = dungeon.objects.all()
    return render_template("room.html", dungeons=dungeons)