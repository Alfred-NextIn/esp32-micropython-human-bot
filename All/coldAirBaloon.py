#exercise 1
from machine import I2C
from d1motor import Motor
import machine,time

pin=machine.Pin(21,machine.Pin.IN)
i2c=machine.I2C(1,scl=machine.Pin(22), sda=machine.Pin(21))
# device=i2c.scan()
# print(device)
A1=Motor(0,i2c)
speeds=[1000,1500,2000,3000,4000,8000,10000]


def varSpeed():
    for j in speeds:
        A1.speed(j)
        time.sleep(2)
        A1.brake()
        time.sleep(1) 
        
def varDir():
    #clockwise 
    A1.speed(10000)
    time.sleep(4)
    #Anticlockwise 
    A1.speed(-10000)
    time.sleep(4)

A1.speed(100000)        

