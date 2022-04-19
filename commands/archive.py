from .command import Command
from .list import List
from .delete import Delete
from settings import *
from models import *
import os
import shutil

class Archive(Command):


    def __init__(self):
        name = "archive"
        description = "archive the adventure"
        usage = "archive [adventure]"
        super().__init__(name, description, usage)
    
    def create_acrhive(self):
        os.mkdir(archive_folder)
        return 1

    def check_archive(self):
        if os.path.exists(archive_folder):
            return 1
        return self.create_acrhive()
        

    def move_in(self, adventure):
        if self.check_archive() != 1:
            theme.print_text("Error while acrhive!", ['WARNING'])
            return
        adventure_path = data+adventure+file_ext
        shutil.move(adventure_path, archive_folder)
        theme.print_text("{} is archived!".format(adventure), ['CYAN', 'UNDERLINE'])
         

    def move_out(self, adventure):
        if self.check_archive() != 1:
            theme.print_text("Error while acrhive!", ['WARNING'])
            return
        adventure_path = data+adventure+file_ext
        src = archive_folder+adventure+file_ext
        shutil.move(src, adventure_path)
        theme.print_text("{} recovered!".format(adventure), ['CYAN', 'UNDERLINE'])