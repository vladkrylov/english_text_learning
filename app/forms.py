from flask_wtf import Form
from wtforms import TextField, TextAreaField, BooleanField, SelectField
from wtforms.validators import Required

from models import Tense

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
    all_tenses = None 
    
    phrase = TextField(u"phrase", validators = [Required()])
    tense = SelectField(u"tense", validators = [Required()])
    
    def __init__(self):
        super(PhraseForm, self).__init__()
        self.tense.choices = self.GetTensesForSelect()
        
    def GetTensesForSelect(self):
        if PhraseForm.all_tenses is None:
            PhraseForm.all_tenses = [(t.short_name, t.name) for t in Tense.query.all()]
            print "Database request here!"
        
        return PhraseForm.all_tenses
