#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError

from user import Base
from user import User
from typing import Dict


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db",)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add user to database"""
        user_1 = User(email=email, hashed_password=hashed_password)
        try:
            self._session.add(user_1)
            # store result
            self._session.commit()
        except Exception as e:
            print("An Exception occur {e}").format(e)
            self._session.rollback()
            raise
        return user_1

    def find_user_by(self, **kwargs: Dict[str, str]) -> User:
        """
        Search for a user in a database
        Args:
            Dic: Key value pair of name and email
        Return:
            User: User in the database
        """

        try:
            user = self.__session.query(User).filter_by(**kwargs).one()

        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError
        return user
