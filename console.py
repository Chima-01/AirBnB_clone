#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
import cmd
import sys


""" HBNB CONSOLE
implementing a console to store and retrive data in
from json file
"""


class HBNBCommand(cmd.Cmd):
    """ creating a commandline interpreter """
    prompt = "(hbnb) "
    __classes = {'BaseModel'}
    __total_instance = storage.all()

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """ Exits console on command and sig CTRL + D"""
        print()
        return True

    def emptyline(self):
        """ do nothing if empty line passed """
        pass

    def do_create(self, args):
        """ Creates a new instance of basemodel """
        if not args:
            self.error(1)
        elif args not in self.__classes:
            self.error(2)
        else:
            total_cls = {'BaseModel': BaseModel}
            instance = total_cls[args]()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """ show instance of id and class provided"""
        if not args:
            self.error(1)
        elif len(args.split()) < 2:
            self.error(3)
        else:
            base, base_id = args.split()
            if base not in self.__classes:
                self.error(2)
                return
            base_id = base + "." + base_id
            if base_id not in self.__total_instance:
                self.error(4)
            else:
                print(self.__total_instance[base_id])

    def do_destroy(self, args):
        """Deletes an instance base on class name and id given"""
        if not args:
            self.error(1)
        elif len(args.split()) < 2:
            self.error(3)
        else:
            base, base_id = args.split()
            if base not in self.__classes:
                self.error(2)
                return
            base_id = base + "." + base_id
            if base_id not in self.__total_instance:
                self.error(4)
            else:
                del self.__total_instance[base_id]
                storage.save()

    def do_all(self, args):
        """print all instance in storage"""
        all_dict = {str(v) for v in self.__total_instance.values()}
        if not args:
            print(all_dict)
            return
        elif args in self.__classes:
            print(all_dict)
        else:
            self.error(2)

    def do_update(self, args):
        """Updates instance according to base and id given"""
        if not args:
            self.error(1)
            return False

        base_id = args.split()
        if len(base_id) < 2:
            self.error(3)
        elif len(base_id) < 3:
            print("** attribute name missing **")
        elif len(base_id) < 4:
            print("** value missing **")
        else:
            if base_id[0] not in self.__classes:
                self.error(2)
            elif f"{base_id[0]}.{base_id[1]}" not in self.__total_instance:
                self.error(4)
            else:
                instance_key = f"{base_id[0]}.{base_id[1]}"
                instance = self.__total_instance[instance_key]
                setattr(instance, base_id[2], base_id[3])
                instance.save()

    def error(self, num):
        """print error according to number given"""
        if num == 1:
            print("** class name missing **")
        elif num == 2:
            print("** class doesn't exist **")
        elif num == 3:
            print("** instance id missing **")
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
