0x00. AirBnB clone - The console

Description
The AirBnB Clone Project is a Python-based project aimed at developing a simplified version of the popular AirBnB platform. It involves creating a command-line interpreter to manage various objects related to AirBnB, such as users, states, cities, places, etc. The project focuses on implementing a parent class (BaseModel) for initialization, serialization, and deserialization of objects, creating classes for AirBnB objects that inherit from BaseModel, implementing file storage for object persistence, and writing unit tests to validate the functionality of the project.

Command Interpreter Description
The command interpreter is a Python script that serves as the interface for interacting with the AirBnB objects. It allows users to perform various operations on AirBnB objects, such as creating, retrieving, updating, and deleting them. The command interpreter supports a set of commands that users can enter to perform specific actions on the AirBnB objects.

How to Start the Command Interpreter
To start the command interpreter, follow these steps:

1.Clone the repository containing the AirBnB project code.
2.Navigate to the root directory of the project.
3.Run the command python airbnb_cli.py in the terminal to start the command interpreter.
4.How to Use the Command Interpreter
5.Once the command interpreter is running, users can enter commands to interact with AirBnB objects.

Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

 The supported commands include:

>create: Create a new AirBnB object.
>retrieve: Retrieve an existing AirBnB object.
>update: Update attributes of an existing AirBnB object.
>delete: Delete an existing AirBnB object.
>quit: Exit the command interpreter.

create <class_name>: Creates a new instance of the specified class (e.g., BaseModel) and saves it to the JSON file.

show <class_name> <id>: Prints the string representation of an instance based on the class name and ID.

destroy <class_name> <id>: Deletes an instance based on the class name and ID.

all [class_name]: Prints all instances or instances of a specific class.

update <class_name> <id> <attribute_name> "<attribute_value>": Updates an instance attribute and saves the change to the JSON file

Examples
Here are some examples of how to use the command interpreter:

To create a new BaseModel instance: create BaseModel
To show an instance: show BaseModel 1234-5678
To delete an instance: destroy BaseModel 1234-5678
To list all instances: all or all BaseModel
To update an attribute: update BaseModel 1234-5678 email "airbnb@mail.com"
