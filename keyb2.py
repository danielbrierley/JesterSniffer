from pynput import keyboard
from win32gui import GetWindowText, GetForegroundWindow
import writeFaders
import time

writeFaders.init()
def press(a, x):
    # print(a.name)
    # print(x)
    active = GetWindowText(GetForegroundWindow())
    # print(active[:11])
    if active == 'Monitor' or active[:11] == 'Front Panel':
        writeFaders.pressButton('flash', x)

def release(a, x):
    # print(a.name)
    active = GetWindowText(GetForegroundWindow())
    if active == 'Monitor' or active[:11] == 'Front Panel':
        writeFaders


keys = '1234567890-=qwertyuiop[]'

def on_press(key):
    print(f'Key {key} pressed.')
    print(str(key))


def on_release(key):
    print(f'Key {key} released.')
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()