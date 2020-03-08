import flask
from application import db

class dungeon(db.Document):
    dungeonID       =   db.IntField( unique=True )
    name            =   db.StringField( max_length=50 )
    length          =   db.IntField()
    width           =   db.IntField()
    material        =   db.StringField( max_length=50 )

class monster(db.Document):
    monster_id      =   db.IntFiled( unique=True )
    called          =   db.StringField( max_length=50 )
    monster_type    =   db.StringField( max_length=50 )
    damage          =   db.Intfield()

class populate(db.Document):
    dungeonID       =   db.IntField()
    monster_id      =   db.IntField()