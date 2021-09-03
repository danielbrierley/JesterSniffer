import sacn
import time

def init():
    global sender
    sender = sacn.sACNsender()  # provide an IP-Address to bind to if you are using Windows and want to use multicast
    sender.start()  # start the sending thread
    sender.activate_output(1)  # start sending out data in the 1st universe
    sender[1].multicast = True  # set multicast to True
    # sender[1.destination = "192.168.1.20"  # or provide unicast information.
    # Keep in mind that if multicast is on, unicast is not used

def send(data):
    sender[1].dmx_data = tuple(data)

def quit():
    sender.stop()  
