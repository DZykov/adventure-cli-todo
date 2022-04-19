from .command import Command
from settings import *
from models import *
from .list import List
import os

class Delete(Command):


    def __init__(self):
        name = "delete"
        description = "delete mission or adventure"
        usage = "delete [adventure] [mission]"
        super().__init__(name, description, usage)
    
    def delete_mission(self, adventure, mission, printl=True):
        mis_data = None
        adv = self.load_project(adventure)
        for mis in adv:
            if mis['name'] == mission:
                mis_data = mis
                break
        if mis_data == None:
            theme.print_text("{} doesn't exist!", ['WARNING'])
            return -1
        index = adv.index(mis_data)
        adv.remove(mis_data)
        res = self.update_project(adventure, adv)
        if res == 1 and printl:
            List().print_adventure(adventure)
        if res == 1 and not printl:
            return index
        return -1
    
    def delete_project(self, project):
        if self.exists_project(project):
            os.remove(data+project+file_ext)
            theme.print_text("{} was deleted!".format(project), ['YELLOW', 'BOLD'])
            return 1
        else:
            theme.print_text("The file does not exist", ['WARNING'])
            return -1