#!/usr/bin/env python3
"""A personal Data module"""

import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"
    def __init__(self, fields: List[str]):

        super(RedactingFormatter, self).__init__(self.FORMAT)
        logging.basicConfig(format=RedactingFormatter.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """"""
        return filter_datum(self.fields,RedactingFormatter.REDACTION,
                             record.msg, RedactingFormatter.SEPARATOR)
def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """A function that replace a message with some random values"""
    for field in fields:
        message = re.sub("{}=.*?{}".format(field, separator),
                         "{}={}{}".format(field, redaction, separator),
                         message)
    return message
