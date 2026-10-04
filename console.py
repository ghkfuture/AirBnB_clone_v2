#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console """
    prompt = '(hbnb) ' if sys.stdin.isatty() else ''

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def do_EOF(self, arg):
        """ Method to exit the HBNB console """
        print()
        exit()

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def _parse_params(self, args):
        """ Parses key=value arguments for do_create """
        new_dict = {}
        for arg in args:
            if '=' in arg:
                key, val = arg.split('=', 1)
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1].replace('_', ' ').replace('\\"', '"')
                elif '.' in val:
                    try:
                        val = float(val)
                    except ValueError:
                        continue
                else:
                    try:
                        val = int(val)
                    except ValueError:
                        continue
                new_dict[key] = val
        return new_dict

    def do_create(self, arg):
        """ Create an object of any class """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        kwargs = self._parse_params(args[1:])
        instance = classes[class_name](**kwargs)
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """ Show an instance based on class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """ Delete an instance based on class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return
        models.storage.all().pop(key)
        models.storage.save()

    def do_all(self, arg):
        """ Shows all objects, or all objects of a class """
        args = arg.split()
        obj_list = []
        if args:
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            for k, v in models.storage.all(classes[args[0]]).items():
                obj_list.append(str(v))
        else:
            for k, v in models.storage.all().items():
                obj_list.append(str(v))
        print(obj_list)

    def do_update(self, arg):
        """ Update an instance based on class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = models.storage.all()[key]
        setattr(obj, args[2], args[3])
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
