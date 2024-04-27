#!/usr/bin/env python3
"""A flask app"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    """Index page"""
    payload = {"message": "Bienvenue"}
    return jsonify(payload)
