# JesterSniffer

This software directly reads the memory of PhantomJester v4.1, when the JesterML (or any of its variants) are used, capturing what would be the DMX output of the desk. It then outputs this data through the sACN DMX protocol. It was originally written for visualising the output in Capture 2021, but is designed in a way that the sending routine can be easily modified and replaced with an alternative.

## PhantomJester
PhantomJester is a piece of software designed to emulate the Jester range of desks by Zero88 (https://zero88.com/control/jester). it is available for download at https://zero88.com/storage/downloads/c931e8d3-b5c4-471f-9ef2-23503c964603/phantom-jester-4.1.zip. WHile PhantomJester on it's own works in WINE on Linux, at this time JesterSniffer does not. 

## Running
To run the program open the latest release in the tab on the right and choose between main.exe or basic.exe. main.exe is a version with a Pygame-powered GUI, visualising the DMX output from the desk, and showing messages with the status of the program. basic.exe is a version without a GUI, but instead opens a Terminal window with just the status messages.

## Source Code
The source for this program was designed in a way that makes it easy to modify one particulat bit, whether it's the input, output, some tasks in-between or the whole thing

### Dependancies
You will need the latest version of Python 3 (written in 3.9.5)
Once that is installed, you will need to use pip to install some packages.
Install them with `python -m pip install -r requirements.txt`

### Modifications
The main loops for main.exe and basic.exe are in pygameDisplay.py and basic.py respecively.
readDMX.py is the script that inputs the DMX Output from the desk. getDMX() is run at the start of the loop
sendsacn.py is the script that outputs the DMX signal through the sACN protocol (a server-based DMX protocol). It is broadcasted on Universe 1 and should be detected automatically by Capture 2021. send() is run at the end of the loop
patching.py is an extra script that isn't needed, but patch() is run between the input and the output. The main purpose is so that you can modify the DMX signal between the desk and the sACN server, so that if you use the Student edition of Capture where not all fixtures are available, you can use an alternate fixture and modify the patching on-the-fly from one fixture to another. The current code in the script is to convert a MAC 250 Wash to a ColorWash 1200E AT

### Running
To run just run one of the 2 main programs. basic.py is the barebones for the program to function and just runs from the console. main.py has a Pygame-powered GUI to visualise the live DMX output which may be helpful in some situations.
