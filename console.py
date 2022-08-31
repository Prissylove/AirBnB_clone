#!/usr/bin/env python3
"""Entry point for the command interpreter"""
import cmd
import re
from shlex import split

import models

# A global constant since both functions within and outside uses it.
CLASSES = [
    "BaseModel"
]


class HBNBCommand(cmd.Cmd):
    """This defines the class for console
    """

    intro = ''
    prompt = '(hbnb)'
    file = None

    def default(self, arg):
        """Default behavior for the cmd module"""
        action_map = {
            "create": self.do_create,

        }
        match = re.search(r"\.", arg)
        if match:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in action_map:
                    call = "{} {}".format(arg1[0], command[1])
                    return action_map[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, argv):
        'Responds to EOF  Command'
        print("")
        return True

    def do_quit(self, argv):
        'Exits the console'
        return True

    def emptyline(self):
        """Command to execute when empty line + <ENTER> key"""
        pass

    def do_create(self, argv):
        """Creates a new instance of the BaseModel, and saves it to `JSON`
        File and returns the id"""
        args = check_args(argv)
        if args:
            print(eval(args[0])().id)
            self.storage.save()

def parse(arg):
    """ Parses arguments passed to command """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lex]
            retl.append(brackets.group())
            return retl
    else:
        lex = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lex]
        retl.append(curly_braces.group())
        return retl


def check_args(args):
    """Checks if arguments are valid

    Args:
        args (str): the string containing the arguments passed to a command

    Returns:
        Error message if args is None or not a valid class, else the argumments
    """

    arg_list = parse(args)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list


if __name__ == '__main__':
    HBNBCommand().cmdloop()
