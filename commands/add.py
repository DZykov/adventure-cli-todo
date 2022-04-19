from .command import Command
from settings import *
from models import *
import os

class Add(Command):


    def __init__(self):
        name = "add"
        description = "add mission to the adventure"
        usage = "add [adventure] [mission] [-r num_of_days]"
        super().__init__(name, description, usage)
    
    def add(self, adventure, mission):
        if not self.exists_project(adventure):
            theme.print_text(adventure+" does not exist!", ['WARNING'])
            return -1
        data_mission = mission.split(' -r')
        obj_mission = None
        if len(data_mission) == 1:
            obj_mission = Mission(data_mission[0], False)
        elif len(data_mission) == 2:
            obj_mission = Mission(data_mission[0], False, repeat=int(data_mission[1]))
        adv = self.load_project(adventure)
        for mis in adv:
            if mis['name'] == data_mission[0]:
                theme.print_text("{} already exists!".format(obj_mission.name), ['WARNING'])
                return -1
        adv.append(obj_mission.get_mission())
        res = self.update_project(adventure, adv)
        if res == 1:
            m_str = str(theme.return_text(obj_mission.name, ['MISSION']))
            print("{} is added!".format(m_str))
        return -1
        