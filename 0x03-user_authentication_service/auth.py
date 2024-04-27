#!/usr/bin/env python3
"""
Module that Authenticate a User
"""

import bcrypt


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
