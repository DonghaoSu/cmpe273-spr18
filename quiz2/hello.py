from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/users", methods=['POST'])
def new_users():
    name = request.form["name"]
    return (jsonify({"id": 1, "name": name}), 201)

@app.route("/users/<int:id>", methods = ['GET'])
def users(id):
    return (jsonify({"id": id, "name": "foo"}), 200)


@app.route("/users/<int:id>", methods=['DELETE'])
def del_users(id):
    return ("", 204)
