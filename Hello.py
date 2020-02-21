# Write your code here :-)
from microbit import *

flag = True

while True:
    sleep(20)
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    print((x, y, z))
    