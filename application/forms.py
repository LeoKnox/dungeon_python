from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from application.models import monster

class LoginForm(FlaskForm):
    monster_id  =   IntegerField("Monster Id", validators=[DataRequired()])
    called      =   StringField("Called", validators=[DataRequired()])
    remember_me =   BooleanField("Remember Me")
    submit      =   SubmitField("Login")

class PopulateForm(FlaskForm):
    monster_id  =   IntegerField("Monster Id", validators=[DataRequired()])
    called      =   StringField("Called", validators=[DataRequired(), Length(min=3)])
    called_confim =   StringField("Called", EqualTo('called'), Length(min=3), validators=[DataRequired()])
    monster_type =   StringField("Type", validators=[DataRequired()])
    damage      =   IntegerField("Damage", validators=[DataRequired()])
    submit      =   SubmitField("Login")

    def validate_monster(self, monster_id):
        monster = monster.objects(called=called.data).first()
        if monster:
            raise ValidationError("Already in use try again")