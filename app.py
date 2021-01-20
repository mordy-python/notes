from flask import Flask, render_template, request, url_for, redirect
import datetime
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient('localhost', 27017)

db = client.todo
collection = db.todo

@app.route("/")
def index():
    posts = collection.find()
    posts = posts.sort("date",-1)
    return render_template("index.html", posts=posts)
@app.route("/upload")
def upload():
    return render_template("upload.html")
@app.route("/save", methods=['POST'])
def save():
    name = request.form.get('name')
    title = request.form.get('title')
    content = request.form.get('notes')
    post = {
        'name':name,
        'date':datetime.datetime.utcnow(),
        'title':title,
        'content':content
    }
    collection.insert_one(post)
    return redirect(url_for('index'))
@app.route("/del/admin/mordy/2005")
def del():
    for i in collection.find():
        collection.delete_one(i)
    return redirect(url_for('index'))
app.run()