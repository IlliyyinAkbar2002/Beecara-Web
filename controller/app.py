from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('../../view/pages/index.html')


@app.route('/login')
def login():
    return render_template('../../view/pages/login.html')


@app.route('/register')
def register():
    return render_template('../../view/pages/register.html')
