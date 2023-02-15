from win32gui import GetWindowText, GetForegroundWindow
import writeFaders
import keyboard
import time

writeFaders.init()

ignore = ['left', 'right', 'up', 'down']

def press(a, x):
    # print(a.name)
    # print(x)
    active = GetWindowText(GetForegroundWindow())
    # print(active[:11])
    if active == 'Monitor' or active[:11] == 'Front Panel' and not a.name in ignore:
        writeFaders.pressButton('flash', x)

def release(a, x):
    # print(a.name)
    active = GetWindowText(GetForegroundWindow())
    if active == 'Monitor' or active[:11] == 'Front Panel' and not a.name in ignore:
        writeFaders.releaseButton('flash', x)

def func(f, b):
    return lambda a: f(a, b)


keys = ['1234567890-=', 'qwertyuiop[]']
for k in range(2):
    for x in range(12):
        # print(x)
        keyboard.on_press_key(keys[k][x], func(press, x+24+(12*k)), suppress=False)
        keyboard.on_release_key(keys[k][x], func(release, x+24+(12*k)), suppress=False)

keyboard.wait()

# while True:
#     event = keyboard.read_event()
#     print(event)