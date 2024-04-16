#!/usr/bin/env python3
""""Authentication class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication template"""

    def __init__(self):
        """Object instantiation"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Authentication method"""
        return False
    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        return
    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return
