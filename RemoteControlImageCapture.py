import keyPressModule as kp
from djitellopy import tello
import time
import cv2
kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img
me.streamon()
#remote control
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

    if(kp.getKey('q')): me.land(); time.sleep(3)
    if (kp.getKey('t')): me.takeoff()

    if(kp.getKey('c')):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    if(kp.getKey('i')):me.flip_forward()
    if(kp.getKey('k')):me.flip_back()
    if(kp.getKey('j')):me.flip_left()
    if(kp.getKey('l')):me.flip_right()





    return [lr,fb,up,yv]





while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow('frame.jpg', img)
    cv2.waitKey(1)
    #sleep(0.05)