#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from models.engine.file_storage import FileStorage
from models.city import City
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == db:
        cities = relationship("city", backref='state')
    else:
        @property
        def cities(self):
            """List of all related City objects"""
            from models import storage
            city_list = []
            for key, obj in storage.all(City).items():
                if self.id == obj.state_id:
                    city_list.append(obj)
            return city_list

    def __init__(self, *args, **kwargs):
        """States Constructor"""
        super().__init__(*args, **kwargs)
