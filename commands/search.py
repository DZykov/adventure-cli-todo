from .command import Command
from settings import *
from functions import get_filenames
from .list import List

class Search(Command):


    def __init__(self):
        name = "search"
        description = "returns all missions with given kewword"
        usage = "search [kewword]"
        super().__init__(name, description, usage)
    
    def search(self, mission):
        missions = 0
        path = data
        filenames = get_filenames(path, remove_extension=True)
        ls = List()
        for filename in filenames:
            adv = ls.return_adventure(filename)
            for mis in adv:
                if mission in mis['name']:
                    theme.print_text(filename, ['ADVENTURE'])
                    ls._print_mission(mis)
                    missions =+ 1
        if missions == 0:
            theme.print_text("{} doesn't exists!".format(mission), ['RED', 'UNDERLINE'])
        return missions