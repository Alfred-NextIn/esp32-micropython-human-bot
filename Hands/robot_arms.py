from time import sleep 
from machine import Pin
from servo import Servo
from random import randrange
import robot_head
#stepper imports
import mystep
from machine import Pin

#robotHeadObject
botHead=robot_head.RoboHead()

left_hand = Servo(25)
right_hand = Servo(27)

#initialization of pins for stepper
In1 =Pin(21,Pin.OUT)
In2 =Pin(22,Pin.OUT)
In3 =Pin(4,Pin.OUT)
In4 =Pin(33,Pin.OUT)

#creeating a stepper object
s1= mystep.Stepper.create(In1,In2,In3,In4)
#currentMode=3

#hands on self
def handDown():
    left_hand.angle(180)
    right_hand.angle(0)
    sleep(1)

#hand forward stretch
def handStretch():
    left_hand.angle(90)
    right_hand.angle(110)

#hands up
def cheer():
    left_hand.angle(30)
    right_hand.angle(160)

#play drums
def drum():
    for i in range(0,16,1):
        left_hand.angle(30)
        sleep(1)
        right_hand.angle(110)
        sleep(1)
        left_hand.angle(110)
        sleep(1)
        right_hand.angle(30)
        sleep(1)
    
#hands Up    
def handUp():
    left_hand.angle(0)
    right_hand.angle(200)

#dance
def dance():
    botHead.drawHead()
    botHead.laugh()
    while True:
        left_hand.angle(randrange(0,200))
        right_hand.angle(randrange(0,200))
        sleep(0.5)

#laugh, move hands and turn around
def analogous():
    botHead.drawHead()
    botHead.laugh()
    for i in range(0,100,1):
        left_hand.angle(randrange(0,200))
        right_hand.angle(randrange(0,200))
        s1.stepMode(randrange(0,5))
        s1.move(randrange(100,150))
        
        
#control right Traffic    
def controlRightTraffic():
    handDown()
    left_hand.angle(0)
    sleep(3)
    right_hand.angle(110)
    sleep(3)
    s1.stepMode(3)
    s1.move(200)

#control left Traffic
def controlLeftTraffic():
    handDown()
    right_hand.angle(200)
    sleep(3)
    left_hand.angle(90)
    sleep(3)
    s1.stepMode(2)
    s1.move(200)

def turnLeft():
    s1.stepMode(3)
    s1.move(100)
    
def turnRight():
    #currentMode=2
    s1.stepMode(2)
    s1.move(100)
    
def turnBack():
    s1.stepMode(3)
    s1.move(360)
#     if currentMode==3:
#         s1.stepMode(currentMode)
#         s1.move(360)
#     
#     else:
#         #currentMode=2
#         s1.stepMode(2)
#         s1.move(360)
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
#tests
# handDown()
# botHead.cry()

#turnLeft()
#turnRight()
# turnBack()
# sleep(1)
#controlLeftTraffic()
# sleep(1)
#controlRightTraffic()   
# sleep(1)   
#analogous()
# sleep(1)
#dance()
# sleep(1)    
# handStretch()
# sleep(1)
# handUp()
# sleep(1)
# botHead.smile()
# botHead.Blinker()
#drum()
# sleep(1)
#cheer()
# 
# 
# print("Facial Expressions")
# botHead.cry()
botHead.smile()
# sleep(1)
#botHead.laugh()
# sleep(1)
# botHead.Blinker()
# botHead.humanFace()

#salsa
# left_hand.angle(90)
# right_hand.angle(160)
# sleep(1)
# s1.stepMode(3)
# s1.move(80)
# sleep(1)
# s1.stepMode(2)
# s1.move(80)
# sleep(1)
# #long
# s1.stepMode(3)
# s1.move(200)
doThings()
# drum()