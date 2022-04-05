from flask import Flask
from flask import render_template
from flask import Flask, request, json
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/blogs.db")


def main():
    app.run(port=8080, host='127.0.0.1')
    
@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return render_template("index.html", news=news)


if __name__ == '__main__':
    main()