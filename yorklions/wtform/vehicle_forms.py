from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from ..models.user import User
from datetime import datetime


class CreateTradeInForm(FlaskForm):
    max_year = int(datetime.now().strftime("%Y")) + 1
    year = IntegerField("Year", validators=[DataRequired(), NumberRange(min=2000, max=max_year)], name="year")
    make = StringField("Make", validators=[DataRequired()], name="make")
    model = StringField("Model", validators=[DataRequired()], name="model")
    trim = StringField("Trim Level", validators=[DataRequired()], name="trim")
    colour = SelectField("Colour", choices=["Black", "White", "Grey", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Beige", "Brown"])
    type = SelectField("Vehicle Type", choices=["Crossover", "SUV", "Sedan", "Coupe", "Sports Car", "Station Wagon", "Hatchback", "Convertible", "Pickup Truck", "Minivan", "Other"])
    kilometres = IntegerField("Kilometres", validators=[DataRequired(), NumberRange(min=0)], name="kilometres")
    max_range = IntegerField("Max Range", validators=[DataRequired(), NumberRange(min=0)], name="max_range")
    picture = FileField("Picture", validators=[FileAllowed(["jpg", "jpeg", "png"])])
    accidents = TextAreaField("Describe any accidents or repairs", name="accidents")
    details = TextAreaField("Describe any other details (e.g. add-ons, packages, etc.)", name="details")
    submit = SubmitField("Submit")
