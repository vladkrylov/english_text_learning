from flask_wtf import Form
from wtforms import TextField, TextAreaField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
    openid = TextField("openid", validators = [Required()])
    remember_me = BooleanField("remember_me", default = False)

class RegisterForm(Form):
    name = TextField("name", validators = [Required()])
    email = TextField("email", validators = [Required()])
    
class AddTextForm(Form):
    title = TextField("title", validators = [Required()])
    text = TextAreaField("text", validators = [Required()])

