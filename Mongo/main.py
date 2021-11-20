from bson import objectid
from flask import Flask,request, Response, jsonify
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import json

app = Flask(__name__)
#conexion al server de mongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/dblibrary"
mongo = PyMongo(app)

#EndPoint

@app.route('/books', methods=['POST'])
def add_book():
    name = request.json['name']
    price = request.json['price']
    if name and price:
        id = mongo.db.books.insert({
            'name':name, 'price':price
            })
        response = jsonify({'message':'Book'+ name +' added successfully'})
        return Response(response, mimetype='application/json')

@app.route('/books', methods=['GET'])
def get_books():
    books = mongo.db.books.find()
    response = json_util.dumps(books)# BSON a JSON          
    return Response(response, mimetype="application/json")

@app.route('/book/<id>', methods=['GET'])
def get_book(id):
    book = mongo.db.books.find_one({'_id':ObjectId(id)})
    response = json_util.dumps(book)# BSON a JSON          
    return Response(response, mimetype="application/json")

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    mongo.db.books.delete_one({'_id':ObjectId(id)})
    response = jsonify({"message": "Book "+id+"has been deletd"})         
    return response

@app.route('/books/<_id>', methods=['PUT'])
def update_book(_id):
    name = request.json['name']
    price = request.json['price']
    if name and price and _id:
        mongo.db.books.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'name': name, 'price': price}})
        response = jsonify({'message': 'Book ' + _id + ' Updated Successfully'})
        return response

if __name__ == "__main__":
    app.run(debug=True, port=5600)