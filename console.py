#!/usr/bin/python3
"""Command interpreter module for AirBnB project."""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

CLASSES = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter class."""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line + ENTER."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of a class with optional parameters."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        kwargs = {}
        for param in args[1:]:
            if "=" not in param:
                continue
            key, val = param.split("=", 1)
            if val.startswith(""") and val.endswith("""):
                val = val[1:-1].replace("\"", """).replace("_", " ")
            elif "." in val:
                try:
                    val = float(val)
                except ValueError:
                    continue
            else:
                try:
                    val = int(val)
                except ValueError:
                    continue
            kwargs[key] = val

        instance = self.__classes[class_name](**kwargs)
        instance.save()
        print(instance.id)
    def do_show(self, arg):
        """Prints string representation of instance based on class and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances."""
        args = shlex.split(arg)
        objects = models.storage.all()
        result = []
        if len(args) > 0:
            if args[0] not in CLASSES:
                print("** class doesn't exist **")
                return
            for key, obj in objects.items():
                if key.split('.')[0] == args[0]:
                    result.append(str(obj))
        else:
            for obj in objects.values():
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """Updates an instance based on class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = objects[key]
        attr_name = args[2]
        attr_val = args[3]

        if attr_name in ("id", "created_at", "updated_at"):
            return

        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_val = attr_type(attr_val)
            except (ValueError, TypeError):
                pass
        else:
            if attr_val.isdigit():
                attr_val = int(attr_val)
            else:
                try:
                    attr_val = float(attr_val)
                except ValueError:
                    pass

        setattr(obj, attr_name, attr_val)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
