from commands import *
from functions import *
import sys
import datetime

if __name__ == '__main__':
    try:
        diff = 0
        with open('reload.txt', 'r+', encoding='utf-8') as f:
            date_str = f.read()
            if len(date_str) == 0:
                date_str = datetime.datetime.now().strftime("%d/%m/%Y")
                f.write(date_str)
            date1 = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            date2 = datetime.datetime.now().strftime("%d/%m/%Y")
            date3 = date1 - datetime.datetime.strptime(date2, "%d/%m/%Y")
            diff = abs(date3.days)
        
        if diff > 0:
            with open('reload.txt', 'r+', encoding='utf-8') as f:
                f.write(datetime.datetime.now().strftime("%d/%m/%Y"))
            reload_missions()

        args = sys.argv  
        if(args[1] == 'add'):
            add.add(args[2], ' '.join(args[3:]))
        
        elif(args[1] == 'archive'):
            if args[2] == 'in':
                archive.move_in((args[3]))
            if args[2] == 'out':
                archive.move_out((args[3]))    

        elif(args[1] == 'check'):
            if args[3] == 'all':
                check.check_all(args[2])
            else:
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
            elif args[2] == 'archive':
                ls.print_archive()
            elif args[2] == 'check':
                ls.print_all(prop='CHECKED')
            elif args[2] == 'uncheck':
                ls.print_all(prop='UNCHECKED')
            elif args[3] == 'check':
                ls.print_adventure(args[2], prop='CHECKED')
            elif args[3] == 'uncheck':
                ls.print_adventure(args[2], prop='UNCHECKED')
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
            if args[3] == 'all':
                uncheck.uncheck_all(args[2])
            else:
                uncheck.uncheck(args[2], ' '.join(args[3:]))

    except Exception as e:
        hlp.print_help()
        print(e)
