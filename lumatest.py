#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import sys

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import ST7735 as ST7735

# Raspberry Pi pin configuration:
RST = 27
DC = 25
SPI_PORT = 0
SPI_DEVICE = 0

# Create a new SPI device object.
spi = SPI.SpiDev()
spi.open(bus=SPI_PORT, device=SPI_DEVICE)

# Create TFT LCD display class.
disp = ST7735.ST7735(
    port=0,
    cs=1, # GPIO 18 (Pin 12)
    dc=24, # GPIO 24 (Pin 18)
    backlight=25, # GPIO 25 (Pin 22)
    rotation=0,
    spi_speed_hz=4000000)

# Initialize display.
disp.begin()

# Clear display.
disp.clear()



# Create blank image for drawing.
width = disp.width
height = disp.height
image = Image.new('RGB', (width, height), (0, 0, 0))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background.
draw.rectangle((0, 0, width, height), fill=(255, 255, 255))

# Draw a red cross.
draw.line((0, 0, width, height), fill=(255, 0, 0))
draw.line((0, height, width, 0), fill=(255, 0, 0))

# Display image.
disp.display(image)

time.sleep(10.0)

# Clear display.
disp.clear()
