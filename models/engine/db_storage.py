#!/usr/bin/python3
""" New db engine for HBNB """

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
from os import close, getenv

DICT = {
    'State' = State
    'City' = City
    'Place' = Place
    'Amenity' = Amenity
    'Revie' = Review
    'User' = User
}


class DBStorage:
    """ Storage for HBNB models in SQLAlchemy """
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        enviroment = getenv('HBNB_MYSQL_ENV')
        self.__engine = create_engine(
            'mysqlmysql+mysqldb://{}:{}@{}/{}'.format(
                user, password, host, database), pool_pre_ping=True')
        if enviroment == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Return Database Storage """
        query_list = []
        query_dict = {}
        if cls in DICT:
            obj = self.__session.query(classes[cls]).all()
            for obj_ in obj:
                key = "{}.{}".format(obj_.__class__.__name__, obj_.id)
                value = obj_
                query_dict[key] = value
        elif cls is None:
