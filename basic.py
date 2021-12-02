import readDMX
import sendsacn
import patching

run = True
waiting = False
readDMX.init()
sendsacn.init()
extraPatch = True

print('Waiting for PhantomJester...')

try:
    while run:
        if waiting != readDMX.connected:
            if readDMX.connected:
                print('Connected to '+readDMX.desk+' v'+readDMX.version)
            else:
                print('Waiting for PhantomJester...')
            waiting = readDMX.connected
        if readDMX.connected:
            dmx = readDMX.getDMX()
            if extraPatch:
                dmx  = patching.patch(dmx)
            sendsacn.send(dmx)
        else:
            readDMX.init()
except KeyboardInterrupt:
    print('Quitting...')
    readDMX.quit()
    sendsacn.quit()
