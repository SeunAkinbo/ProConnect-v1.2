#!/usr/bin/python3
"""The Users View"""
from api.v1.views import app_views
from flask import jsonify, request
from flasgger.utils import swag_from
from models import database
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_users.yml')
def get_users():
    """
    Retrives the list of all users
    """
    users = database.all(User).values()
    return jsonify({"users": [user.to_dict() for user in users]})