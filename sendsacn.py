import sacn

def init(universe=1):
    global sender
    sender = sacn.sACNsender()
    sender.start()
    sender.activate_output(universe)
    sender[universe].multicast = True 

def send(data):
    sender[1].dmx_data = tuple(data)

def quit():
    sender.stop()  
