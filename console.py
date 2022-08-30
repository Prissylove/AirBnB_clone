#!/usr/bin/env python3
"""Entry point for the command interpreter"""
import cmd
class Console(cmd.Cmd):
    """This defines the class for console
    """
    intro = ''
    prompt = '(hbnb)'
    file  = None

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


def parse(arg):
    """ Parses arguments passed to file """
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    Console().cmdloop()
