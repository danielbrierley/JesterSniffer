# PhantomJesterOutput

This software directly reads the memory of PhantomJester v4.1, when the JesterML (or any of its variants) are used, capturing what would be the DMX output of the desk. It then outputs this data through the sACN DMX protocol. It was originally written for visualising the output in Capture 2021, but is designed in a way that the sending routine can be easily modified and replaced with an alternative.

## PhantomJester
PhantomJester is a piece of software designed to emulate the Jester range of desks by Zero88 (https://zero88.com/control/jester). it is available for download at https://zero88.com/storage/downloads/c931e8d3-b5c4-471f-9ef2-23503c964603/phantom-jester-4.1.zip. 

## Dependancies
You will need the latest version of Python 3 (written in 3.9.5)
Once that is installed, you will need to use pip to install some packages. These are pygame, ReadWriteMemory and sacn.
USe the command prompt to cd into the Python folder (usually ~\AppData\Local\Programs\Python\Python39) and run ```python.exe -m pip install *PACKAGE NAME*```

## Patching
As far as I could tell, PhantomJester doesn't store the DMX output directly in memory, it only stores patched channels, and fixtures in order of their number, and channels in the order they appear on the monitor. Because of this, the fixture patching will need to be done in readDMX.py. Start by makining a patch constant up at the top. There are 2 sample ones already there, for the Martin MAC 250 Entour and Wash. Each index in the array is the values in order they are displayed on the monitor, and the values of each index are what DMX channel that index should map to. Then under the line patching the faders, you will need the following like for each fixture: ```dmx, counter = getValues(dmx, memory, *DMX ADDRESS*, *PATCH CONSTANT*, counter)```. I recommend you include comments before each patch signifying which fixture they are for.

## Running
When using this software, run PhantomJester with a JesterML desk running first, otherwise this program will crash. Then run this program by running pygameDisplay.py. This will display a visualisation of the DMX universe in a Pygame window. Moving the mouse will show which channel and the white rectangles show the values of that channel.
