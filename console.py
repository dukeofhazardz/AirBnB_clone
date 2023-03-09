#!/usr/bin/env python3
""" The entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The Holberton Airbnb command line"""
    prompt = '(hbnb) '
    classes = {"BaseModel", "FileStorage", "User", "State",
               "City", "Amenity", "Place", "Review"}

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id\n"""
        if len(line) == 0:
            print("** class name missing **")
            return
        elif line not in self.classes:
            print("** class doesn't exist **")
            return
        newObject = eval(line)()
        print(newObject.id)
        newObject.save()

    def do_show(self, line):
        """ Prints the string representation of an instance
        based on the class name and id\n"""
        if len(line) == 0:
            print("** class name missing **")
            return
        strings = split(line)
        if strings[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(strings) != 2:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[keyValue])

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (saves the change into the JSON file)\n"""
        if len(line) == 0:
            print("** class name missing **")
            return
        strings = split(line)
        if strings[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(strings) != 2:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[keyValue]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name"""
        if line:
            if line not in self.classes:
                print("** class doesn't exist **")
            else:
                print(["{}".format(obj) for obj in storage.all().values()
                      if line == type(obj).__name__])
            return
        print(["{}".format(obj) for obj in storage.all().values()])

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute (save the
        change into the JSON file)"""
        if len(line) == 0:
            print("** class name missing **")
            return
        strings = split(line)
        for string in strings:
            if string.startswith('"') and string.endswith('"'):
                string = string[1:-1]
        if strings[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(strings) < 2:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
            return
        if len(strings) < 3:
            print("** attribute name missing **")
            return
        if len(strings) < 4:
            print("** value missing **")
            return
        try:
            setattr(storage.all()[keyValue], strings[2], eval(strings[3]))
        except NameError:
            setattr(storage.all()[keyValue], strings[2], strings[3])

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
