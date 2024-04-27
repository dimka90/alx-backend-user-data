#!/usr/bin/env python3
"""DB module
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
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
        """
        store users in the Database
        Argument
            email(str): User email to store
            hashed_password(str): hashed password to store
        Return:
            User: A saved user instance stored in the database        """
        session = self._session
        add_user = User(email=email, hashed_password=hashed_password)
        session.add(add_user)
        session.commit()
        return add_user

    def find_user_by(self, **kwargs) -> User:
        """
        search for a user in the database
        Argument:
                kwargs(dict): a key, value pair for email and
                hashed_password
        Return:
                User(instance)
        """
        if not kwargs:
            raise InvalidRequestError
        for key, value in kwargs.items():
            if not hasattr(User, key):
                raise InvalidRequestError

        requested_user = self._session.query(User).filter_by(**kwargs).first()

        if not requested_user:
            raise NoResultFound
        return requested_user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Argument:
                kwargs(dict): a key, value pair for email and
                hashed_password
        Return:
                User(instance)
        """
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if hasattr(User, key):
                setattr(user, key, value)
            else:
                raise ValueError
        self._session.commit()
