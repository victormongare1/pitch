from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,FileField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you.',validators = [Required()])
  submit = SubmitField('Submit')
class NewPitch(FlaskForm):
  title = StringField("Pitch Title", validators = [Required()])
  pitch = TextAreaField("Description", validators = [Required()])  
  category=SelectField("Category",
  choices=[("interview","interview"),("motivation","motivation"),("product","product"),("promotion","promotion")],validators = [Required()])
  submit=SubmitField("Add Pitch")
class CommentForm(FlaskForm):
  text = TextAreaField('Leave a comment:',validators=[Required()])
  submit=SubmitField('Submit')