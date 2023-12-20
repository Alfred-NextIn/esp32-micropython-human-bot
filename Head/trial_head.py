from machine import Pin
from machine import SPI
from  ST7735 import Display, color565
import fonts.sysfont as sysfont
from time import sleep


        
sck = Pin(18)
miso= Pin(19)
mosi= Pin(23)

SPI_CS = 26
SPI_DC = 5
spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
display=Display(spi,SPI_CS,SPI_DC)
display.clear()


def topTooth():
   
def downTooth():
   
    
   
def laughtyTeeth():
     polyType=4
    #increase number to move down, vice versa 
    fromTop=86
    #increase number to move leftwards, vice versa 
    fromRight=[80,66.5,52.5,39]
    #radius of polygon
    rad=7
    for i in fromRight:
        display.draw_filledPolygon(polyType,fromTop,i,rad,color565(255,255,255),rotate=45)
 
    
    
     polyType=4
    #increase number to move down, vice versa 
    fromTop=103
    #increase number to move leftwards, vice versa 
    fromRight=[79,64.5,50,36]
    #radius of polygon
    rad=7
    
     for i in fromRight: 
        display.draw_filledPolygon(polyType,fromTop,i,rad,color565(255,255,255),rotate=45)
    

def laughyMouth():
    display.draw_ellipse(95,60,18,40,color565(255,255,255))
    showTeeth()

laughyMouth()
# polyType=4
# #increase number to move down, vice versa 
# fromTop=103
# #increase number to move leftwards, vice versa 
# fromRight=[94,79,63,48,33]
# #radius of polygon
# rad=7
# 
# for i in fromRight: 
#     display.draw_filledPolygon(polyType,fromTop,i,rad,color565(255,255,255),rotate=45)
# 
