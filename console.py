#!/usr/bin/python3

"""
Module for console
"""

import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(f"BaseModel()")
                new_instance.save()
                print(new_instance.id)
            except Exception as e:
                print(e)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            try:
                if arg[0] not in storage.classes:
                    raise KeyError
                elif len(arg) < 2:
                    print("** instance id missing **")
                else:
                    key = arg[0] + '.' + arg[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        print(storage.all()[key])
            except KeyError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            try:
                if arg[0] not in storage.classes:
                    raise KeyError
                elif len(arg) < 2:
                    print("** instance id missing **")
                else:
                    key = arg[0] + '.' + arg[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        del storage.all()[key]
                        storage.save()
            except KeyError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(value) for value in storage.all().values()])
        else:
            arg = arg.split()
            try:
                if arg[0] not in storage.classes:
                    raise KeyError
                else:
                    print([str(value) for key, value in storage.all().items() if arg[0] in key])
            except KeyError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            try:
                if arg[0] not in storage.classes:
                    raise KeyError
                elif len(arg) < 2:
                    print("** instance id missing **")
                elif len(arg) < 3:
                    print("** attribute name missing **")
                elif len(arg) < 4:
                    print("** value missing **")
                else:
                    key = arg[0] + '.' + arg[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        instance = storage.all()[key]
                        setattr(instance, arg[2], arg[3].strip('"'))
                        instance.save()
            except KeyError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
