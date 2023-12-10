#!/usr/bin/python3
from models.base_model import BaseModel
import cmd
import re
from shlex import split
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def parse(arg):
    """Parsing method for instances"""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, args):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, args):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        words = parse(args)
        if len(words) == 0:
            print("** class name missing **")
        elif words[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(words[0])().id)
            storage.save()

    def do_show(self, args):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        words = parse(args)
        objects = storage.all()
        if len(words) == 0:
            print("** class name missing **")
        elif words[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(words[0], words[1]) not in objects:
            print("** no instance found **")
        else:
            print(objects["{}.{}".format(words[0], words[1])])

    def do_destroy(self, args):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        words = parse(args)
        objects = storage.all()
        if len(words) == 0:
            print("** class name missing **")
        elif words[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(words[0], words[1]) not in objects.keys():
            print("** no instance found **")
        else:
            del objects["{}.{}".format(words[0], words[1])]
            storage.save()

    def do_all(self, args):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        words = parse(args)
        if len(words) > 0 and words[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objects = []
            for obj in storage.all().values():
                if len(words) > 0 and words[0] == obj.__class__.__name__:
                    objects.append(obj.__str__())
                elif len(words) == 0:
                    objects.append(obj.__str__())
            print(objects)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        words = parse(arg)
        objects = storage.all()

        if len(words) == 0:
            print("** class name missing **")
            return False
        if words[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(words) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(words[0], words[1]) not in objects.keys():
            print("** no instance found **")
            return False
        if len(words) == 2:
            print("** attribute name missing **")
            return False
        if len(words) == 3:
            try:
                type(eval(words[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(words) == 4:
            obj = objects["{}.{}".format(words[0], words[1])]
            if words[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[words[2]])
                obj.__dict__[words[2]] = valtype(words[3])
            else:
                obj.__dict__[words[2]] = words[3]
        elif type(eval(words[2])) == dict:
            obj = objects["{}.{}".format(words[0], words[1])]
            for k, v in eval(words[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
