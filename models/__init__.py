#!/usr/bin/python3
<<<<<<< HEAD
"""This module instantiates an object of class FileStorage & Database"""
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')
if storage_type == "db":
    from models.engine.db_storage import DBStorage
=======
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import environ as env

if env.get('HBNB_TYPE_STORAGE') == 'db':
>>>>>>> 282a6eac2c664e4fe68b5d2974534cd19c4d3e4e
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
