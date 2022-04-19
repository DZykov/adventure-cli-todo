import os
from .command import Command
from settings import *
from functions import get_filenames

class Help(Command):


    def __init__(self):
        name = "help"
        description = "print all commands and their usage"
        usage = "help"
        super().__init__(name, description, usage)

    def print_help(self):
        commands = {}
        path = cmd_path
        filenames = get_filenames(path,ingore=True)
        for filename in filenames:
            with open(path+filename) as file:
                cmd_name = "No name given. File: {}".format(filename)
                cmd_description = "No description given"
                cmd_usage = "No usage given"
                for line in file:
                    if "name = " in line:
                        cmd_name = line.split("name = ")[1].replace("\"","").replace("\n", "")
                    if "description = " in line:
                        cmd_description = line.split("description = ")[1].replace("\"","").replace("\n", "")
                        commands[cmd_name] = [cmd_description]
                    if "usage = " in line:
                        cmd_usage = line.split("usage = ")[1].replace("\"","").replace("\n", "")
                        commands[cmd_name].append(cmd_usage)
                        break
        print("\n")
        for command in commands:
            theme.print_text("{}\t\t{}\n".format(command, commands[command][0]), 
                            ['CYAN'])
            theme.print_text("{}\t\t{}\n".format(" "*len(command), commands[command][1]), 
                            ['DARKCYAN', 'BOLD'])

