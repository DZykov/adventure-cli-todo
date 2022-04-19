from .command import Command
from settings import *
from functions import get_filenames

class List(Command):


    def __init__(self):
        name = "list"
        description = "print an adventure or all adventures"
        usage = "list [adventure|""]"
        super().__init__(name, description, usage)

    def print_all(self):
        path = data
        filenames = get_filenames(path, remove_extension=True)
        for filename in filenames:
            self.print_adventure(filename)
    
    def print_adventure(self, adventure):
        adv = self.return_adventure(adventure)
        if adv == -1:
            theme.print_text("Couldn't load {}...".format(adventure), ['WARNING'])
            return
        theme.print_text(adventure, ['ADVENTURE'])
        for mis in adv:
           self._print_mission(mis)
            
    def _print_mission(self, mis):
        print("\t", end="")
        symb = str(theme.return_text(theme.error, ['WARNING']))
        date_checked = ""
        if mis['checked'] == True:
            symb = str(theme.return_text(theme.check, ['GREEN', 'BOLD']))
            date_checked = mis['checked_date']
        elif mis['checked'] == False:
            symb = str(theme.return_text(theme.cross, ['WARNING']))
        print(symb, end=" ")
        mis_name = str(theme.return_text(mis['name'], ['MISSION']))
        print(mis_name)
        if date_checked != "":
            print("\t\t", end="")
            print(date_checked)
        else:
            pass
        if mis['repeat'] != 0:
            print("\t\t", end="")
            print("Repeats every {} days.".format(mis['repeat']))

    def return_adventure(self, adventure):
        adv_data = self.load_project(adventure)
        if adv_data == -1:
            return -1
        return adv_data
