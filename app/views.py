from app import app
import json

from flask import render_template, request, redirect, flash, url_for
from models import db, Text, Phrase, Tense
from forms import AddTextForm, PhraseForm

from sqlalchemy import desc
from sqlalchemy.sql import exists
from app.models import Tense
from sqlalchemy.sql.expression import except_

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/")
@app.route("/index")
def index():
    recent_texts = Text.query.order_by(Text.id.desc()).limit(10)
    return render_template("index.html", recent_texts = recent_texts)

@app.route("/addtext", methods = ['GET', 'POST'])
def addtext():
    form = AddTextForm()
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        
        new_text_item = Text(title=title, body=text)
        
        db.session.add(new_text_item)
        db.session.commit()
        
        return redirect(url_for("viewtext", text_id = new_text_item.id))
    return render_template("addform.html", form = form)

@app.route("/texts/<text_id>")
def viewtext(text_id):
    text_obj = Text.query.get_or_404(text_id)

    return render_template("viewtext.html", text = text_obj.body.split('\n'))

@app.route("/tasks/<text_id>")
def task(text_id):
    form = PhraseForm()
    text_obj = Text.query.get_or_404(text_id)
    text = text_obj.body
    lines = [[w for w in s.split()] for s in text.split('\n')]

    return render_template("task.html", title = text_obj.title, 
                                        lines = lines, 
                                        form = form)

@app.route("/ajax_add_phrase", methods = ['GET', 'POST'])
def add_new_phrase():
    phrase_body = request.form['phrase']
    tense_shortname = request.form['tense']
    url_parts = request.form['url'].split("/")
    text_id = int(url_parts[-1])
    
    already_exists = Phrase.query.filter_by(body = phrase_body).first()
    if already_exists is None:
        new_phrase = Phrase(body=phrase_body,
                            text=Text.query.get(text_id),
                            tense=Tense.query.filter_by(short_name=tense_shortname).first())
        db.session.add(new_phrase)
        db.session.commit()
    else:
        return json.dumps({'status':'already_exists', 'statustext':'This phrase is already exists.'})
      
    return json.dumps({'status':'ok', 'statustext':'New phrase was successfully added.'})
    
    
