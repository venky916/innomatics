from flask import Flask, render_template, request ,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import string,random,os
import requests


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
path = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = path
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1000),nullable=False)
    short = db.Column(db.String(20),unique=True, nullable=False)

    def __init__(self, original, short):
        self.url = original
        self.short = short

    def __repr__(self) -> str:
        return " id-{} , url-{} , short-http://127.0.0.1:5000/{}".format(self.id, self.url, self.short)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        urls = request.form['input_url']
        response=requests.get(urls)
        print(response)
        if response.status_code==200:
            check_url= Urls.query.filter_by(url=urls).first()
            if check_url:
                return render_template('home.html',actual_url=check_url.url,short_url=check_url.short)
            else:
                short_url=short()
                new_url = Urls(urls, short_url)
                db.session.add(new_url)
                db.session.commit()
                # print(new_url)
                # print(type(new_url))
                # print(type(new_url.id))
                # print(type(new_url.url))
                # print(type(new_url.short))
                return render_template("home.html",actual_url=urls ,short_url=short_url)   
    else:
        return render_template('home.html')
    
def short():
    letter=string.ascii_lowercase + string.ascii_lowercase +string.digits
    endpoint=''
    for _ in range(7):
        endpoint +=random.choice(letter)
    return endpoint

@app.route('/<short_url>')
def redirect(short_url):
    print(short_url)
    original_url = Urls.query.filter_by(short= short_url).first()
    if original_url:
        print(original_url)
        print(type(original_url))
        print(type(original_url.id))
        print(original_url.url)
        print(type(original_url.short))
        return original_url.url
    else:
        return f'<h1>no such url</h1>'
    
@app.route('/history')
def history():
    urls = Urls.query.all()
    return render_template('history.html',urls=urls)  

if __name__ == '__main__':
    app.run(debug = True)