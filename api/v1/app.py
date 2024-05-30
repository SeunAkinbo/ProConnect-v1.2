#!/usr/bin/python3
"""The Flask Application"""
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from api.v1.views import app_views
from models import database

#Create and configure the Flask application
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*":{"origin":"*"}})


Swagger(app, config={'title': 'ProConnect Restful API'})

@app.teardown_appcontext
def close_db(exception=None):
    """
    Terminates the database session
    """
    database.close()

@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors
    """
    return make_response(
        jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    """The main entry point for the Flask application"""
    app.run(threaded=True)