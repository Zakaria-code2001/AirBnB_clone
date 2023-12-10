#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """designing the baseModel Class with the instance attributes initialization"""

    def __init__(self, *args, **kwargs):
        """creating a BaseModel from a dictionary"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """This Method is used to update_at attribute with the current date and time using the datetime module."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """this method get the values which are of datetime object type and  convert them to string objects in ISO format"""
        dictFormat = self.__dict__.copy()
        dictFormat["created_at"] = self.created_at.isoformat()
        dictFormat["updated_at"] = self.updated_at.isoformat()
        dictFormat["__class__"] = self.__class__.__name__
        return dictFormat

    def __str__(self):
        """We are using the __str__ method to return a human readable or informal string representation of an object."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
