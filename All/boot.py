#boot.py
"""
This file will contain all the network configurations
"""

def ap():
    import network
    password = "12345"
    essid = "Robot"

    ap = network.WLAN(network.AP_IF)
    #ap.active()
    ap.config(essid=essid, password=password)
    ap.active(True)
    ip= ap.ifconfig()
    print(ip)

ap() 