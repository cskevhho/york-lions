from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from ..models.rating import Rating

class CreateRatingForm(FlaskForm):
    f_name = StringField(
            "First Name", validators=[Length(min=0, max=20)]
            )
    l_initial = StringField(
            "Last Initial", validators=[Length(min=0, max=1)]
            )
    rating = FloatField( # set 0-5 so the rating of a vehicle can go below 1
                        "Rating (0-5)", validators=[DataRequired(), NumberRange(min=0, max=5)]
                        )
    review_body = TextAreaField(
            "Review Body (max 280 char)", validators=[Length(min=0, max=280)] # tweet tweet
            )
    submit = SubmitField("Submit Rating")

class CreateRatingFormAdmin(FlaskForm):
     make = StringField(
             "Make", validators=[DataRequired(), Length(min=1, max=20)]
             )
     model = StringField(
             "Model", validators=[DataRequired(), Length(min=1, max=20)]
             )
     year = StringField(
             "Year", validators=[DataRequired(), Length(min=4, max=4)]
             )
     f_name = StringField(
             "First Name", validators=[Length(min=0, max=20)]
             )
     l_initial = StringField(
             "Last Initial", validators=[Length(min=0, max=1)]
             )
     rating = FloatField( # set 0-5 so the rating of a vehicle can go below 1
                         "Rating (0-5)", validators=[DataRequired(), NumberRange(min=0, max=5)]
                         )
     review_body = TextAreaField(
             "Review Body (max 280 char)", validators=[Length(min=0, max=280)] # tweet tweet
             )
     submit = SubmitField("Submit Rating")


class ReadRatingForm(FlaskForm):
                         pass

                     # You can call this unethical, but this is just to censor sneaky profanity 8^)
class UpdateRatingForm(FlaskForm):
    pass

class DeleteRatingForm(FlaskForm):
    pass
