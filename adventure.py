from commands import *
from functions import reload_missions
import sys
import datetime

if __name__ == '__main__':
    try:
        diff = 0
        with open('reload.txt', 'w+', encoding='utf-8') as f:
            date_str = f.read()
            if len(date_str) == 0:
                date_str = datetime.datetime.now().strftime("%d/%m/%Y")
                f.write(date_str)
            date1 = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            date2 = datetime.datetime.now()
            date3 = date2 - date1
            diff = abs(date3.days)
        
        if diff > 0:
            with open('reload.txt', 'r+', encoding='utf-8') as f:
                f.write(datetime.datetime.now().strftime("%d/%m/%Y"))
            reload_missions()

        args = sys.argv  
        if(args[1] == 'add'):
            add.add(args[2], ' '.join(args[3:]))

        elif(args[1] == 'check'):
            check.check(args[2], ' '.join(args[3:]))

        elif(args[1] == 'delete'):
            if len(args) == 3:
                delete.delete_project(args[2])
            else:
                delete.delete_mission(args[2], ' '.join(args[3:]))

        elif(args[1] == 'help'):
            hlp.print_help()

        elif(args[1] == 'init'):
            init.init(args[2])

        elif(args[1] == 'list'):
            if len(args) == 2:
                ls.print_all()
            else:
                ls.print_adventure(args[2])

        elif(args[1] == 'rename'):
            if len(args) == 4:
                rename.rename_project(args[2], args[3])
            else:
                string = ' '.join(args[3:])
                names = string.split(' -n ')
                rename.rename_mission(args[2], names[0], names[1])

        elif(args[1] == 'search'):
            search.search(' '.join(args[2:]))

        elif(args[1] == 'uncheck'):
            uncheck.uncheck(args[2], ' '.join(args[3:]))

    except Exception as e:
        hlp.print_help()
        print(e)
