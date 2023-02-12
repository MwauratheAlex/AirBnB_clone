#!/usr/bin/python3
""" This module contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class for the AirHBNB console """
    __classes = {"BaseModel"}
    prompt = "(hbnb) "
    def check_exists(self, name):
        """ Checks if a class or id exists in storage """
        for obj in storage.all().values():
            if name in obj.values():
                return True
        return False

    def validate_args(self, arg):
        """ Validates user input """
        key = ""
        arg_len = len(arg.split())
        if arg_len == 0:
            print("** class name missing **")
            return False
        elif arg_len >= 1 and str(arg.split()[0]) not in self.__classes:
            print("** class doesn't exist **")
            return False
        elif arg_len == 1:
            print("** instance id missing **")
            return False
        else:
            key = "{}.{}".format(arg.split()[0], arg.split()[1])
            if key not in storage.all():
                print("** no instance found **")
                return False
        return key


    def do_EOF(self, line):
        """ Type Ctrl-D to quit """
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
        If the class name is missing, print ** class name missing ** (ex: $ create)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)"""
        if not arg:
            print("** class name missing **")
        elif str(arg) not in self.__classes:
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            model.save()
            print(model.id)
            storage.reload()

    def do_show(self, line):
        """ Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        If the class name is missing, print ** class name missing **
        (ex: $ show)
        If the class name doesn’t exist, print ** class doesn't exist **
        (ex: $ show MyModel)
        If the id is missing, print ** instance id missing ** 
        (ex: $ show BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found **
        (ex: $ show BaseModel 121212) """
        key = self.validate_args(line)
        if key != False:
            print(storage.all()[key])
            
    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234. """
        key = self.validate_args(line)
        if key != False:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all. """
        if not arg:
            print(storage.all())
        else:
            if str(arg) in self.__classes:
                print(storage.all())
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>" """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
