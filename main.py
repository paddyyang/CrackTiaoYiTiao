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

def set_png(is_pull):
    if is_pull > -1:
        capture.capture()
    global img, photo, cv
    img = Image.open('c1.png')
    w,h = img.size
    print 'original size = ', w, ',',h
    img = resize(w, h, 360, 640, img)
    photo = ImageTk.PhotoImage(img)
    cv.create_image(0,0,anchor=NW,image = photo)

def capture_game():
    set_png(0)

def clear_game():
    global cv
    cv.delete("all")
    set_png(-1)

def resize(w, h, w_box, h_box, pil_image):
  f1 = 1.0*w_box/w # 1.0 forces float division in Python2
  f2 = 1.0*h_box/h
  factor = min([f1, f2])
  #print(f1, f2, factor) # test
  # use best down-sizing filter
  width = int(w*factor)
  height = int(h*factor)
  return pil_image.resize((width, height), Image.ANTIALIAS)

def distance(x0,y0,x1,y1):
    s = math.sqrt(math.pow(2*x0-2*x1,2) + math.pow(2*y0-2*y1,2))
    return 2 * round(s)

def circle(canvas, x, y, r):
    id = canvas.create_oval(x-r, y-r, x+r, y+r, fill='red')
    return id
    

line_start = False
line_complete= False
start_x = 0.0
start_y = 0.0
end_x = 0.0
end_y = 0.0
fire_distance = 0
def click_callback(event):
    print "clicked at", event.x, event.y
    global line_start, line_complete, start_x, start_y, end_x, end_y, cv
    global fire_distance
    if line_start == False:
        line_start = True
        start_x = event.x
        start_y = event.y

        circle(cv, start_x, start_y, 10)
        print "start x,y = ", start_x, ",", start_y
    elif line_start == True:
        if line_complete == False:
            line_cimplete = True
            line_start = False
            end_x = event.x
            end_y = event.y
            circle(cv, end_x, end_y, 10)
            print "end x,y = ", end_x, ",", end_y
            cv.create_line(start_x,start_y,end_x,end_y,fill='red',dash=(4,4))
            s0 = distance(start_x, start_y, end_x, end_y)
            fire_distance = int(s0)
            print "line distance:", fire_distance
        else:
                print "logic error!"

def fire_game():
    run.longpress(-1, str(fire_distance))
    time.sleep(1)
    set_png(0)



root = Tk()
root.title('Tiao Yi Tiao')

#show image
#img = Image.open('c1.png')
#w,h = img.size
#print 'original size = ', w, ',',h
#img = resize(w, h, 360, 540, img)
#photo = ImageTk.PhotoImage(img)
#label = Label(root, image=photo, width=360,height=540)
#label.pack()

cv = Canvas(root,bg = 'white', width=360, height=640)
cv.bind("<Button-1>", click_callback)
img = Image.open('c1.png')
w,h = img.size
print 'original size = ', w, ',',h
img = resize(w, h, 360, 640, img)
photo = ImageTk.PhotoImage(img)
cv.create_image(0,0,anchor=NW,image = photo)
cv.pack()

button_fire = Button(root, text = "fire", command = fire_game)
button_fire.pack()
#show capture button
button_capture = Button(root, text = "capture", command = capture_game)
button_capture.pack()

button_clear = Button(root, text = "clear", command = clear_game)
button_clear.pack()

root.mainloop()
