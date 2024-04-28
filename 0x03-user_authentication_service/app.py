#!/usr/bin/env python3
"""A flask app"""

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)


@app.route("/")
def index():
    """Index page"""
    payload = {"message": "Bienvenue"}
    return jsonify(payload)


@app.route("/users", methods=["POST"])
def users():
    """Register Users"""
    email = request.form.get("email")
    password = request.form.get("password")
    # Creating an instance of an Auth class
    AUTH = Auth()

    try:
        register_user = AUTH.register_user(email, password)

    except ValueError:
        payload = {"message": "email already registered"}

        return jsonify(payload), 400

    payload = {"email": email, "message": "user created"}
    return jsonify(payload), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
