from .command import Command
from settings import *
from functions import get_filenames
from functions import load_file

class List(Command):


    def __init__(self):
        name = "list"
        description = "print an adventure or all adventures"
        usage = "list [adventure|""]"
        super().__init__(name, description, usage)

    def print_all(self, prop='ALL'):
        path = data
        filenames = get_filenames(path, remove_extension=True)
        for filename in filenames:
            self.print_adventure(filename, prop=prop)
    
    def print_adventure(self, adventure, prop='ALL'):
        adv = self.return_adventure(adventure)
        if adv == -1:
            theme.print_text("Couldn't load {}...".format(adventure), ['WARNING'])
            return
        theme.print_text(adventure, ['ADVENTURE'])
        stats = [0, 0]
        for mis in adv:
            checked = self._print_mission(mis, prop=prop)
            if checked == 0:
                stats[0] += 1
            elif checked == 1:
                stats[0] += 1
                stats[1] += 1
        theme.print_text("\t{}/{}".format(stats[1], stats[0]), ['GREEN', 'ITALIC'])
    
    def _print(self,mis_name, symb, date_checked, repeat):
        print("\t", end="")
        print(symb, end=" ")
        print(mis_name)
        if date_checked != "":
            print("\t\t", end="")
            print(date_checked)
        else:
            pass
        if repeat != 0:
            print("\t\t", end="")
            print("Repeats every {} days.".format(repeat))

    def _print_mission(self, mis, prop='ALL'):
        
        symb = str(theme.return_text(theme.error, ['WARNING']))
        date_checked = ""
        checked = 0
        if mis['checked'] == True:
            symb = str(theme.return_text(theme.check, ['GREEN', 'BOLD']))
            date_checked = mis['checked_date']
            checked = 1
        elif mis['checked'] == False:
            symb = str(theme.return_text(theme.cross, ['WARNING']))
        mis_name = str(theme.return_text(mis['name'], ['MISSION']))
        if  prop=='CHECKED' and mis['checked'] == True:
            self._print(mis_name, symb, date_checked,mis['repeat'])
            return checked
        if  prop=='UNCHECKED' and mis['checked'] == False:
            self._print(mis_name, symb, date_checked,mis['repeat'])
            return checked
        if  prop=='ALL':
            self._print(mis_name, symb, date_checked,mis['repeat'])
            return checked
        return -1

    def print_archive(self):
        path = archive_folder
        filenames = get_filenames(path, remove_extension=False)
        for filename in filenames:
            adv = load_file(path+filename)
            theme.print_text(filename.replace(file_ext, ''), ['YELLOW', 'UNDERLINE', 'BOLD'])
            for mis in adv:
                theme.print_text("\t\t{}".format(mis['name']), ['YELLOW', 'UNDERLINE'])
            

    def return_adventure(self, adventure):
        adv_data = self.load_project(adventure)
        if adv_data == -1:
            return -1
        return adv_data
