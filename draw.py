from display import *
import numpy as np

def draw_line( x0, y0, x1, y1, screen, color ):
    x0,y0,x1,y1,A,B,m = reorient(x0,y0,x1,y1)
    A2 = 2 * A
    B2 = 2 * B
    x,y = x0,y0
    # vertical
    if np.isinf(m):
        while y < y1:
            plot(screen, color, x, y)
            y += 1
    # octants 1 & 5
    elif m > 0 and m <= 1:
        d = A2 + B
        while x < x1:
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += B2
            x += 1
            d += A2
    # octants 2 & 6
    elif m > 1:
        d = A + B2
        while y < y1:
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += A2
            y += 1
            d += B2
    # octants 8 & 4
    elif m < 0 and m >= -1:
        d = A2 - B
        while x < x1:
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= B2
            x += 1
            d += A2
    # octants 7 & 3
    elif m < -1:
        d = A - B2
        while y > y1:
            plot(screen, color, x,y)
            if d > 0:
                x += 1
                d += A2
            y -= 1
            d -= B2
    # horizontal
    else:
        while x < x1:
            plot(screen, color, x, y)
            x += 1

# initial and final points swapped depending on line orientation 
def reorient(x0,y0,x1,y1):
    A = int(y1 - y0)
    B = int(-(x1 - x0))
    if x0 == x1:
        x0, y0, x1, y1 = int(min(x0,x1)), int(min(y0,y1)), int(max(x0,x1)), int(max(y0,y1))
        return x0,y0,x1,y1,A,B,np.inf
    m = -A / B
    if m < 0:
        x0, y0, x1, y1 = int(min(x0,x1)), int(max(y0,y1)), int(max(x0,x1)), int(min(y0,y1))
        A, B = -abs(A), -abs(B)
    else:
        x0, y0, x1, y1 = int(min(x0,x1)), int(min(y0,y1)), int(max(x0,x1)), int(max(y0,y1))
        A, B = abs(A), -abs(B)
    return x0,y0,x1,y1,A,B,m
    