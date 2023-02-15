from ReadWriteMemory import ReadWriteMemory
import time
import math

rwm = ReadWriteMemory()

def init():
    global process
    process = rwm.get_process_by_name('PhantomJester.exe')
    process.open()

buttons = {
    'left':0x2E,
    'right':0x2F,
    'up':0x30,
    'down':0x31,
    'enter':0x32,
    'blackout':0x38,
    'insert':0x44,
    'clear':0x45,
    'edit':0x46,
    'colour':0x4F,
    'beamshape':0x50,
    'position':0x51,
    'home':0x53,
    'fixtures':0x85,
    'shift':0x99,
    'pageup':0xA5,
    'pagedown':0xA6,
    'special':0xA7,
    'go':0xA9,
    'mode':0xAA,
    'pagea':0xAB,
    'pageb':0xAC,
    'chases':0xAE,
    'tag':0xAF
}
# health_pointer = process.get_pointer(0x00462978)#, offsets=[0xf4])

# def updateBatch(values):
#     dmx = values
#     for o in range(0, len(dmx), 4):
#         dmxInt = 0
#         for x in range(4):
#             dmxInt += dmx[o+x] << (8*x)
#         process.write(0x00462978+o, dmxInt)

# def updateChanges(values):
#     global oldValues
#     dmx = values
#     for o in range(0, len(dmx)):
    #     if oldValues[o] != dmx[o]:
    #         #print(dmx[o],chr(dmx[o]))
    #         process.write(0x00462978+o, dmx[o], 1)
    # oldValues = dmx

def setFader(faderID, value):
    if faderID < 24:
        process.write(0x00462978+faderID, value, 1)
    elif faderID < 48:
        process.write(0x004629A8+faderID-24, value, 1)

def pressButton(buttonID, channel=0):
    # print(buttonID)
    if buttonID == 'all':
        for x in buttons:
            button = buttons[x]
            process.write(0x00462B00+button, 1, 1)
    elif buttonID == 'flash' and channel < 24:
        process.write(0x00462BC4+channel, 1, 1)
    elif buttonID == 'flash' and channel < 48:
        process.write(0x00462C5A+channel-24, 1, 1)
    else:
        button = buttons[buttonID]
        # print(hex(0x00462B00+button))
        process.write(0x00462B00+button, 1, 1)

def releaseButton(buttonID, channel=0):
    if buttonID == 'all':
        for x in buttons:
            button = buttons[x]
            process.write(0x00462B00+button, 0, 1)
    elif buttonID == 'flash' and channel < 24:
        process.write(0x00462BC4+channel, 0, 1)
    elif buttonID == 'flash' and channel < 48:
        process.write(0x00462C5A+channel-24, 0, 1)
    else:
        button = buttons[buttonID]
        process.write(0x00462B00+button, 0, 1)

def quit():
    process.close()


if __name__ == '__main__':
    init()
    for x in range(48):
        setFader(x, 0)
        # setFader(x, int(127*math.sin(x/2))+128)
    
    # for x in range(48):
    #     pressButton('flash', x)
    #     time.sleep(0.2)
    #     releaseButton('flash', x)
        
    pressButton('go')
    time.sleep(0.1)
    releaseButton('go')
        #process.read(0x004629A8+x) & 255
    #for x in range(24):
    #    if dmx[x] == oldDmx[x]:
    #        dmx[x] = process.read(0x00462978+x) & 255
    # updateChanges(dmx)
    quit()
