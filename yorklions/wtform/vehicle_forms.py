from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField, FloatField
from wtforms.validators import InputRequired, NumberRange
from datetime import datetime

class CreateVehicleForm(FlaskForm):
    max_year = int(datetime.now().strftime("%Y")) + 1
    price = FloatField("Price", validators=[InputRequired(), NumberRange(min=0)], name="price")
    discount = FloatField("Discount", validators=[InputRequired(), NumberRange(min=0)], name="discount")
    year = IntegerField("Year", validators=[InputRequired(), NumberRange(min=2000, max=max_year)], name="year")
    make = StringField("Make", validators=[InputRequired()], name="make")
    model = StringField("Model", validators=[InputRequired()], name="model")
    trim = StringField("Trim Level", validators=[InputRequired()], name="trim")
    colour = SelectField("Colour", choices=["Black", "White", "Grey", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Beige", "Brown"])
    type = SelectField("Vehicle Type", choices=["Crossover", "SUV", "Sedan", "Coupe", "Sports Car", "Station Wagon", "Hatchback", "Convertible", "Pickup Truck", "Minivan", "Other"])
    kilometres = IntegerField("Kilometres", validators=[InputRequired(), NumberRange(min=0)], name="kilometres")
    max_range = IntegerField("Max Range", validators=[InputRequired(), NumberRange(min=0)], name="max_range")
    picture = FileField("Picture", validators=[InputRequired()])
    description = TextAreaField("Description", name="description")
    submit = SubmitField("Create Vehicle")

class CreateTradeInForm(FlaskForm):
    max_year = int(datetime.now().strftime("%Y")) + 1
    year = IntegerField("Year", validators=[InputRequired(), NumberRange(min=2000, max=max_year)], name="year")
    make = StringField("Make", validators=[InputRequired()], name="make")
    model = StringField("Model", validators=[InputRequired()], name="model")
    trim = StringField("Trim Level", validators=[InputRequired()], name="trim")
    colour = SelectField("Colour", choices=["Black", "White", "Grey", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Beige", "Brown"])
    type = SelectField("Vehicle Type", choices=["Crossover", "SUV", "Sedan", "Coupe", "Sports Car", "Station Wagon", "Hatchback", "Convertible", "Pickup Truck", "Minivan", "Other"])
    kilometres = IntegerField("Kilometres", validators=[InputRequired(), NumberRange(min=0)], name="kilometres")
    max_range = IntegerField("Max Range", validators=[InputRequired(), NumberRange(min=0)], name="max_range")
    picture = FileField("Picture", validators=[FileAllowed(["jpg", "jpeg", "png"])])
    accidents = TextAreaField("Describe any accidents or repairs", name="accidents")
    details = TextAreaField("Describe any other details (e.g. add-ons, packages, etc.)", name="details")
    submit = SubmitField("Submit")
