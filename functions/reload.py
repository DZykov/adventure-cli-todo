from .get_filenames import get_filenames
from settings import *
from models import Mission
import os
import json

def load_file(filename):
    if os.path.exists(filename):
        f = open(filename)
        adv = json.load(f)
        f.close()
        return adv
    return None

def load_json(f):
    j = open(f)
    adv = json.load(j)
    j.close()
    return adv

def write_json(f, adv):
    with open(f, 'w', encoding='utf-8') as project_file:
        json.dump(
            adv,
            project_file,
            indent=4,
        )

def reload_missions():
    filenames = get_filenames(data)
    for filename in filenames:
        adv = load_file(data+filename)
        for mis in adv:
            if mis['repeat'] > 0:
                mis_obj = Mission(mis['name'], mis['checked'], repeat=mis['repeat'], checked_date=mis['checked_date'])
                mis_obj.reload()
                index = adv.index(mis)
                adv.remove(mis)
                adv.insert(index, mis_obj.get_mission())
                write_json(data+filename, adv)
