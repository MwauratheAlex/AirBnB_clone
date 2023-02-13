#!/usr/bin/python3
""" This module contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class for the AirHBNB console """
    __classes = {"BaseModel"}
    prompt = "(hbnb) "

    def validate_args(self, arg):
        """ Validates user input,
        returns the key if found,
        else returns empty string """
        key = ""
        arg_len = len(arg.split())
        if arg_len == 0:
            print("** class name missing **")
        elif arg_len >= 1 and str(arg.split()[0]) not in self.__classes:
            print("** class doesn't exist **")
        elif arg_len == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg.split()[0], arg.split()[1])
            if key not in storage.all():
                print("** no instance found **")
                key = ""
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
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel """
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
        """ Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234 """
        key = self.validate_args(line)
        if key:
            print(storage.all()[key])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234. """
        key = self.validate_args(line)
        if key:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all. """
        if not arg:
            print(storage.all())
        else:
            if str(arg) in self.__classes:
                print(storage.all())
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage:
            update <class name> <id> <attribute name> "<attribute value>" """
        key = self.validate_args(line)
        if key:
            line_len = len(line.split())
            if line_len < 3:
                print("** attribute name missing **")
            elif line_len < 4:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                attribute = line.split()[2]
                value = line.split()[3]
                setattr(obj, attribute, value)
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
