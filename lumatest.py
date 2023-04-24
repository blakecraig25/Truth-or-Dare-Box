#!/usr/bin/env python

import time
import spidev
import RPi.GPIO as GPIO
from PIL import Image

# ST7789V LCD display parameters
WIDTH = 240
HEIGHT = 320
SPEED_HZ = 32000000

# Raspberry Pi pin configuration:
RST = 27
DC = 25
SPI_PORT = 0
SPI_DEVICE = 0

# Initialize SPI bus and display
spi = spidev.SpiDev()
spi.open(SPI_PORT, SPI_DEVICE)
spi.max_speed_hz = SPEED_HZ

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RST, GPIO.OUT)
GPIO.setup(DC, GPIO.OUT)

# Reset display
GPIO.output(RST, GPIO.HIGH)
time.sleep(0.1)
GPIO.output(RST, GPIO.LOW)
time.sleep(0.1)
GPIO.output(RST, GPIO.HIGH)
time.sleep(0.1)

# Send initialization commands to display
GPIO.output(DC, GPIO.LOW)
spi.writebytes([0x36, 0x00]) # Memory Data Access Control
GPIO.output(DC, GPIO.HIGH)
spi.writebytes([0x3A, 0x05]) # Interface Pixel Format
GPIO.output(DC, GPIO.LOW)
spi.writebytes([0xB2, 0x0C, 0x0C, 0x00, 0x33, 0x33]) # Porch Setting
spi.writebytes([0xB7, 0x35]) # Gate Control
spi.writebytes([0xBB, 0x2B]) # VCOM Setting
spi.writebytes([0xC0, 0x2C]) # LCM Control
spi.writebytes([0xC2, 0x01, 0xFF]) # VDV and VRH Command Enable
spi.writebytes([0xC3, 0x11]) # VRH Set
spi.writebytes([0xC4, 0x20]) # VDV Set
spi.writebytes([0xC6, 0x0F]) # Frame Rate Control
spi.writebytes([0xD0, 0xA4, 0xA1]) # Power Control 1
spi.writebytes([0xE0, 0xD0, 0x04, 0x0D, 0x11, 0x13, 0x2B, 0x3F, 0x54, 0x4C, 0x18, 0x0D, 0x0B, 0x1F, 0x23]) # Positive Gamma Control
spi.writebytes([0xE1, 0xD0, 0x04, 0x0C, 0x11, 0x13, 0x2C, 0x3F, 0x44, 0x51, 0x2F, 0x1F, 0x1F, 0x20, 0x23]) # Negative Gamma Control
spi.writebytes([0x21]) # Display Inversion On
spi.writebytes([0x11]) # Sleep Out
time.sleep(0.1)
spi.writebytes([0x29]) # Display On

# Clear display
GPIO.output(DC, GPIO.LOW)
spi.writebytes([0x2C])
for i in range(WIDTH * HEIGHT):
    spi.writebytes([0x00, 0x00])

# Function to display
