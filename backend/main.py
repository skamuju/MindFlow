

from flask import Flask

app = Flask(__name__)

flip = True

@app.route('/')
def welcome():
    return 'Welcome to MindFlow!'

@app.route('/graph')
def graphs():
    return "pending"

@app.route('/journals')
def journals():
    return "pending"

@app.route('/medicines')
def meds():
    return "pending"

@app.route('/Resources')
def recs():
    return "pending"


if __name__ == "__main__":
    app.run(debug = True)