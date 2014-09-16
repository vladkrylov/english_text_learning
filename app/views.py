from nltk_routine import *

from app import app
from flask import render_template, request, redirect, flash, url_for
from models import db, Text
from forms import AddTextForm


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/addtext", methods = ['GET', 'POST'])
def add_text():
    form = AddTextForm()
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        
        new_text_item = Text(title=title, body=text)
        
        db.session.add(new_text_item)
        db.session.commit()
        
        return redirect(url_for("task", text_id = new_text_item.id))
    return render_template("addform.html", form = form)

@app.route("/texts/<text_id>")
def view_text(text_id):
    text = Text.query.get_or_404(text_id)
    return render_template("viewtext.html", text = text.body.split('\n'))

@app.route("/task/<text_id>")
def task(text_id):
    text_obj = Text.query.get_or_404(text_id)
    text = text_obj.body
    
    tags = recognize(text)
    words = text.split()
    
    verbs = construct_verbs_list(tags)
    verbs_dict = {v: {i for i, x in enumerate(verbs) if x == v}
                  for v in verbs}
    print "---------------------------"
    print {tags.index(w): w for w in tags}
    print "---------------------------"

    return str(verbs)
    



