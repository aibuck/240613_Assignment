from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class TalkForm(FlaskForm):
  message = StringField('Message', validators=[DataRequired()])
  submit = SubmitField('Send')