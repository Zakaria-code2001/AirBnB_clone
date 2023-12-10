#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Representation of an abstract storage engine."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the all the objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """Serialize the objects in JSON format"""
        instdict = FileStorage.__objects
        objects = {obj: instdict[obj].to_dict() for obj in instdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects, f)

    def reload(self):
        """Deserialize the objects in JSON format"""
        try:
            with open(FileStorage.__file_path) as f:
                objects = json.load(f)
                for o in objects.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
