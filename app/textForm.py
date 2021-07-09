from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  DataRequired
class TextForm(FlaskForm):
    textTospeech = StringField('ENTRER LE TEXT QUE VOUS VOULEZ ENTENDRE', validators=[DataRequired()])
    submit = SubmitField('ENTENDRE')