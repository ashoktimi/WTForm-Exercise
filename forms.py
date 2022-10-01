
from typing import Any
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf



class PetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(values=['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo", [Optional(), URL()])
    age = FloatField("Age", validators=[Optional(), NumberRange(0, 30)])
    notes = StringField("About", validators=[Optional()])
    available = BooleanField("Available", default = "checked", validators=[Optional()])