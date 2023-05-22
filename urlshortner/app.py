import os
from flask import Flask, render_template, request ,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random,string

app = Flask(__name__)

############# SQL Alchemy Configuration #################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

#######################################################

############# Create a Model ################################################################3
class urllis(db.Model):
    __tablename__ = 'urllis'
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.Text)
    short_url=db.Column(db.Text)

    def __init__(self, url,short_url):
        self.urls = url
        self.short_url = short_url

    def __repr__(self):
        return "urlfull Name - {} , id-{} ,short_url - {} ".format(self.url,self.id,self.short_url)
########################################################################################################


@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        url = request.form['inp_url']
        check_url= urllis.query.filter_by(url=url).first()
        if check_url:
            return redirect(url_for("home.html",url=url ,short_url=check_url.short_url))
        else:
            short_url=short()
            new_url = urllis(url,short_url)
            db.session.add(new_url)
            db.session.commit()
            return render_template("home.html",url=url,short_url=short_url)
    else:
        return render_template('home.html')
    
def short():
    letter=string.ascii_lowercase + string.ascii_lowercase +string.digits
    endpoint=''
    for _ in range(3):
        endpoint +=random.choice(letter)
    return endpoint

@app.route('/history')
def history():
    all_urls = urllis.query.all()
    return render_template("history.html",all_urls=all_urls)

@app.route('/<short_url>')
def redirect(short_url):
    check_url=urllis.query.filter_by(short_url=short_url).first()
    if check_url:
        return redirect(check_url.url)
    
if __name__ == '__main__':
    app.run(debug = True)