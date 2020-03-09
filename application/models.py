import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class dungeon(db.Document):
    dungeonID       =   db.IntField( unique=True )
    name            =   db.StringField( max_length=50 )
    length          =   db.IntField()
    width           =   db.IntField()
    material        =   db.StringField( max_length=50 )

class monster(db.Document):
    monster_id      =   db.IntField( unique=True )
    called          =   db.StringField()
    monster_type    =   db.StringField( max_length=50 )
    damage          =   db.IntField()

    def set_called(self, called):
        self.called = generate_password_hash(called)

    def get_called(self, called):
        return check_password_hash(self.called, called)

class populate(db.Document):
    dungeonID       =   db.IntField()
    monster_id      =   db.IntField()