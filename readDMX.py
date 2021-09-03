from ReadWriteMemory import ReadWriteMemory

#DMX Patching for each channel
#Create an array for each channel in order they appear on PhantomJester, and assign each to the channel number of the fixture
#eg The first item on the monitor the dimmer and on the entour the dimmer is on channel 2
#   The second item on the monitor is colour and on the entour the colour wheel is channel 3
#   etc
ENTOUR_PATCH = [2,3,1,4,6,5,8,9,15,7,11,10,13,12,14]
WASH_PATCH = [2,3,4,5,6,1,7,13,9,8,11,10,12]

def init():
    global process, dmx1Pointer
    #Link to PhantomJester
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name('PhantomJester.exe')
    process.open()
    #Pointer to DMX address 1 in memory
    dmx1Pointer = process.get_pointer(0x1004A7F9)#, offsets=[0x00])

def quit():
    process.close()

def getDMX():
    memory = getMemory()
    dmx = [0 for x in range(512)]
    #FADERS
    dmx, counter = getValues(dmx, memory, 1, [x for x in range(1,49)], 0) #Faders
    #FIXTURE 1
    dmx, counter = getValues(dmx, memory, 300, ENTOUR_PATCH, counter)
    #FIXTURE 2
    dmx, counter = getValues(dmx, memory,  73, ENTOUR_PATCH, counter)
    #FIXTURE 3
    dmx, counter = getValues(dmx, memory, 200,   WASH_PATCH, counter)
    #FIXTURE 4
    dmx, counter = getValues(dmx, memory, 103,   WASH_PATCH, counter)
    return dmx


def getValues(dmx, memory, address, PATCH, counter=0):
    #Load values from memory and patch into DMX array
    for x in range(len(PATCH)):
        dmx[address+PATCH[x]-2] = memory[counter+x]
    counter += len(PATCH)
    return dmx, counter

def getMemory():
    #Read PhantomJester Memory
    memRange = 512
    memory = [0 for x in range(memRange)]
    for x in range(memRange):
        memory[x] = process.read(dmx1Pointer+x) & 255
    return memory


if __name__ == '__main__':
    import pygameDisplay
    pygameDisplay.main()
