
#exercise 3
import mystep
from machine import Pin

In1 =Pin(21,Pin.OUT)
In2 =Pin(22,Pin.OUT)
In3 =Pin(4,Pin.OUT)
In4 =Pin(33,Pin.OUT)


s1= mystep.Stepper.create(In1,In2,In3,In4)

#all stepping modes

# while True:
#     s1.stepMode(0)
#     s1.move(300)
# 
# 
#     s1.stepMode(3)
#     s1.move(300)


# s1.stepMode(1)
# s1.move(500)
# 
# s1.stepMode(2)
# s1.move(500)
# 
# 
# s1.stepMode(4)
# s1.move(500)
# 
s1.stepMode(4)
s1.move(500)

