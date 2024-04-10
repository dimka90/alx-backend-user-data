#!/usr/bin/env python3
"""A personal Data module"""

import re


def filter_datum(fields: list, redaction: str, message: str,
                 separator: str) -> str:
    """A function that replace a message with some random values"""
    for field in fields:
        message = re.sub("{}=.*?{}".format(field, separator),
                         "{}={}{}".format(field, redaction, separator),
                         message)
    return message
