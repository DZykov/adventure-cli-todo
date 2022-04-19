from .command import Command
from settings import *
import json
import os.path

class Init(Command):


    def __init__(self):
        name = "init"
        description = "init an adventure"
        usage = "init [adventure]"
        super().__init__(name, description, usage)
    
    def init(self, project):
        path = data
        if self.exists_project(project):
            adv = str(theme.return_text(project, ['ADVENTURE']))
            print("Adventure {} already exists!".format(adv))
            return 0
        res = self.update_project(project, [])
        adv = str(theme.return_text(project, ['ADVENTURE']))
        if res == 1:
            print("Adventure {} is created!".format(adv))
        return res
