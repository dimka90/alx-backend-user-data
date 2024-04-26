#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.auth import Auth

a = Auth()

print(1,a.require_auth(None, None))
print(2,a.require_auth(None, []))
print(3,a.require_auth("/api/v1/status/", []))
print(4,a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(5,a.require_auth("/api/v1/status", ["/api/v1/status/"]))
print(6,a.require_auth("/api/v1/users", ["/api/v1/status/"]))
print(7,a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))
