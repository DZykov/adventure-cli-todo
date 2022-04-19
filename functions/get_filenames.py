import os
from settings import *

def get_filenames(path, remove_extension=False, ingore=False):
    filenames = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    if remove_extension:
        filenames = [w.replace('.json', '') for w in filenames]
        filenames = [w.replace('.py', '') for w in filenames]
    if ingore:
        for ingore in ignore_commands:
            filenames.remove(str(ingore))
    return filenames
