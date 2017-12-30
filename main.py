import os
import time
import subprocess
import sys
import math

import Tkinter
from Tkinter import *
from PIL import Image, ImageTk
import run
import capture

def capture_game():
    capture.capture()
    global img, photo
    img = Image.open('c1.png')
    w,h = img.size
    print 'original size = ', w, ',',h
    img = resize(w, h, 360, 540, img)
    photo = ImageTk.PhotoImage(img)
    label.configure(image = photo)

def resize(w, h, w_box, h_box, pil_image):
  f1 = 1.0*w_box/w # 1.0 forces float division in Python2
  f2 = 1.0*h_box/h
  factor = min([f1, f2])
  #print(f1, f2, factor) # test
  # use best down-sizing filter
  width = int(w*factor)
  height = int(h*factor)
  return pil_image.resize((width, height), Image.ANTIALIAS)


root = Tk()
root.title('Tiao Yi Tiao')

#show image
img = Image.open('c1.png')
w,h = img.size
print 'original size = ', w, ',',h
img = resize(w, h, 360, 540, img)
photo = ImageTk.PhotoImage(img)
label = Label(root, image=photo, width=360,height=540)
label.pack()

#show capture button
button_capture = Button(root, text = "capture", command = capture_game)
button_capture.pack()

root.mainloop()
