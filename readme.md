# Adventure: Simple todo-cli
    Simple todo-cli made with python. Support multiples projects, colours, and repeated tasks. 

## Index
   - [Workflow](#Workflow "Goto Workflow")
   - [Demo](#Demo "Goto Demo")
   - [Installation](#Installation "Goto Installation")
   - [Features](#Features "Goto Features")
   - [Commands](#Controls "Goto Commands")
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
    $ python3 adventure.py


## Features
   - Supports 7 colours, bold/italic/underline text
   - Theme management (really robust at the moment)
   - Multiple projects (aka lists of todos)
   - Repeated tasks

## Commands
| Kewword      | Arguments          | Explanation   
|--------------|--------------------|---------------
| help         | none               | print all commands and their usage
| add          | add [adventure] [mission] [-r num_of_days]    |add mission to the adventure
| search       | search [kewword]   | returns all missions with given kewword
| init         | init [adventure]   | init an adventure
| check        | check [adventure] [mission]  | check mission in the adventure
| uncheck      | uncheck [adventure] [mission]  | uncheck mission in the adventure
| delete       | delete [adventure] [mission] | delete mission or adventure
| rename       |  rename [adventure new_name] [-n mission name] | rename mission or adventure
| list         |  list [adventure or ""] | print an aventure or all adventures

## Contributing
   This assignment was originally created for the purposes of a Computer Science Communications course, we tried our very        best to make sure it reaches professional standards but there is a possibility that it misses the mark.

## To-Do and Issues
- [ ] Add daemon
- [ ] Add notifications
- [ ] Add event scheduling
    
If you would like to add to this small project or want to report an error or bug, feel free to do so!
