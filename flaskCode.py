from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_dear():
    return "<h1>I LOVE YOU DARLING ..!</h1>"

@app.route('/hello_feelings')
def hello_feelings():
    return "<h1>I CAN'T LIVE WITH OUT YOU ..!</h1>"

@app.route('/hello_feelings_1')
def hello_feelings_1():
    data = request.args.get('x')
    return "THIS IS MY NAME {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
