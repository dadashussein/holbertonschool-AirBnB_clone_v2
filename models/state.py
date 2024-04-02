#!/usr/bin/python3
""" State Module for HBNB project """
form os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State Class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    def __init__(self, *args, **kwargs):
        """ Initialization of State instance """
        super().__init__(*args, **kwargs)
        
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            from models import storage
            from models.city import City
            cities = storage.all(City)
            return [city for city in cities.values if city.state_id == self.id]
