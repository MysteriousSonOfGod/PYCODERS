# from flask import Flask
# app=Flask(__name__)
#
# @app.route('/')
# def home():
#     return "This is Ravi I have completed Python Advanced"
#
# if __name__=="__main__":
#     app.run(debug=True)

# from flask import *
# app=Flask(__name__)
#
# @app.route('/prasad')
# def Display():
#     return "prasad Flask"
#
# if __name__=="__main__":
#     app.run(debug=True)


from flask import Flask
app=Flask(__name__)

@app.route('/home/<name>')
def dis(name):
    return "hello,"+name


@app.route('/home/<int:age>')
def fage(age):
    return "Age is {}".format(age)


def about():
    return "This is about page";


app.add_url_rule("/about", "about", about)

if __name__=="__main__":
    app.run(debug=True)