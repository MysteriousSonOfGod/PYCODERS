from flask import *
app=Flask(__name__)


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        uname=request.form['uname']
        passwd=request.form['pass']
        if uname=='ravi' and passwd=='Raviprasad@143':
            return "Welcome {}".format(uname)

    else:
        user = request.args.get('nm')
        return "not page"

if __name__=="__main__":
    app.run(debug=True)