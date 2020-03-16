from flask import Flask, request, make_response, redirect, abort
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    user_agent = request.headers.get('User_Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)


@app.route('/kal')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/red')
def inx():
    return redirect('user.html')


