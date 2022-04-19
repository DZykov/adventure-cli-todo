# Adventure: Simple todo-cli
-    Simple todo-cli made with python. Supports multiples projects, colours, and repeated tasks. 

## Index
   - [Workflow](#Workflow "Goto Workflow")
   - [Demo](#Demo "Goto Demo")
   - [Installation](#Installation "Goto Installation")
   - [Features](#Features "Goto Features")
   - [Commands](#Commands "Goto Commands")
   - [Structure](#Structure "Goto Structure")
   - [To-Do and Issues](#To-Do-and-Issues "Goto ToDo-and-Issues")

## Workflow

![alt text](https://github.com/DZykov/adventure-cli-todo/blob/master/img/workflow.gif)

## Demo

![alt text](https://github.com/DZykov/adventure-cli-todo/blob/master/img/cmds.png)

![alt text](https://github.com/DZykov/adventure-cli-todo/blob/master/img/help.png)

## Installation
#### Build from source
You need to have python 3.8 and json installed for this option.

Clone the repo, open the folder and run the source file


    $ git clone https://github.com/DZykov/adventure-cli-todo.git
    $ cd adventure-cli-todo
    $ python3 ./adventure.py


## Features
   - Supports 7 colours, bold/italic/underline text
   - Theme management (really robust at the moment)
   - Multiple projects (aka lists of todos)
   - Repeated tasks

## Commands
| Kewword      | Arguments                                     | Explanation                             |
|--------------|-----------------------------------------------|-----------------------------------------|
| help         | none                                          | print all commands and their usage      |
| add          | add [adventure] [mission] [-r num_of_days]    |add mission to the adventure             |
| search       | search [kewword]                              | returns all missions with given kewword |
| init         | init [adventure]                              | init an adventure                       |
| archive      | atchive [adventure]                           | archive an adventure                       |
| check        | check [adventure] [mission\|all]              | check mission in the adventure          |
| uncheck      | uncheck [adventure] [mission\|all]            | uncheck mission in the adventure        |
| delete       | delete [adventure] [mission]                  | delete mission or adventure             |
| rename       | rename [adventure new_name] [-n mission name] | rename mission or adventure             |
| list         | list [adventure] [check\|uncheck\| ]          | print an aventure or all adventures     |

## Structure
- /commands contains all possible commands as objects. Every command has to have name, description, and usage.
- /data contains projects as json files. Name of the file is the name of the project.
- /functions contains helper functions.
- /settings contains theme script and config file. Config has paths to data and commands.
- reload.txt is a text file that has a date of latest reload. The date updates once a day during the first run.

## Contributing
   Feel free to use or add ;).

## To-Do and Issues
- [ ] Add daemon
- [ ] Add notifications
- [ ] Add event scheduling
    
If you would like to add to this small project or want to report an error or bug, feel free to do so!
