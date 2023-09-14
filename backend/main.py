

from flask import Flask

app = Flask(__name__)

flip = True

@app.route('/')
def welcome():
    return 'Welcome to MindFlow!'

@app.route('/switch')
def switch():
    if flip:
        return 'True'
    
    else:
        return 'False'


if __name__ == "__main__":
    app.run(debug = True)