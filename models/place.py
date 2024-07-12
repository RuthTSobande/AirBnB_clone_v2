#!/usr/bin/python3
<<<<<<< HEAD
""" Place Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
=======
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
>>>>>>> 282a6eac2c664e4fe68b5d2974534cd19c4d3e4e
from sqlalchemy.orm import relationship
import models
from os import environ as env

<<<<<<< HEAD
if models.storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id',
                                            onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id',
                                            onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True, nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_type == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer(), nullable=False, default=0)
        number_bathrooms = Column(Integer(), nullable=False, default=0)
        max_guest = Column(Integer(), nullable=False, default=0)
        price_by_night = Column(Integer(), nullable=False, default=0)
        latitude = Column(Float(), nullable=True)
        longitude = Column(Float(), nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary='place_amenity',
                                 backref="place_amenities", viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __int__(self, *args, **kwargs):
        """initialises Place"""
        super().__int__(*args, **kwargs)

    if models.storage_type != 'db':
        @property
        def reviews(self):
            from models.review import Review
            """File Storage relationship between Reviews & Place"""
            review_list = []
            all_reviews = models.storage.all(Review)
            for city in all_reviews.values():
                if Review.place_id == self.id:
                    review_list.append(city)
            return review_list

        @property
        def amenities(self):
            from models.place import Amenity
            """File Storage relationship between Amenity & Place"""
            amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list
=======

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey("places.id")),
    Column('amenity_id', String(60), ForeignKey("amenities.id"))
)


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    __reviews = relationship("Review", cascade="all, delete", backref="place")
    __amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        backref="place",
        viewonly=False
    )

    @property
    def reviews(self):
        """get all refiews with the current place id
        from filestorage
        """
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            return self.__reviews
        list = [
            v for k, v in models.storage.all(models.Review).items()
            if v.place_id == self.id
        ]
        return (list)

    @property
    def amenities(self):
        """get all amenities with the current place id
        """
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            return self.__amenities
        list = [
            v for k, v in models.storage.all(models.Amenity).items()
            if v.id in self.amenity_ids
        ]
        return (list)
>>>>>>> 282a6eac2c664e4fe68b5d2974534cd19c4d3e4e
