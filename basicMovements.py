from djitellopy import tello, Tello
import keyPressModule as kp
from time import sleep

kp.init()
me = Tello()
me.connect()


print(me.get_battery())

me.takeoff()
me.move_forward(100)
sleep(2)
me.move_right(100)
sleep(2)
me.move_back(100)
sleep(2)
me.move_left(100)
sleep(2)
me.land()


me.land()