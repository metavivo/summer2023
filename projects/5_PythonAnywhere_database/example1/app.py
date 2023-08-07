from flask import Flask, render_template, request, jsonify, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="valitutti",
    password="Bellosguardo68",
    hostname="valitutti.mysql.pythonanywhere-services.com",
    databasename="valitutti$comments"
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#------------------------------------------------------------------------

class Word(db.Model):
	__tablename__ = "words"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)

	def __init__(self, name):
		self.name = name

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

#------------------------------------------------------------------------

@app.route("/")
def home():
#    return 'prova'
    return render_template('input.html')


@app.route('/input', methods = ["POST"])
def input():
##    return "Input word inserted!"
    if request.method == 'POST':
        word = request.form['word']
        data = Word(word)
        db.session.add(data)
        db.session.commit()
        out = Word.query.all()
        return render_template("output.html", word_data = out)
