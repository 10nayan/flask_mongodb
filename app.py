import os
from flask import Flask, request, jsonify
from mongoengine import connect
from api import api_bp

# Flask app object
app = Flask(__name__)

# Register the Blueprint with a URL prefix
app.register_blueprint(api_bp, url_prefix = '/api')

# Configuration for the MongoDB database
app.config['MONGODB_DB'] = os.environ['DATABASE_NAME']
app.config['MONGODB_HOST'] = os.environ['DATABASE_URL']

# Initialize the MongoEngine connection
db = connect(host = app.config['MONGODB_HOST'], db = app.config['MONGODB_DB'])

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug = True, port = 8000)



