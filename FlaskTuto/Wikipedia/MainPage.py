from flask import Flask, render_template, redirect, url_for
from flask import request, jsonify, json
from datainfo import *
app=Flask(__name__)

@app.route('/eng')
def postJsonHandler():
    res=Wikipi()
    r=res.collect()
    return dict(r)



if __name__=="__main__":
    app.run(debug=True)