import ntptime
import network
import secrets
import time
import urequests
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB332
import pngdec
import random

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
print(wlan.isconnected())
  
time.sleep(10)

# Create a PicoGraphics instance
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB332)

# Set the backlight so we can see it!
display.set_backlight(1.0)

# Create some pens for use later.
BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)

# Clear the screen
display.set_pen(BLACK)
display.clear()

# Create an instance of the PNG Decoder
png = pngdec.PNG(display)
png.open_file("fuji.png")

# Decode our PNG file and set the X and Y
png.decode(0, 120, scale=1)

status = wlan.ifconfig()
ip_str = "IP: " + status[0]
ip_msk = "SM: " + status[1]
ip_gwy = "GW: " + status[2] 

# variable to keep track of the hue
h1 = 0.0

# what size steps to take around the colour wheel
OFFSET = 0.005

ntptime.settime()
x_pos = 10
y_pos = 50

while True:
    h1 += OFFSET
    now_time = (time.localtime())
    year = str(now_time[0])
    month = str(now_time[1])
    day = str(now_time[2])
    hour = str(now_time[3])
    minute = str(now_time[4])
    seconds = str(now_time[5])
    #if a number is one character pad out with a leading zero
    if len(seconds) < 2:
        seconds = '0' + seconds
    if len(minute) < 2:
        minute = '0' + minute
    if len(hour) < 2:
        hour = '0' + hour 
    display_time = (hour + ':' + minute + ':' + seconds)
    display_date = (day + ':' + month + ':' + year)
    display.set_font("cursive")
    display.set_thickness(4)
    RAINBOW = display.create_pen_hsv(h1, 1.0, 1.0)
    display.set_pen(RAINBOW)
    display.text(display_time,x_pos, y_pos, scale=2)
    display.set_pen(WHITE)
    display.set_thickness(2)
    display.text(display_date,x_pos+40, y_pos+60, scale=1)
    display.update()
    time.sleep(1)
    
    display.set_pen(BLACK)
    display.rectangle(0, 0, 320, 80)
    display.update()





