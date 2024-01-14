#!/usr/bin/python3
"""
This is the base model to our Airbnb console which will be designed to help
with initialization, serialization and  deserialization of our future instances
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """
        To initial the class
        """
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        To save the time and date the instance of the object was updated
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Return
            instance_dict (dict): a dictionary  containing all keys/values
            of __dict__ of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict

    def __str__(self):
        """
        The format of the string for output
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
