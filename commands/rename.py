from .command import Command
from settings import *
from models import *
from .list import List
from .delete import Delete
import os

class Rename(Command):


    def __init__(self):
        name = "rename"
        description = "rename mission or adventure"
        usage = "rename [adventure |+name] [-n mission name]"
        super().__init__(name, description, usage)
    
    def rename_mission(self, adventure, mission, name):
        mis_data = None
        adv = self.load_project(adventure)
        for mis in adv:
            if mis['name'] == mission:
                mis_data = mis
                break
        if mis_data == None:
            theme.print_text("{} doesn't exist!", ['WARNING'])
            return -1
        mis_obj = Mission(mis['name'], mis['checked'], repeat=mis['repeat'], checked_date=mis['checked_date'])
        mis_obj.name = name
        delete = Delete()
        index = delete.delete_mission(adventure, mis['name'], printl=False)
        adv = self.load_project(adventure)
        adv.insert(index, mis_obj.get_mission())
        res = self.update_project(adventure, adv)
        if res == 1:
            List().print_adventure(adventure)
        return -1
    
    def rename_project(self, project, name):
        if self.exists_project(project):
            os.rename(data+project+file_ext, data+name+file_ext)
            theme.print_text("{} was renamed to {}!".format(project, name), ['YELLOW', 'BOLD'])
            return 1
        else:
            theme.print_text("The file does not exist", ['WARNING'])
            return -1