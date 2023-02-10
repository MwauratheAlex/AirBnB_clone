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

if __name__ == "__main__":
    HBNBCommand().cmdloop()

