from win32gui import GetWindowText, GetForegroundWindow
import writeFaders
import keyboard
import time

writeFaders.init()

ignore = ['left', 'right', 'up', 'down']

def press(a, x, i=0):
    # print(a.name)
    # print(x)
    active = GetWindowText(GetForegroundWindow())
    # print(active[:11])
    if active == 'Monitor' or active[:11] == 'Front Panel' and not a.name in ignore:
        # print('execute')
        # print(x, i)
        writeFaders.pressButton(x, i)

def release(a, x, i=0):
    # print(a.name)
    active = GetWindowText(GetForegroundWindow())
    if active == 'Monitor' or active[:11] == 'Front Panel' and not a.name in ignore:
        writeFaders.releaseButton(x, i)

def func(f, b, i=0):
    return lambda a: f(a, b, i)


keys = ['1234567890-=', 'qwertyuiop[]']
for k in range(2):
    for x in range(12):
        # print(x)'
        keyboard.on_press_key(keys[k][x], func(press, 'flash', x+24+(12*k)), suppress=False)
        keyboard.on_release_key(keys[k][x], func(release, 'flash', x+24+(12*k)), suppress=False)

keyboard.on_press_key('space', func(press, 'go'), suppress=False)
keyboard.on_release_key('space', func(release,'go'), suppress=False)

if __name__ == '__main__':
    keyboard.wait()

# while True:
#     event = keyboard.read_event()
#     print(event)