import os
import time
import subprocess
import sys
import math

#delay for 3 second
operation_delay = 1
def longpress(distance, duration):
           if distance == -1:
                   op_cmd = "adb shell input swipe 0 0 1 1 " + duration
                   os.system(op_cmd)
           else:
                   op_cmd = "adb shell input swipe 0 0 1 1 " + duration
                   os.system(op_cmd)
                    
#if(len(sys.argv) >= 0):
#    d1 = sys.argv[1]
#    d2 = sys.argv[2]
#    longpress(d1,d2)
