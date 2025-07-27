import keyPressModule as kp
from djitellopy import tello
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
    lr,fb,up,yv =0,0,0,0
    speed = 50
    if(kp.getKey('a')): yv = -speed
    elif(kp.getKey('d')): yv = speed

    if(kp.getKey('w')): fb = speed
    elif(kp.getKey('s')): fb = -speed

    if(kp.getKey('UP')): up = speed
    elif(kp.getKey('DOWN')): up = -speed

    if(kp.getKey('LEFT')): lr = -speed
    elif(kp.getKey('RIGHT')): lr = speed

    if(kp.getKey('q')): me.land()
    if (kp.getKey('t')): me.takeoff()
    if (kp.getKey('b')): print(me.get_battery())
    return [lr,fb,up,yv]





while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)