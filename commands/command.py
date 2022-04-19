"""
This is super class for all commands.
"""

import json
import os
from settings import *

class Command:

    def __init__(self, name, description, usage):
        self.name = name
        self.description = description
        self.usage = usage

    def get_name(self):
        return name
    
    def get_description(self):
        return description

    def get_usage(self):
        return usage
    
    def update_project(self, project, jdata):
        try:
            with open(data+project+file_ext, 'w', encoding='utf-8') as project_file:
                json.dump(
                    jdata,
                    project_file,
                    indent=4,
                )
            return 1
        except:
            theme.print_text("An error has occured while updating.", ['WARNING'])
            return -1

    def exists_project(self, project):
        return os.path.exists(data+project+file_ext)

    def load_project(self, project):
        if self.exists_project(project):
            f = open(data+project+file_ext)
            jdata = json.load(f)
            f.close()
            return jdata
        theme.print_text("{} doesn't exist!".format(project), ['WARNING'])
        return -1
    