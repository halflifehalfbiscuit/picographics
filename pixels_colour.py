import network
import secrets
import time
import urequests
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB332
import pngdec
import random

# Create a PicoGraphics instance
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB332)

# Set the backlight so we can see it!
display.set_backlight(1.0)

# Create some pens for use later.
BG = display.create_pen(255,255,255)
TEXT = display.create_pen(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))

WIDTH, HEIGHT = display.get_bounds()



def make_circles(size):
    x_pos = 0
    y_pos = 0
    count = 1
    while count > 0:
        while x_pos < WIDTH+1:
            x_pos = (random.randrange(0,WIDTH))
            y_pos = (random.randrange(0,HEIGHT))
            TEXT = display.create_pen(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
            display.set_pen(TEXT)
            display.circle(x_pos,y_pos,random.randrange(1,size))
            display.update()
            print("x:",x_pos,"y:",y_pos)
            time.sleep(0.1)

make_circles(50)
