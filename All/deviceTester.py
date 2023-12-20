from servo import Servo
from time import sleep


left_hand = Servo(25)
right_hand = Servo(27)



def handsDown():
    left_hand.angle(90)
    right_hand.angle(90)
    
def handsUp():
    left_hand.angle(110)
    right_hand.angle(90)
    
#handsDown()
#sleep(1)
handsUp()