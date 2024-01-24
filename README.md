# AirBnB_clone

Developing a foundation for a simplified AirBnB website, Holberton School's project begins with crafting a command-driven console. This console serves as the initial building block, enabling users to manage objects within the website's framework.

Key functionalities of this console include:

**Object Creation:** Effortlessly bring new objects, such as Users or Places, into existence within the website.

**Object Retrieval:** Seamlessly access and retrieve existing objects from various storage sources, including files and databases.

**Object Manipulation:** Perform diverse operations on objects, such as counting, calculating statistics, or other necessary tasks.

**Object Modification:** Adapt and update object attributes as needed, ensuring website content remains current and accurate.

**Object Deletion:** Easily remove objects that are no longer relevant or required, maintaining a clean and organized website structure.

This console establishes a robust foundation for subsequent project stages, ultimately aiming to deploy a functional AirBnB website replica.





Examples of use <topic>
========================================
vagrantAirBnB_clone$./console.py
(hbnb) help

________________________________________
Documented commands (type help):
________________________________________
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
