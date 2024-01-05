#main.py
"""
This file will contain all the air-boat control configurations and htlm for ui
"""
import sys
import socket
import time
from machine import Pin, I2C
from d1motor import Motor
from sht3x import SHT3X
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
sht30 = SHT3X()

state = "Stopped"
temperature =0
humidity = 0
speed = 0
slide_speed =500

a = Pin(22)
b = Pin(21)
i2c = I2C(1, scl= a, sda = b)

#first motor
right_motor = Motor(0,i2c)
#second motor
left_motor = Motor(1,i2c)

def Movement(r,l):
     right_motor.speed(r)
     left_motor.speed(l)


def Stop():
    right_motor.brake()
    left_motor.brake()

def sht():
    if sht30.isPresent(): #prints true is the sht is on the found on the I2C BUS
        temperature, humidity = sht30.getTempAndHumi()
        print('temp :',temperature,'humidity :',humidity)
    return temperature, humidity

def distance():
    from hcsr04 import HCSR04
    sensor = HCSR04(trigger_pin=5, echo_pin=23)
    #while True:
    distance = sensor.distance_cm()
    #print('Distance:', distance, 'cm')
    time.sleep_ms(100)
    return distance

def speedof():
    t1 = time.ticks_us()
    first_distance = distance()
    time.sleep_ms(100)
    second_distance = distance()
    t2 = time.ticks_us()
    time_difference= time.ticks_diff(t2,t1)
    total_speed = (second_distance - first_distance)/(time_difference*10**-6)
    return total_speed
    

def random_direction():
    Stop()
    import random
    random.seed(0)
    for i in range(3):
        ranval = random.randint(0,2)
    if ranval == 1:
        Movement(10000,30) #turn right
    elif ranval == 2:
        Movement(30,10000)#turn left
    else:
        Movement(10000,10000) 
        
        
def calculated_direction():
    for i in range(0,181,90):
        servo_object.angle(i)
        c_distance = distance()
        time.sleep_ms(1000)
        if i == 0:
            left_distance = c_distance
        elif i == 180:
            right_distance = c_distance
    if left_distance > right_distance or left_distance < 0:
        Movement(30,10000)   #go left
    else:
        Movement(10000,30)  #go right
        


def autonomos():
    from servo import Servo
    ervo_object= Servo()
    while True:
        getdistance = distance()
        time.sleep(1)
        if getdistance <= 5:
            #stop #turn #servo##chec distance on three sides
            calculated_direction()
        elif getdistance < 0:
            #stop#reverse#pick a direction
            stop()
            Movement(-10000,-10000)
        else:
            #keep moving forward
            random_direction()
            #Movement(10000,10000)

def servo(ang):
    try:
        from servo import Servo
        #using a default data pin of 26
        servo_object= Servo()
        servo_object.angle(ang)
    except KeyboardInterrupt:
        print("servo error")
        
        

def web_page(): 
    html = """
        <html>
            <head>
                <meta charset="utf-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <title>Air Boat</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
                <script src="main.js"></script>
                <style>
                body{
                  background-image: linear-gradient(blue, white);
                  font-family:sansarif;
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
                 #topArc{
                     border: 2px solid transparent;
                     border-radius:50px;
                     /* clip-path: polygon(100% 65%,87% 45%,51% 37%,15% 43%, 0 64%,0 85%,17% 86%,24% 69%,51% 67%,75% 68%,84% 87%,100% 87%); */
                      clip-path: polygon(0 40%,50% 0, 100% 40%,100% 100%,49% 58%,0 100%);
                 }
                @media(min-width:600px){
                 .main{
                     margin-top:-30px;
                     border: 2px solid white;
                     box-shadow:2px 2px 2px 2px gray;
                     height:195px;
                     width:18%;
                     border-radius: 70%;
                 }
                 
                 #screen{
                     width:400px;
                     height:200px;
                     background-color: black;
                     color:white;
                     margin-bottom:2%;
                    
                 }
                 
                 }
            @media(max-width: 600px){
                .main{
                     margin-top:-30px;
                     border: 2px solid white;
                     box-shadow:2px 2px 2px 2px gray;
                     height:220px;
                     width:70%;
                     border-radius: 70%;
                 }
                 #screen{
                     margin-top:10px;
                     padding:5px;
                     width:90%;
                     border:5px solid white;
                     height:170px;
                     background-color: black;
                     color:white;
                     margin-bottom:2%;
                     border-radius:10px;
                 }
                 
            }
                 .temp{
                     width:65px;
                     height:60px;
                     border-radius: 100%;
                     background-color:black;
                     color:white;
                     margin-top:40px;
                 }
                 span{
                     position:relative;
                     top:20px;
                     font-weight:bold;
                 }
                 
                 .inner{
                    text-align: left;
                 }
                 
                 .slider {
  -webkit-appearance: none;  /* Override default CSS styles */
  appearance: none;
  width: 100%; /* Full-width */
  height: 20px; /* Specified height */
  border-radius:50px;
  background: #d3d3d3; /* Grey background */
  outline: none; /* Remove outline */
  opacity: 0.7; /* Set transparency (for mouse-over effects on hover) */
  -webkit-transition: .2s; /* 0.2 seconds transition on hover */
  transition: opacity .2s;
}
/* Mouse-over effects */
.slider:hover {
  opacity: 1; /* Fully shown on mouse-over */
}
@media(min-width:800px){
    #screen{
         margin-top:100px;
         padding:5px;
         width:90%;
         border:5px solid white;
         height:250px;
         background-color: black;
         color:white;
         margin-bottom:10%;
         border-radius:10px;
    
    }
    
     .main{
     margin-top:-10px;
     border: 2px solid white;
     box-shadow:2px 2px 2px 2px gray;
     height:230px;
     width:30%;
     border-radius: 70%;
     }
     
     .tab{
     margin-top:30px;
     }
}
/* The slider handle (use -webkit- (Chrome, Opera, Safari, Edge) and -moz- (Firefox) to override default look) */
.slider::-webkit-slider-thumb {
  -webkit-appearance: none; /* Override default look */
  appearance: none;
  width: 25px; /* Set a specific slider handle width */
  height: 20px; /* Slider handle height */
  boeder-radius:50px;
  background: #000000; /* Green background */
  cursor: pointer; /* Cursor on hover */
}
.slider::-moz-range-thumb {
  width: 25px; /* Set a specific slider handle width */
  height: 20px; /* Slider handle height */
  border-radius:100%;
  background: #000000; /* Green background */
  cursor: pointer; /* Cursor on hover */
}
                </style>
            </head>
            <body>
                <center>
                    <div id="screen">
                          GROUP 4 AIRBOAT PROJECT<br>
                          <br>
                          <div class="inner">
                         Moving Status: """+ state +"""<br><br>
                         Temperature: """+ temperature +"""&deg;C<br><br>
                         Humidity: """+ humidity +"""%<br><br>
                         Speed:"""+ speed +"""cm/s<br><br>
                          </div>
                    </div>
                      <a href=\"?autonomos\">
                      <div class="auto" style="background-color:red; float:left; margin-top:-5px; font-weight:bolder; border-radius:100%; color:white; width:40px; height:40px;"><center><div style="position:relative; top:10px;">Auto</div></center></div>
                      </a>
                    <div id="topArc" style=" background-color:white; width:90%; height:120px;">
                        <div class="temp" style="float:left;"><span>"""+ temperature +"""&deg;C</span></div>
                        <div class="temp" style="float:right;"><span>"""+ humidity +"""%</span></div>
                        <div class="temp" style="margin-top:10px;"><span>"""+ speed +"""cm/s</span></div>
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
                <a href=\"?button_stop\">
                <div id="butC" style="background-color:black; width:60px; height:60px;"></div>
                </a>
                
                <a href=\"?button_down\">
                <div id="butD" style="background-color:black; width:70px; height:60px;"></div>
                </a>
                </center>
                </div>
                <br>
                <!--<div style = "width:80%; font-size:16px; font-weight:bolder;" class="tab">
                <center>Accelerator</center>
                    <input type = "range" min = "0" max = "10000" value = """+ speed +""" class="slider" step="100">
                </div>-->
            </center>
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
        
        temperature, humidity = sht()
        temperature = str(round(temperature,2))
        humidity = str(round(humidity,2))
        
        t_speed = speedof()
        speed = str(round(t_speed,2))
        print(t_speed, type(t_speed))
        
        print('Content => {}'.format(request))

        up = request.find('/?button_up')
        left = request.find('/?button_left')
        right = request.find('/?button_right')
        down = request.find('/?button_down')
        stop = request.find('/?button_stop')
        auto = request.find('/?autonomos')


        if up == 6:
            servo(90)
            state = "Forward"
            Movement(10000,10000)

        if left == 6:
            servo(170)
            state = "LEFT"
            Movement(30,10000)

        if right == 6:
            servo(10)
            state = "RIGHT"
            Movement(10000,30)
            

        if down == 6:
            servo(90)
            state = "REVERSE"
            Movement(-10000,-10000)
            
        if auto == 6:
            autonomos()
            
        if stop == 6:
            servo(90)
            state = "STOP"
            Stop()
        

        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)#.write()
        conn.close()

except KeyboardInterrupt:
    print('KeyboardInterrupt','Program stopped')
    sys.exit()