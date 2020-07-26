from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

species = ['Rabbit', 'Tiger', 'Lion', 'Raccoon', 'Dog', 'Cat', 'Octopus']

class AddPetForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(message="Pet name can't be blank")])
    species = SelectField("Species", choices=[(sp, sp) for sp in species], validators=[InputRequired(message="Pet species can't be blank")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Must be a valid URL")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Notes", validators=[Optional()])

# , AnyOf(['rabbit', 'tiger', 'lion', 'raccoon', 'dog', 'cat', 'octopus'], message="Species must be one of the following: %(values)s")