
import requests

NEO_PATCH = -1

prev = (-1, -1, -1, -1, -1)
def patch(dmx):
    # Code to be executed between retrieving data from PhantomJester and sending through sACN
    # Ideal for repatching one fixture to an equivalent one that is useable in Capture Student Edition
    # e.g. Mac 250 Wash to ColorWash 1200 E AT

    dmx = convWash(dmx,103)
    dmx = convWash(dmx,200)

    return dmx

# Any additional functions for patching
def convWash(dmx, addr):
    global prev
    Mac2Color = [16,17,9,10,11,7,15,1,2,3,4,5,13]
    addr -= 1
    wash = dmx[addr:addr+13]
    # print(addr)
    if addr == NEO_PATCH:
        cyan = wash[2]
        magenta = wash[3]
        yellow = wash[4]
        brightness = wash[1]/255
        red = int((255-cyan)*brightness)
        green = int((255-magenta)*brightness)
        blue = int((255-yellow)*brightness)
        if wash[5] in range(103-13, 129-13):
            red = 255
            green = 0
            blue = 0
        elif wash[5] in range(129-13, 153-13):
            red = 0
            green = 255
            blue = 0
        elif wash[5] in range(153-13, 180-13):
            red = 0
            green = 0
            blue = 255
        if (red, green, blue, wash[5], wash[1]) != prev:
            print(red, green, blue)
            url = 'http://10.233.200.209:62000/'
            myobj = {'sliders': [0, red, green, blue, 0, 255, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0]}

            try:
                x = requests.post(url, json = myobj)
            except:
                pass
            else:
                x.close()
            prev = (red, green, blue, wash[5], wash[1])
    # print(yellow, cyan, magenta)
    patchedWash = [0 for x in range(17)]
    for x in range(len(Mac2Color)):
        patchedWash[Mac2Color[x]-1] = wash[x]
    #Frost/Zoom
    patchedWash[14] = 255-patchedWash[14]
    #Dimmer
    patchedWash[16] = int(patchedWash[16]*0.5)
    #Colour Wheel
    patchedWash[6] = int(patchedWash[6]*.69)


    dmx[addr:addr+len(patchedWash)] = patchedWash
    return dmx


# Run main program
if __name__ == '__main__':
    import pygameDisplay
    pygameDisplay.main()
