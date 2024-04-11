#!/usr/bin/env python3
"""A personal Data module"""
import os
import mysql.connector
import re
from typing import List
import logging

PII_FIELDS = ("name", "email", "password", "ssn", "phone")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Innialise method """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format the """
        return filter_datum(self.fields, RedactingFormatter.REDACTION,
                            super().format(record),
                            RedactingFormatter.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """A function that replace a message with some random values"""
    for field in fields:
        message = re.sub("{}=.*?{}".format(field, separator),
                         "{}={}{}".format(field, redaction, separator),
                         message)
    return message


def get_logger() -> logging.Logger:
    """A loger function"""
    logger = logging.getLogger("user_data")
    # logger.propagate = False
    logger.propagate = False
    # setting a level
    logger.setLevel(logging.INFO)
    # Create a StreamHandler
    strem_handler = logging.StreamHandler()

    strem_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(strem_handler)
    return logger


def get_db():
    """Connect the Database using the environment vairable"""
    connector = mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", 'root'),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )
    return connector
