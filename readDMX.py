from ReadWriteMemory import ReadWriteMemory, ReadWriteMemoryError
import psutil, win32api

connected = False

def getDeskDLL(pid):
    try:
        p = psutil.Process(pid)
    except psutil.NoSuchProcess:
        desk = ''
    else:
        dlls = []
        desk = ''
        for dll in p.memory_maps():
            dirs = dll.path.split('\\')
            dll = dirs[len(dirs)-1]
            dlls.append(dll)
            if dll == 'Jester.dll' or dll == 'JesterML.dll':
                desk = dll
                break
    return desk

def getVersion(pid):
    p = psutil.Process(pid).memory_maps()[0].path
    info = win32api.GetFileVersionInfo(p, '\\')
    versionRaw = '%s.%s.%s.%s' % (
        info['FileVersionMS'] >> 16,
        info['FileVersionMS'] & 0xffff,
        info['FileVersionLS'] >> 16,
        info['FileVersionLS'] & 0xffff)
    if versionRaw == '2.1.0.0':
        version = '2.1'
    elif versionRaw == '1.0.0.1':
        version = '4.1'
    return version
    
def loadDeskConfig():
    global process, dmxPointer, dmxPatchPointer, memRange, ml, connected, version, desk
    desk = getDeskDLL(process.pid)
    version = getVersion(process.pid)
    #deskNamePointer = process.get_pointer(0x0364FB8A)
    #deskName = ''
    #for x in range(15):
    #    deskName = deskName + chr(process.read(deskNamePointer+x) & 255)
    if desk == 'Jester.dll':
        memRange = 48
        ml = False
        if version == '4.1':
            dmxPointer = process.get_pointer(0x1002D284)
            dmxPatchPointer = process.get_pointer(0x1002D2CC)
        elif version == '2.1':
            dmxPointer = process.get_pointer(0x100268E4)
            dmxPatchPointer = process.get_pointer(0x1002692C)
    elif desk == 'JesterML.dll': #Jester ML Config
        memRange = 512
        ml = True
        if version == '4.1':
            dmxPointer = process.get_pointer(0x1004A7F9)#, offsets=[0x00])
            dmxPatchPointer = process.get_pointer(0x1004A9F9)
        elif version == '2.1':
            dmxPointer = process.get_pointer(0x10039F28)#, offsets=[0x00])
            dmxPatchPointer = process.get_pointer(0x1003A128)
    
def init():
    global process, dmxPointer, memRange, ml, connected
    #Link to PhantomJester
    rwm = ReadWriteMemory()
    try:
        process = rwm.get_process_by_name('PhantomJester.exe')
    except ReadWriteMemoryError:
        pass
    else:
        process.open()
        try:
            desk = getDeskDLL(process.pid)
        except:
            pass
        else:
            if desk:
                try:
                    loadDeskConfig()
                except:
                    pass
                else:
                    connected = True

def quit():
    if connected:
        process.close()

def getDMX():
    global connected, patched
    patching, patched = getPatching()
    if getDeskDLL(process.pid):
        memory = getMemory()
        dmx = [0 for x in range(512)]
        #Patching
        for x in range(512):
            if patched[x]:
                dmx[x] = memory[patching[x]]
    else:
        connected = False
        dmx = [0 for x in range(512)]
    return dmx

def getPatching():
    patching = [0 for x in range(512)]
    patched = [0 for x in range(512)]
    if ml:
        for x in range(512):
            patching[x] = process.read(dmxPatchPointer+(x*2)) & 511
            patched[x] = process.read(dmxPatchPointer+(x*2)+1) & 255
    else:
        for x in range(512):
            value = process.read(dmxPatchPointer+x) & 255
            if value == 255:
                patched[x] = False
                value = 0
            else:
                patched[x] = True
            patching[x] = value
    return patching, patched

def getMemory():
    #Read PhantomJester Memory
    memory = [0 for x in range(memRange)]
    for x in range(memRange):
        memory[x] = process.read(dmxPointer+x) & 255
    return memory

if __name__ == '__main__':
    import pygameDisplay
    pygameDisplay.main()
