from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

species = ['Dog', 'Cat', 'Porcupine']

class AddPetForm(FlaskForm):
    """Form to add a new pet"""
    name = StringField("Name", validators=[InputRequired(message="Pet name can't be blank")])
    species = SelectField("Species", choices=[(sp, sp) for sp in species], validators=[InputRequired(message="Pet species can't be blank")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Must be a valid URL")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form to edit an existing pet"""
    name = StringField("Name", validators=[InputRequired(message="Pet name can't be blank")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Must be a valid URL")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available?", validators=[Optional()])