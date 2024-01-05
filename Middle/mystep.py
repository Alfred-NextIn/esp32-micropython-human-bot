
import machine,time
class Stepper:
    
    half_step=[ [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [1,0,1,0],
                [1,0,1,1],
                [0,0,0,1],
                [1,0,0,1] ]
    
    single_step=[ [1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1] ]
    
    single_step_backwards=[ [0,0,0,1],
                [0,0,1,0],
                [0,1,0,0],
                [1,0,0,0] ]
    
    half_step_backwards=[ [1,0,0,1],
                [0,0,0,1],
                [1,0,1,1],
                [1,0,1,0],
                [0,1,1,0],
                [0,1,0,0],
                [1,1,0,0],
                [1,0,0,0] ]
    
    full_step=[ [1,1,0,0],
                [0,1,1,0],
                [0,0,1,1],
                [0,1,0,1],
                [1,0,0,1] ]
    
    full_step_backward=[ [1,0,0,1],
                         [0,1,0,1],
                         [0,0,1,1],
                         [0,1,1,0],
                         [1,1,0,0] ]


    def __init__(self,pin1,pin2,pin3,pin4,delay):
        
        self.pin1= pin1
        self.pin2= pin2
        self.pin3= pin3
        self.pin4= pin4
        self.delay=delay  
        
        # initialize all pins to 0
        self.clrAll()
        
    def stepMode(self,mode=None):
        if mode==2:
            self.mode= self.full_step
        elif mode==0:
            self.mode= self.single_step
        elif mode==1:
            self.mode= self.single_step_backwards
        elif mode==3:
            self.mode= self.full_step_backward
        elif mode==5:
            self.mode= self.half_step_backwards
        elif mode==4:
            self.mode=self.half_step
        else:
            print("No mode selected")
        
    def move(self,count):
        
        for x in range(count):
            for state in self.mode:
                self.pin1(state[0])
                self.pin2(state[1])
                self.pin3(state[2])
                self.pin4(state[3])
                time.sleep_ms(self.delay)
        self.clrAll()
    
        
    def clrAll(self):
        self.pin1(0)
        self.pin2(0)
        self.pin3(0)
        self.pin4(0)
    
    def create(pin1,pin2, pin3, pin4, delay=2):
        return Stepper(pin1, pin2, pin3, pin4, delay)

