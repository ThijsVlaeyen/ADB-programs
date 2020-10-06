#!/usr/bin/env python3

from ppadb.client import Client
import numpy
import time
from mss import mss

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

device.shell('input tap 532 957')

time.sleep(.5)

g = { 'left': 101, 'top': 238, 'width': 1, 'height': 1 }
y = { 'left': 115, 'top': 589, 'width': 1, 'height': 1 }
r = { 'left': 298, 'top': 252, 'width': 1, 'height': 1 }
b = { 'left': 291, 'top': 602, 'width': 1, 'height': 1 }

sct = mss()

def detect_next():

    while True:
        time.sleep(.25)

        green_pixel = numpy.array(sct.grab(g))
        yellow_pixel = numpy.array(sct.grab(y))
        red_pixel = numpy.array(sct.grab(r))
        blue_pixel = numpy.array(sct.grab(b))

        green_r = green_pixel[0][0][0]
        yellow_r = yellow_pixel[0][0][0]
        red_r = red_pixel[0][0][0]
        blue_r = blue_pixel[0][0][2]

        print(green_r, yellow_r, red_r, blue_r)

        if green_r != 0:
            return 'g'
        if yellow_r != 58:
            return 'y'
        if red_r != 0:
            return 'r'
        if blue_r != 30:
            return 'b'

moves = 1
colors = []

while True:
    for i in range(moves):
        color = detect_next()
        print(f'detected {color}')

        #colors.append(color)

    print(colors)

    time.sleep(1)

    for color in colors:
        if color == 'g':
            device.shell('input tap 300 450')
        if color == 'y':
            device.shell('input tap 300 1450')
        if color == 'r':
            device.shell('input tap 800 450')
        if color == 'b':
            device.shell('input tap 800 1450')

    moves += 1
    colors = []
