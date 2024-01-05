"""
This file will contain all the air-boat control configurations and htlm for ui
"""
import sys
import socket
import time
from time import sleep 
from machine import Pin
from servo import Servo
from random import randrange
import robotHead
#stepper imports
import mystep


#robotHeadObject
botHead=robotHead.RoboHead()

left_hand = Servo(25)
right_hand = Servo(27)

#initialization of pins for stepper
In1 =Pin(21,Pin.OUT)
In2 =Pin(22,Pin.OUT)
In3 =Pin(4,Pin.OUT)
In4 =Pin(33,Pin.OUT)

#creeating a stepper object
s1= mystep.Stepper.create(In1,In2,In3,In4)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

botHead.welcome()
botHead.drawHead()

#hands on self
def handDown():
    left_hand.angle(180)
    right_hand.angle(-40)
    sleep(1)
handDown()
#hand forward stretch
def handStretch():
    left_hand.angle(120)
    right_hand.angle(0)

#hands up
def handCheer():
    left_hand.angle(90)
    right_hand.angle(0)

#play drums
def handUp():
    left_hand.angle(0)
    right_hand.angle(90)
    
    
#hands Up    
def handDrum():
    for i in range(0,10,1):
        left_hand.angle(30)
        sleep(0.2)
        right_hand.angle(170)
        sleep(0.2)
        left_hand.angle(110)
        sleep(0.2)
        right_hand.angle(30)
        sleep(0.2)

#dance
def robotDance():
    botHead.drawHead()
    botHead.laugh()
    for i in range(0,25,1):
        left_hand.angle(randrange(0,200))
        right_hand.angle(randrange(0,200))
        sleep(0.1)

        
        
#control right Traffic    
def controlRightTraffic():
    handDown()
    botHead.smile()
    left_hand.angle(0)
    sleep(3)
    right_hand.angle(0)
    sleep(3)
    s1.stepMode(3)
    s1.move(200)
    sleep(0.5)
    handDown()

#control left Traffic
def controlLeftTraffic():
    handDown()
    botHead.smile()
    right_hand.angle(90)
    sleep(3)
    left_hand.angle(110)
    sleep(3)
    s1.stepMode(2)
    s1.move(200)
    sleep(0.5)
    handDown()

def turnLeft():
    s1.stepMode(3)
    s1.move(100)
    
def turnRight():
    #currentMode=2
    s1.stepMode(2)
    s1.move(100)
    
def turnBack():
    s1.stepMode(3)
    s1.move(100)
#dance()
    
def doThings():
    while True:
        botHead.smile()
        s1.stepMode(2)
        s1.move(100)
        sleep(1)
        s1.stepMode(2)
        s1.move(100)
        sleep(1)
        dance()
        drum()
    
def sherif():
    for i in range(0,10,1):
        left_hand.angle(30)
        sleep(1)
        right_hand.angle(160)
        left_hand.angle(180)
        sleep(1)
        right_hand.angle(0)
        
          
    
def web_page(): 
    html = """
        <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Page Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
    <script src="main.js"></script>
    <style>
        button{
            height:45px;
            margin-bottom:10px;
            margin-right:5px;
            background-color:purple;
            border:2px solid white;
            border-radius:50px;  
            color:white
        }

        button:hover{
            cursor:pointer;
            height:50px;
        }
        
         #but{
                clip-path: polygon(40% 0%, 40% 20%, 100% 20%, 100% 80%,40% 80%, 40% 100%, 0% 50%)
            }     #butUP{
                     clip-path:polygon(51% 0%,100% 50%,78% 50%, 78% 100%, 20% 100%, 20% 50%,0% 50%)
                 }
                 
                 #butR{
                     clip-path:polygon(0% 20%,60% 20%,60% 0%, 100% 50%, 60% 100%, 60% 80%,0% 80%)
                 }
                 #butD{
                     clip-path:polygon(0% 63%,19% 63%,18% 0%, 80% 0%, 81% 63%, 100% 62%,51% 100%)
                 }
                 #butC{
                     margin-top:4%;
                     margin-bottom:4%;
                     clip-path: circle(50% at 50% 50%)
                 }

         @media(max-width: 600px){
                .main{
                     margin-top:-30px;
                     border: 2px solid white;
                     box-shadow:2px 2px 2px 2px gray;
                     height:220px;
                     width:220px;
                     margin-left:20%;
                     border-radius: 70%;
                }
     
}
    
    </style>
</head>	
    <body>
            <center>
        <div style="width:100px; height:20px; border-radius:10px; padding-top:10px; border:5px solid black;">
            <center><span>ROBOT v101</span></center>

        </div>    
        </center>
    
        <center><strong>Controls</strong></center><br>
        <div  style="width:50%; height:150px; float:right; ">
            <center>
                <span><strong>Facial Expressions</strong></span>
            </center>
            <a href=\"?smile\"><button>Smile</button></a>
            <a href=\"?laugh\"><button>laugh</button></a>
            <a href=\"?normal\"><button>Normal Face</button></a>
            <a href=\"?cry\"><button>cry</button></a>
            <a href=\"?blinker\"><button>Blinker</button></a>
            <a href=\"?human_face\"><button>Human Face</button></a>
        </div>

        <div style="width:50%;">
                <center>
                        <span style="margin-bottom:20px;"><strong>Motion</strong></span>
                </center>
                <a href=\"?cheer\"> <button>Cheer</button></a>
                <a href=\"?drum\"><button>drum</button></a>
                <a href=\"?dance\"><button>Dance</button></a>
                <a href=\"?danceSherif\"><button>Sherif</button></a>
                <a href=\"?control_right\"><button>Control Right Traffic</button></a>
                <a href=\"?control_left\"><button>Control left Traffic</button></a>
                </div>
                
                
                <div class="main">
                    <center>
                <a href=\"?button_up\">    
                <div id="butUP" style="background-color:black; width:70px; height:70px;"></div>
                </a>
                <a href=\"?button_right\">
                <div id="butR" style="background-color:black; width:70px; height:70px; float:right;"></div>
                </a>
                <a href=\"?button_left\">
                <div id="but" style="background-color:black; width:70px; height:70px; float:left;"></div>
                </a>
                <a href=\"?turnBack\">
                <div id="butC" style="background-color:black; width:60px; height:60px;"></div>
                </a>
                
                <a href=\"?handDown\">
                <div id="butD" style="background-color:black; width:70px; height:60px;"></div>
                </a>
                </center>
                </div>
        </body>
        </html>
        
    """
    return html


 
try:
    while True:
        conn, addr = s.accept()
        connection_status=str(addr)
        print('Got a connection from {}'.format(connection_status))
        request = conn.recv(1024)
        request = str(request)
    
        
        print('Content => {}'.format(request))

        up = request.find('/?button_up')
        left = request.find('/?button_left')
        right = request.find('/?button_right')
        down = request.find('/?handDown')
        center = request.find('/?turnBack')
        auto = request.find('/?normal')
        smile= request.find('/?smile')
        laugh= request.find('/?laugh')
        cry= request.find('/?cry')
        blinker= request.find('/?blinker')
        human_face= request.find('/?human_face')
        cheer= request.find('/?cheer')
        drum= request.find('/?drum')
        dance= request.find('/?dance')
        things= request.find('/?danceSherif')
        controlR= request.find('/?control_right')
        controlL= request.find('/?control_left')
        

        if up == 6:
            handUp()

        if left == 6:
            turnRight()

        if right == 6:
            turnLeft()

        if center == 6:
            turnBack()
            
        if down == 6:
            handDown()
            
        if smile == 6:
            botHead.smile()
            
        if things == 6:
            sherif()    
        
        if laugh == 6:
            botHead.laugh()
        
        if cry == 6:
            botHead.cry()
            
        if auto == 6:
            botHead.drawHead()
            
        if blinker == 6:
            botHead.Blinker()
            
        if human_face == 6:
            botHead.humanFace()
            
        if cheer == 6:
            handCheer()
            
        if drum == 6:
            handDrum()
            
        if dance == 6:
            robotDance()
            
        if controlL == 6:
            controlLeftTraffic()
            
        if controlR == 6:
            controlRightTraffic()    

        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)#.write()
        conn.close()

except KeyboardInterrupt:
    print('KeyboardInterrupt','Program stopped')
    sys.exit()