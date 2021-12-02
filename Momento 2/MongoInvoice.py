from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from flask_cors import CORS
#import json
app = Flask(__name__)

CORS(app)

# conexión al server de MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dbinvoice'
mongo = PyMongo(app)

#EndPoints

@app.route('/books', methods=['POST'])
def add_book():
    number = request.form['number']
    date = request.form['date']
    price = request.form['price']
    balance = request.form['balance']
    if number and price:
        id = mongo.db.books.insert(
            {'number':number, 'date':date, 'price':price, 'balance': balance}
        )
        response = jsonify({'message':'Book '+ number + ' added successfully'})
        return response

@app.route('/books',methods=['get'])
def get_books():
    books = mongo.db.books.find()
    response = json_util.dumps(books) # BSON a JSON
    return Response(response, mimetype="applicatcd ion/json")

@app.route('/books/<id>', methods=["GET"])
def get_book(id):
    book = mongo.db.books.find_one({'_id':ObjectId(id)})
    response = json_util.dumps(book)
    return Response(response, mimetype="application/json")

@app.route('/books/<id>', methods=['delete'])
def delete_book(id):
    mongo.db.books.delete_one({'_id':ObjectId(id)})
    response = jsonify({"message":"Book "+id+" has been deleted"})
    return response

@app.route('/books/<_id>', methods=['PUT'])
def update_book(_id):
    number = request.form['number']
    date = request.form['date']
    price = request.form['price']
    balance = request.form['balance']
    if number and price and _id:
        mongo.db.books.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'number':number, 'date':date, 'price':price, 'balance': balance}})
        response = jsonify({'message': 'Book ' + _id + ' Updated Successfully'})
        return response
    
if __name__ == "__main__":
    app.run(debug=True, port=5600)