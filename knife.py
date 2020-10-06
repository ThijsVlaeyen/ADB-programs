from ppadb.client import Client
from PIL import Image
import numpy
import time

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

device.shell('input tap 300 450')
time.sleep(1)
device.shell(f'input touchscreen swipe 200 804 1820 200 270')
#device.shell(f'input touchscreen swipe 900 500 100 500 100')
