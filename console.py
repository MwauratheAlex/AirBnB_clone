#!/usr/bin/python3
""" This module contains the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Class for the AirHBNB console """
    prompt = "(hbnb) "

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
        pass

    def do_show(self, arg):
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
        pass

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234. """
        pass

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all. """
        pass

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>" """
        pass







if __name__ == "__main__":
    HBNBCommand().cmdloop()

