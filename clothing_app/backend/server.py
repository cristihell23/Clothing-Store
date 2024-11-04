from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import products_dao


app = Flask (__name__)

connection = get_sql_connection()


# Use this to test server - 127.0.0.1:5000/hello
@app.route('/hello')

# Test Function
def hello():
    return "hello !"

# For easy of use copy - 127.0.0.1:5000/getProducts
@app.route('/getProducts', methods = ['GET'])

# Get all products from database and return them as JSON.
def get_Products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    # CORS documentation - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Starting Flask Server")
    app.run(port=5000)