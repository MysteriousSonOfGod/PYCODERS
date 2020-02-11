from flask import Flask
import json
app=Flask(__name__)

@app.route('/home/<name>')
def home(name):
   return "Hello "+name

@app.route('/home/<int:age>')
def vote(age):
    if age>18:
        return "YOU ARE THE ELIGIBLE FOR VOTE"
    else:
        return "NOT ELIGIBLE"

if __name__=="__main__":
    app.run(debug=True)
