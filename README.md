# PhantomJesterOutput

This software directly reads the memory of PhantomJester v4.1, when the JesterML (or any of its variants) are used, capturing what would be the DMX output of the desk. It then outputs this data through the sACN DMX protocol. It was originally written for visualising the output in Capture 2021, but is designed in a way that the sending routine can be easily modified and replaced with an alternative.

## PhantomJester
PhantomJester is a piece of software designed to emulate the Jester range of desks by Zero88 (https://zero88.com/control/jester). it is available for download at https://zero88.com/storage/downloads/c931e8d3-b5c4-471f-9ef2-23503c964603/phantom-jester-4.1.zip. 

## Dependancies
You will need the latest version of Python 3 (written in 3.9.5)
Once that is installed, you will need to use pip to install some packages.
Install them with `python -m pip install -r requirements.txt`


## Running
To run just run one of the 2 main programs. basic.py is the barebones for the program to function and just runs from the console. main.py has a Pygame-powered GUI to visualise the live DMX output which may be helpful in some situations.
