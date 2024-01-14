#!/usr/bin/python3
"""
This contains both the example test and the unit test for
project three of the Airbnb project

"""
import unittest
from models.base_model import BaseModel


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    v = my_model_json[key]
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), v))


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """
        for testing the model's initialization procedures
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        To see if the save method works appropriately
        """
        my_model = BaseModel()

        start_updated_at = my_model.updated_at
        current_updated_at = my_model.save()
        self.assertNotEqual(start_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        to confim the proper fuctioning of the dictionary method
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(my_model_dict["id"], my_model.id)
        t = my_model.created_at.isoformat()
        u = my_model.updated_at.isoformat()
        self.assertEqual(my_model_dict["created_at"], t)
        self.assertEqual(my_model_dict["updated_at"], u)

    def test_str(self):
        """
        to test for the string printing function
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith("[BaseModel]"))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
