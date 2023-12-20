from machine import Pin
from machine import SPI
from  ST7735 import Display, color565
import fonts.sysfont as sysfont
from time import sleep


class RoboHead:
    def __init__(self):        
        sck = Pin(18)
        miso= Pin(19)
        mosi= Pin(23)

        SPI_CS = 26
        SPI_DC = 5
        spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
        self.display=Display(spi,SPI_CS,SPI_DC)
        self.display.clear()
        
        #colors
        self.white = color565(255,255,255)
        self.black = color565(0,0,0)


    def drawHead(self):
        self.display.clear()
        #left eye
        self.display.draw_rectangle(10,10,30,40,self.white)
        
        #right eye
        self.display.draw_rectangle(10,75,30,40,self.white)
        #eyesOpen
        self.EyesOpen()

        #nose
        self.display.draw_filledPolygon(3,58,62,15,self.white,rotate=0)
        self.display.draw_filledPolygon(4,58,62,15,self.white,rotate=0)

        #mouth
        self.display.draw_rectangle(80,27,30,73,self.white)
        self.normalMouth()
        
        #smile()
        #laugh()
        
        #main outline of the head
        self.display.draw_rectangle(0,0,125,126,self.white)

    def smilyEyes(self):
         #blush
        self.display.draw_filledEllipse(60, 20, 8, 8, color565(200,0,0))
        self.display.draw_filledEllipse(60, 100, 8, 8, color565(200,0,0))
        
         #right
        self.display.draw_filledEllipse(25,35,8,10,self.white)
        self.display.draw_filledEllipse(24,30,4,4,self.black)
        
        #left
        self.display.draw_filledEllipse(25,95,8,10,self.white)
        self.display.draw_filledEllipse(24,90,4,4,self.black)
        
    def normalMouth(self):
        polyType=4
        fromTop=94
        fromRight=[85,59,42]
        rad=19
        
        for i in fromRight:
            self.display.draw_filledPolygon(polyType,fromTop,i,rad,self.white,rotate=45)

    def destroyMouth(self):
        polyType=4
        fromTop=94
        fromRight=[85,59,42]
        rad=19
        
        for i in fromRight:
            self.display.draw_filledPolygon(polyType,fromTop,i,rad,color565(0,0,0),rotate=45)
     
     
    def laughyMouth(self):
        self.display.draw_rectangle(80,27,30,73,self.black)
        self.display.draw_ellipse(95,60,18,46,self.white)
        self.laughyTeeth()

         
    def smile(self):
        self.display.clear()
        self.drawHead()
        self.destroyMouth()
        self.smilyEyes()
        sleep(2)
        
    def laugh(self):
        self.destroyMouth()
        self.smilyEyes()
        self.laughyMouth()
        
        
    def cry(self):
        self.display.clear()
        self.drawHead()
         #right
        self.display.draw_filledEllipse(25,30,8,10,self.white)
        self.display.draw_filledEllipse(30,30,4,4,self.black)
        
        #left
        self.display.draw_filledEllipse(25,95,8,10,self.white)
        self.display.draw_filledEllipse(30,95,4,4,self.black)
        
        #tears
        for i in range(0,3,1):
            for i in range(36,85,10):
                self.display.draw_filledEllipse(i,95,3,2,self.white)
                self.display.draw_filledEllipse(i,30,3,2,self.white)
                sleep(1)
            
            for i in range(36,85,10):
                self.display.draw_filledEllipse(i,95,3,2,self.black)
                self.display.draw_filledEllipse(i,30,3,2,self.black)
        

    def EyesOpen(self):
        #right
        self.display.draw_filledEllipse(25,30,8,10,self.white)
        self.display.draw_filledEllipse(24,30,4,4,self.black)
        
        #left
        self.display.draw_filledEllipse(25,95,8,10,self.white)
        self.display.draw_filledEllipse(24,95,4,4,self.black)

    def EyesClosed(self):
        #right
        self.display.draw_filledEllipse(25,30,8,10,self.white)
        
        #left
        self.display.draw_filledEllipse(25,95,8,10,self.white)
        
    def topTooth(self):
        polyType=4
        #increase number to move down, vice versa 
        fromTop=86
        #increase number to move leftwards, vice versa 
        fromRight=[94,80,62,47,33]
        #radius of polygon
        rad=7
        for i in fromRight:
            self.display.draw_filledPolygon(polyType,fromTop,i,rad,self.white,rotate=45)
        
        
    def downTooth(self):
        polyType=4
        #increase number to move down, vice versa 
        fromTop=103
        #increase number to move leftwards, vice versa 
        fromRight=[94,79,63,48,33]
        #radius of polygon
        rad=7
        
        for i in fromRight: 
            self.display.draw_filledPolygon(polyType,fromTop,i,rad,self.white,rotate=45)

    def showTeeth(self):
        self.topTooth()
        self.downTooth()
        
        
    def mouthClose(self):
        self.display.draw_filledPolygon(4,94,87,19,self.white,rotate=45)
        self.display.draw_filledPolygon(4,94,59,19,self.white,rotate=45)
        self.display.draw_filledPolygon(4,94,42,19,self.white,rotate=45)
        
        
                
        
    def Blinker(self):        
        for i in range(0,5,1):
            #open Eyes
            self.EyesOpen()
            sleep(2)
            
            #close Eyes
            self.EyesClosed()
            sleep(0.2)
            
    def welcome(self):
        intro=["Welcome","Robot101"]
        
        for j in intro:
            self.display.draw_text(64,80, j, sysfont,color565(0,255,0), background=0,landscape=True, spacing=1, nowrap = False)
            sleep(1)
        
        
        for i in range(125,105,-5):
            self.display.draw_text(72,i , '.', sysfont,color565(0,255,0), background=0,landscape=True, spacing=1, nowrap = False)
            sleep(1)
        sleep(1)
        self.display.clear()
        
   
    def humanFace(self):
        self.display.draw_filledPolygon(4, 0, 128, 180, color565(176,109,9), rotate=45)
         #left eye

        self.display.draw_rectangle(5,15,8,30,color565(0,0,0))
        eyeL=[42,36,30,24,18]
        #eyebrouse
        for i in eyeL:
            self.display.draw_filledPolygon(4, 8, i, 4, color565(0,0,0), rotate=45)


        #right eye
        self.display.draw_rectangle(5,82,8,30,color565(0,0,0))
        eyeR=[110,104,98,92,86]
        for i in eyeR:
            self.display.draw_filledPolygon(4, 8, i, 4, color565(0,0,0), rotate=45)


         #right
        self.display.draw_filledEllipse(25,30,8,10,color565(32,233,206))
        self.display.draw_filledEllipse(24,30,4,4,color565(0,0,0))

        #left
        self.display.draw_filledEllipse(25,95,8,10,color565(32,233,206))
        self.display.draw_filledEllipse(24,95,4,4,color565(0,0,0))
        #nose
        self.display.draw_filledPolygon(3,58,62,15,color565(255,255,255),rotate=0)
        self.display.draw_filledPolygon(4,58,62,15,color565(255,255,255),rotate=0)

        #mouth
        self.display.draw_rectangle(84,27,22,73,color565(255,255,255))
        polyType=4
        #increase number to move down, vice versa 
        fromTop=94
        #increase number to move leftwards, vice versa 
        fromRight=[89,67,45,34]
        #radius of polygon
        rad=13
        for i in fromRight:
            self.display.draw_filledPolygon(polyType,fromTop,i,rad,color565(255,255,255),rotate=45)
            self.display.draw_rectangle(85,36,20,0,color565(176,109,9))
                         
            
    def laughyTeeth(self):
        polyType=4
        #increase number to move down, vice versa 
        fromTop=86
        #increase number to move leftwards, vice versa 
        fromRight=[80,66.5,52.5,39]
        #radius of polygon
        rad=7
        for i in fromRight:
            self.display.draw_filledPolygon(polyType,fromTop,i,rad,color565(255,255,255),rotate=45)
     
        
        
#         polyType=4
#         #increase number to move down, vice versa 
#         fromTop=103
#         #increase number to move leftwards, vice versa 
#         fromRight=[79,64.5,50,36]
#         #radius of polygon
#         rad=7
#         
#         for i in fromRight: 
#             self.display.draw_filledPolygon(polyType,fromTop,i,rad,color565(255,255,255),rotate=45)
#             
