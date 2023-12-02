from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from ..models.rating import Rating

class CreateRatingForm(FlaskForm):
    """ 
        to create a rating we will need the following things:
        - make, model, and year to be passed to the review page with details filled in
        - f_name
        - l_initial (optional name fields can be malicious, but we're not binding to user anyway
        - rating (from 1 to 5)
        - an optional body of text for a review
        - a timestamp for when the rating was created, which will be automatically generated
    """
    f_name = StringField(
            "First Name", validators=[Length(min=0, max=20)]
            )
    l_initial = StringField(
            "Last Initial", validators=[Length(min=0, max=1)]
            )
    rating = FloatField(
            "Rating (0-5)", validators=[DataRequired(), NumberRange(min=0, max=5)]
            )
    review_body = TextAreaField(
            "Review Body (max 280 char)", validators=[Length(min=0, max=280)] # tweet tweet
            )
    submit = SubmitField("Submit Rating")
"""
class ReadRatingForm(FlaskForm):
    return

# You can call this unethical, but this is just to censor sneaky profanity 8^)
class UpdateRatingForm(FlaskForm):
    return


class DeleteRatingForm(FlaskForm):
    return
"""
