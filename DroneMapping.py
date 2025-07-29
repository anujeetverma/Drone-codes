from pygame.examples.midi import NullKey
import keyPressModule as kp
from djitellopy import tello
import numpy as np
from time import sleep
import cv2
import math
###############################
x,y = 500,500
a=0
yaw = 0
kp.init()

me = tello.Tello()
me.connect()
print(me.get_battery())

points = []
####parameters####
fSpeed = 117/10  #forwardspeed in cm/s
aSpeed=  360/10  #anuglarspeed in deg/s
interval = 0.25   #time interval in seconds

dInterval = fSpeed*interval
aInterval = aSpeed*interval


def getKeyboardInput():
    lr,fb,up,yv =0,0,0,0
    speed = 15
    aspeed = 50
    global x,y,yaw,a
    d=0

    if(kp.getKey('a')):
        yv = -aspeed
        yaw -= aInterval
    elif(kp.getKey('d')):
        yv = aspeed
        yaw += aInterval

    if(kp.getKey('w')):
        fb = speed
        d = dInterval
        a = 270
    elif(kp.getKey('s')):
        fb = -speed
        d = -dInterval
        a = -90

    if(kp.getKey('UP')):
        up = speed
    elif(kp.getKey('DOWN')):
        up = -speed

    if(kp.getKey('LEFT')):
        lr = -speed
        d = dInterval
        a = 180


    elif(kp.getKey('RIGHT')):
        lr = speed
        d = -dInterval
        a = -180

    if(kp.getKey('q')): me.land()
    if (kp.getKey('t')): me.takeoff()
    if (kp.getKey('b')): print(me.get_battery())

    sleep(interval)
    a+=yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d*math.sin(math.radians(a)))
    return [lr,fb,up,yv,x,y]

def drawPoints(img , points):
    for point in points:
        cv2.circle(img,point,5,(255,0,255),cv2.FILLED)

    cv2.circle(img, points[-1], 7, (0, 0, 255), cv2.FILLED)
    cv2.putText(img,f'({(points[-1][0]-500)/100},{(points[-1][1]-500)/100})m',
                (points[-1][0]+10,points[-1][1]+30),cv2.FONT_HERSHEY_SIMPLEX,1,
                (0,255,255),1)
while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.01)

    img = np.zeros([1000,1000,3],np.uint8)
    points.append((vals[4],vals[5]))
    drawPoints(img , points)
    cv2.imshow('output',img)
    cv2.waitKey(1)