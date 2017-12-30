import os
import time
import subprocess
import sys
import math

#delay for 3 second
operation_delay = 1
def capture():
           op_cmd = "adb shell screencap -p /sdcard/c1.png"
           os.system(op_cmd)
           time.sleep(operation_delay);
           op_cmd = "adb pull /sdcard/c1.png"
           os.system(op_cmd)


if(len(sys.argv) >= 0):
    #option = sys.argv[1]
    capture()
