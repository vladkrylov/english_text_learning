from flask_wtf import Form
from wtforms import TextField, TextAreaField, BooleanField, SelectField
from wtforms.validators import Required

class LoginForm(Form):
    openid = TextField(u"openid", validators = [Required()])
    remember_me = BooleanField(u"remember_me", default = False)

class RegisterForm(Form):
    name = TextField(u"name", validators = [Required()])
    email = TextField(u"email", validators = [Required()])
    
class AddTextForm(Form):
    title = TextField(u"title", validators = [Required()])
    text = TextAreaField(u"text", validators = [Required()])
    
class PhraseForm(Form):
    phrase = TextField(u"phrase", validators = [Required()])
    tense = SelectField(u"tense", validators = [Required()], choices = [("prs", "Present Simple"),
                                                              ("prc", "Present Continuous"),
                                                              ("prp", "Present Perfect")
                                                              ])

