from flask import Flask, request, jsonify


app = Flask (__name__)


# Use this to test server - 127.0.0.1:5000/hello
@app.route('/hello')
def hello():
    return "hello !"

if __name__ == "__main__":
    print("Starting Flask Server")
    app.run(port=5000)