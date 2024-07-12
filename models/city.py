#!/usr/bin/python3
<<<<<<< HEAD
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
=======
"""This is the city class"""
from models.base_model import BaseModel, Base
from models.state import State
>>>>>>> 282a6eac2c664e4fe68b5d2974534cd19c4d3e4e
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class City(BaseModel, Base):
<<<<<<< HEAD
    """ The city class, contains state ID and name """
    if models.storage_type == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialises City"""
        super().__init__(*args, **kwargs)
=======
    """This is the class for City
    Attributes:
        __tablename__: name of the table represented
        state_id: The state id
        name: input name
    """

    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey(State.id), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade="all, delete", backref="city")
>>>>>>> 282a6eac2c664e4fe68b5d2974534cd19c4d3e4e
