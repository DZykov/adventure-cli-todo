import datetime

class Mission:
    

    def __init__(self, name, checked, repeat=0, checked_date=''):
        self.name = name
        self.checked = checked
        self.repeat = repeat
        self.checked_date = checked_date
    
    def get_mission(self):
        return {'name': self.name,
                'checked': self.checked,
                'repeat': self.repeat,
                'checked_date': self.checked_date,
            }
        
    def check(self):
        self.checked = True
        self.checked_date = datetime.datetime.now().strftime("%d/%m/%Y")

    def uncheck(self):
        self.checked = False
        self.checked_date = ''
    
    def reload(self):
        if self.repeat == 0 or self.checked_date == '':
            return
        date1 = datetime.datetime.strptime(self.checked_date, "%d/%m/%Y")
        date2 = datetime.datetime.now()
        date3 = date2 - date1
        diff = abs(date3.days)
        if diff >= self.repeat and self.repeat != 0: # just in case
            self.uncheck()
        