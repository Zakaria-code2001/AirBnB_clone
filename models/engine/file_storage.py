#!/usr/bin/python3
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__} {obj.id}"
        self.__objects[key] = obj

    def save(self):
        
        for key, obj in self.__objects.items():
            self.__objects[key] = obj.to_dict()
            with open(self.__file_path, 'w') as file:
                json.dump(self.__objects, file)

    def reload(self):
        """
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)

            for key, value in loaded_objects.items():
                class_name, obj_id = key.split()
                class_instance = globals()[class_name]
                obj_instance = class_instance(**value)
                self.new(obj_instance)

        except FileNotFoundError:
            pass
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
