#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

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

    def find_user_by(self, **kwargs) -> User:
        """
        Search for a user in a database
        Args:
            Dic: Key value pair of name and email
        Return:
            User: User in the database
        """
        # filtering the dictionary into it attributes and values
        if not kwargs:
            raise InvalidRequestError
        for attr, values in kwargs.items():
            if not hasattr(User, attr):
                raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).one()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs: Dict[str, str]) -> None:

        # user = self.find_user_by(id=user_id)

        # if user:
        #     for key, values in kwargs.items():
        #         if not hasattr(User, key):
        #             raise ValueError
        #     user.hashed_password = kwargs['hashed_password']
        # self._session.commit()
        user = self.find_user_by(id=user_id)
        session = self._session
        for attr, val in kwargs.items():
            if not hasattr(User, attr):
                raise ValueError
            setattr(user, attr, val)
        session.commit()
