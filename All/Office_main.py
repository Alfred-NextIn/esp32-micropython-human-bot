import sys
import socket
from machine import Pin
from machine import SPI
from  ST7735 import Display, color565
import fonts.sysfont as sysfont
import fonts.Broadway17x15 as Broadway17x15
from servo import Servo
from time import sleep


locker = Servo(4)

sck = Pin(18)
miso= Pin(19)
mosi= Pin(23)

SPI_CS = 26
SPI_DC = 5
spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
display=Display(spi,SPI_CS,SPI_DC)
display.clear()

locker.angle(0)
display.draw_text(10,90,"Lecturer", sysfont,color565(0,255,0), background=0,landscape=True, spacing=1, nowrap = False)
display.draw_text(25,128,"Mr.Isaac Armah Mensah", sysfont,color565(0,255,0), background=0,landscape=True, spacing=1, nowrap = False)

#first display of skeleton
display.draw_text(45,95,"STATUS", Broadway17x15,color565(0,255,0), background=0,landscape=True, spacing=0, nowrap = False)
display.draw_rectangle(65,20,30,90,color565(0,255,0))


def skeleton():
    display.clear()
    display.draw_text(10,90,"Lecturer", sysfont,color565(0,255,0), background=0,landscape=True, spacing=1, nowrap = False)
    display.draw_text(25,128,"Mr.Isaac Armah Mensah", sysfont,color565(0,255,0), background=0,landscape=True, spacing=1, nowrap = False)
    display.draw_text(45,95,"STATUS", Broadway17x15,color565(0,255,0), background=0,landscape=True, spacing=0, nowrap = False)
    display.draw_rectangle(65,20,30,90,color565(0,255,0))

def available():
    #writting in the rect
    skeleton()
    display.draw_text(75,90,"Available", sysfont,color565(0,255,0), background=0,landscape=True, spacing=1, nowrap = False)

def unavailable():
    #writting in the rect
    skeleton()
    display.draw_text(75,97,"Unavailable", sysfont,color565(255,0,0), background=0,landscape=True, spacing=1, nowrap = False)

def busy():
    #writting in the rect
    skeleton()
    display.draw_text(75,75,"Busy", sysfont,color565(255,255,0), background=0,landscape=True, spacing=2, nowrap = False)

def enter():
    skeleton()
    display.draw_text(75,80,"Enter!!", sysfont,color565(0,255,0), background=0,landscape=True, spacing=1, nowrap = False)

def respond(message):
    skeleton()
    display.draw_text(75,100,message, sysfont,color565(0,255,0), background=0,landscape=True, spacing=1, nowrap = False)

def Lock():
    locker.angle(0)
    available()

def Open():
    locker.angle(-40)
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def web_page(): 
    html = """
    <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Office Status giver</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
    <script src="main.js"></script>
    <style>
        .status{
            width:100%;
            height: 70px;
            border:1px solid black;
            margin-bottom:5%;
            font-size: 20pt;
            text-align: center;
            color: white;
            padding-top:2%;
        }
    </style>
</head>
<body>
    <div class="main">
        <center>
         <span><h2>Office Status Setter</h2></span>
         <span><h3>Status</h3></span>
       </center>
       
        <a href=\"?busy\"><button class="status" style="background-color: orange;">Busy</button></a>
        <a href=\"?avail\"><button class="status" style="background-color: green;">Available</button></a>
        <a href=\"?unavail\"><button class="status" style="background-color: red;">Unavailable</button></a>
        <br>
        <center>
            <span><h3>Command</h3></span>
        </center>
        <a href=\"?enter\"><button class="status" style="background-color: black;">Open</button></a>
        <a href=\"?locka\"><button class="status" style="background-color: blue;">Close</button></a>
    </div>
</body>
</html>"""
    
    return html
    

try:
    while True:
        conn, addr = s.accept()
        connection_status=str(addr)
        print('Got a connection from {}'.format(connection_status))
        request = conn.recv(1024)
        request = str(request)
    
        
        print('Content => {}'.format(request))

        Busy = request.find('/?busy')
        avail = request.find('/?avail')
        unavail = request.find('/?unavail')
        Enter = request.find('/?enter')
        locka= request.find('/?locka')
        
        
        if avail == 6:
            available()

        if unavail == 6:
            unavailable()
        
        if Enter == 6:
            Open()
            enter()
            
        if Busy == 6:
            busy()
            
        if locka == 6:
            Lock()
            
            
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)#.write()
        conn.close()
        
except KeyboardInterrupt:
    print('KeyboardInterrupt','Program stopped')
    sys.exit()