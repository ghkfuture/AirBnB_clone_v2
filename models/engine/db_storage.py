#!/usr/bin/python3
""" DBStorage Module for HBNB project """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ Interacts with the MySQL database """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiate DBStorage object """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db),
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on current database session all objects of given class """
        classes = [State, City, User, Place, Review, Amenity]
        result_dict = {}

        if cls is None:
            for c in classes:
                query_res = self.__session.query(c).all()
                for obj in query_res:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    result_dict[key] = obj
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            query_res = self.__session.query(cls).all()
            for obj in query_res:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result_dict[key] = obj
        return result_dict

    def new(self, obj):
        """ Add object to current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Commit all changes of current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj from current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in database and session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Close session """
        self.__session.close()
