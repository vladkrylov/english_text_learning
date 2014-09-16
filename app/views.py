from app import app

from flask import render_template, request, redirect, flash, url_for
from models import db, Text
from forms import AddTextForm

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

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
    text = Text.query.get_or_404(text_id)

    return render_template("viewtext.html", text = text.body.split('\n'))

