#!/usr/bin/env python3
"""
Module that Authenticate a User
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hashes user password
    Argument:
            password(str) -> Password to hash
    Return:
            password(bytes): Hashed password in bytes
    """
    # Generate a salt
    salt = bcrypt.gensalt()

    password = bcrypt.hashpw(password.encode("utf-8"), salt)

    return password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register users
        Argument(s):
            password(str) -> Password to hash
        Return:
            password(bytes): Hashed password in bytes
        """
        try:
            is_register = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            pass
        hashed_password = _hash_password(password)

        user = self._db.add_user(email, hashed_password)

        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user Details
        Arguments:
                email(str): user email
                password(str): password to check

        Return:
                Boolean
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
            return True
        else:
            return False
