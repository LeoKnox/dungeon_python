from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    monster_id  =   IntegerField("Monster Id", validators=[DataRequired()])
    called      =   StringField("Called", validators=[DataRequired()])
    remember_me =   BooleanField("Remember Me")
    submit      =   SubmitField("Login")

class PopulateForm(FlaskForm):
    monster_id  =   IntegerField("Monster Id", validators=[DataRequired()])
    called      =   StringField("Called", validators=[DataRequired()])
    monster_type=   StringField("Type", validators=[DataRequired()])
    damage      =   IntegerField("Damage", validators=[DataRequired()])
    submit      =   SubmitField("Login")