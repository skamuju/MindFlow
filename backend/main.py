

from flask import Flask, request, jsonify
from pymongo import MongoClient, operations

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to MindFlow!'

@app.route('/register', methods = ['POST'])
def register():
    data = request.get_json()
    my_client = MongoClient('mongodb+srv://skamuju2:mflow07@cluster0.vdo8j3z.mongodb.net/?retryWrites=true&w=majority')
    db = my_client['MindFlow']
    collection = db['users']

    post = {'username': data["username"], 'password': data["password"]}
    collection.insert_one(post)
    
    return jsonify({"success": True})

@app.route('/login', methods = ['GET'])
def login():
    data = request.get_json()
    my_client = MongoClient('mongodb+srv://skamuju2:mflow07@cluster0.vdo8j3z.mongodb.net/?retryWrites=true&w=majority')
    db = my_client['MindFlow']
    collection = db['users']

    post = {'username': data["username"], 'password': data["password"]}
    
    if collection.find_one(post):
        return jsonify({"success": True})
    
    else:
        return jsonify({"success": False})

    

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