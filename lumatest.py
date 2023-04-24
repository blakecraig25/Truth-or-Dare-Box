#!/usr/bin/env python

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = None     # Not used for I2C interface
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# OLED display height and width in pixels
DISP_WIDTH = 128
DISP_HEIGHT = 32

# Create OLED display class
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize OLED display
disp.begin()

# Clear display
disp.clear()
disp.display()

# Create blank image for drawing
image = Image.new('1', (DISP_WIDTH, DISP_HEIGHT))

# Get drawing object to draw on image
draw = ImageDraw.Draw(image)

# Draw some text
font = ImageFont.load_default()
draw.text((0,0), "Hello World!", font=font, fill=255)

# Display image on OLED
disp.image(image)
disp.display()

time.sleep(5.0)

# Clear display
disp.clear()
disp.display()
