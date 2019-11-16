from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class MarkAttendance(FlaskForm):
    name = StringField( 'name', validators=[DataRequired()] )
    rollnum = StringField('rollnum', validators=[DataRequired()])
    mac = StringField('mac', validators=[DataRequired()])
    submit = SubmitField('Mark Attendnce')
    