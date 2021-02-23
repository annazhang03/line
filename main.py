from display import *
from draw import *
from random import random

s = new_screen()

# first photo
n = 100 # number of squares
x = (XRES / 2 - 20) / n
for i in range(n):
    c = [random() * 255, random() * 255, random() * 255]
    c = [int(m) for m in c]
    draw_line(0 + i*x, 0 + i*x, XRES-1 - i*x, 0 + i*x, s, c)
    draw_line(XRES-1 - i*x, 0 + i*x, XRES-1 - i*x, YRES-1 - i*x, s, c)
    draw_line(XRES-1 - i*x, YRES-1 - i*x, 0 + i*x, YRES-1 - i*x, s, c)
    draw_line(0 + i*x, YRES-1 - i*x, 0 + i*x, 0 + i*x, s, c)

n = 6 # number of lines going to each edge
w = 15 # width
x = XRES / n
c = [0,0,0]
for i in range(n):
    for j in range(w):
        draw_line(XRES / 2, YRES / 2, 0 + i*x + j, 0, s, c)
        draw_line(XRES / 2, YRES / 2, XRES - 1, 0 + i*x + j, s, c)
        draw_line(XRES / 2, YRES / 2, XRES - 1 - i*x - j, YRES - 1, s, c)
        draw_line(XRES / 2, YRES / 2, 0, YRES - 1 - i*x - j, s, c)

save_extension(s, 'img1.png')

# second photo -- octant lines
clear_screen(s)
c = [0,255,0]
#octants 1 and 5
draw_line(0, 0, XRES-1, YRES-1, s, c)
draw_line(0, 0, XRES-1, YRES / 2, s, c) 
draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)

#octants 8 and 4
c[BLUE] = 255
draw_line(0, YRES-1, XRES-1, 0, s, c)
draw_line(0, YRES-1, XRES-1, YRES/2, s, c)
draw_line(XRES-1, 0, 0, YRES/2, s, c)

#octants 2 and 6
c[RED] = 255
c[GREEN] = 0
c[BLUE] = 0
draw_line(0, 0, XRES/2, YRES-1, s, c)
draw_line(XRES-1, YRES-1, XRES/2, 0, s, c)

#octants 7 and 3
c[BLUE] = 255
draw_line(0, YRES-1, XRES/2, 0, s, c)
draw_line(XRES-1, 0, XRES/2, YRES-1, s, c)

#horizontal and vertical
c[BLUE] = 0
c[GREEN] = 255
draw_line(0, YRES/2, XRES-1, YRES/2, s, c)
draw_line(XRES/2, 0, XRES/2, YRES-1, s, c)

save_extension(s, 'img2.png')
display(s)