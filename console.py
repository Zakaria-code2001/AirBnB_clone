#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import inspect
import importlib
import os
import models



class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    
    def do_EOF(self, args):
        """
        Quit command to exit the program
        """
        return True
    
    
    def do_quit(self,args):
        """
        Quit command to exit the program
        """
        return True
        
    def do_create(self,args):
        """
        Creates a new instance of BaseModel
        """
        "create" "BasModel"
        words = args.split()
        if len(words) == 0:
            print("** class name missing **")
            
        elif len(words) == 1:
            class_name = words[0]
            module_names = [filename[:-3] for filename in os.listdir('models') if filename.endswith('.py')]
            for module_name in module_names:
                module = importlib.import_module(f'models.{module_name}')
                classes = inspect.getmembers(module, inspect.isclass)
                class_names = [name for name, _ in classes]
                if class_name in class_names:
                    given_class = getattr(module, class_name)
                    new_instance = given_class()
                    new_instance.save()
                    print(new_instance.id)
                    return
            print("** class doesn't exist **")  
        else:
            print("** Synthaxe error **")    
            
                              
if __name__ == '__main__':
    HBNBCommand().cmdloop()
