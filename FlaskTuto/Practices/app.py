from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('javascri.html')

@app.route('/view', methods=['POST'])
def view():
    uname = request.form['fname']
    return uname

if __name__=="__main__":
    app.run(debug=True)