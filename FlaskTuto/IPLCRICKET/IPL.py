from flask import Flask
from teams import *
app=Flask(__name__)


@app.route('/')
def home():
    e = []
    r = DATA()
    rs = r.DisplaySchedule()
    return rs

if __name__=="__main__":
    app.run(debug=True)