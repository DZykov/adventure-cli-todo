from .command import Command
from settings import *
from models import *
from .list import List
from .delete import Delete

class Uncheck(Command):


    def __init__(self):
        name = "uncheck"
        description = "uncheck mission in the adventure"
        usage = "uncheck [adventure] [mission|all]"
        super().__init__(name, description, usage)
    
    def uncheck(self, adventure, mission, printl=True):
        mis_data = None
        adv = self.load_project(adventure)
        if adv == -1:
            return adv
        for mis in adv:
            if mis['name'] == mission:
                mis_data = mis
                break
        if mis_data == None:
            theme.print_text("{} doesn't exist!".format(mis['name']), ['WARNING'])
            return -1
        mis_obj = Mission(mis['name'], mis['checked'], repeat=mis['repeat'], checked_date=mis['checked_date'])
        mis_obj.uncheck()
        delete = Delete()
        index = delete.delete_mission(adventure, mis['name'], printl=False)
        adv = self.load_project(adventure)
        adv.insert(index, mis_obj.get_mission())
        res = self.update_project(adventure, adv)
        if res == 1:
            if printl:
                List().print_adventure(adventure)
            return 1
        return -1

    def uncheck_all(self, adventure):
        adv = self.load_project(adventure)
        if adv == -1:
            return adv
        for mis in adv:
            self.uncheck(adventure, mis['name'], printl=False)
        List().print_adventure(adventure)