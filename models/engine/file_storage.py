#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

"""
This module will help with the flow of serialization -deserialization
for the console using the FileStorage class.
"""


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes
    JSON file to instances

    """

    __file_path = "file.json"
    __objects = {}  # the private dictionary

    def new(self, obj):
        """
        this is a setter for our different objects

        Args:
            obj: the objects to be set in our private __objects attribute
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj

    def all(self):
        """
        the getter method that helps to retrieve all objects stored in the
        in the __objects dictionary

        Returns:
            FileStorage.__objects
        """
        return FileStorage.__objects

    def save(self):
        """
        to save the __objects by serializing them to the JSON file path

        """
        my_objts = FileStorage.__objects
        my_obj_dict = {}
        for objts in my_objts.keys():
            my_obj_dict[objts] = my_objts[objts].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(my_obj_dict, file)

    def reload(self):
        """
        for deserializing the object file

        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    my_obj_dict = json.load(file)

                    for key, value in my_obj_dict.items():
                        cls_name, my_obj_id = key.split(".")

                        my_cls = eval(cls_name)

                        instance = my_cls(**value)

                        FileStorage.__objects[key] = instance

                except Exception:
                    pass
