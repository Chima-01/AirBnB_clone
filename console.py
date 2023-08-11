import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class testCommand(cmd.Cmd):
    prompt = "(hbnb)"
    storage = FileStorage()
    storage.reload()

    def do_create(self, args):
        """Creates new instance of BaseModel, saves it
            to json file and prints the id"""
        if not args:
            print("** class name missing **")
            return

        classes_dict = {"BaseModel": BaseModel, "User": User}
        class_name = args.split()[0]
        if class_name not in classes_dict:
            print ("** class doesn't exist **")
            return

        instance = classes_dict[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Show string representation of args"""
        if not args:
            print("** class name missing **")
            return
        class_name, instance_id = args.split()
        if class_name not in classes_dict:
            print ("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        if key in testCommand.storage.all():
            print(testCommand.storage.all()[key])
        else:
            print(** no instance found **)
