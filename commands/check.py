from .command import Command
from settings import *
from models import *
from .list import List
from .delete import Delete

class Check(Command):


    def __init__(self):
        name = "check"
        description = "uncheck mission in the adventure"
        usage = "check [adventure] [mission]"
        super().__init__(name, description, usage)
    
    def check(self, adventure, mission):
        mis_data = None
        adv = self.load_project(adventure)
        if adv == -1:
            return adv
        for mis in adv:
            if mis['name'] == mission:
                mis_data = mis
                break
        if mis_data == None:
            theme.print_text("{} doesn't exist!", ['WARNING'])
            return -1
        mis_obj = Mission(mis['name'], mis['checked'], repeat=mis['repeat'], checked_date=mis['checked_date'])
        mis_obj.check()
        delete = Delete()
        index = delete.delete_mission(adventure, mis['name'], printl=False)
        adv = self.load_project(adventure)
        adv.insert(index, mis_obj.get_mission())
        res = self.update_project(adventure, adv)
        if res == 1:
            List().print_adventure(adventure)
        return -1