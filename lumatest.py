from luma.core.interface.serial import spi
from luma.lcd.device import st7735
from PIL import Image, ImageDraw, ImageFont

# create SPI interface
serial = spi(port=0, device=0, gpio_DC=22, gpio_RST=27)

# create LCD device
device = st7735(serial, rotate=0)

# create an image and draw a rectangle and text on it
image = Image.new(mode="RGB", size=device.size, color=(0, 0, 0))
draw = ImageDraw.Draw(image)
draw.rectangle((10, 10, device.width - 10, device.height - 10), outline="white", fill="black")
font = ImageFont.truetype("arial.ttf", size=16)
draw.text((20, 30), "Hello, world!", font=font, fill="white")

# display the image on the LCD
device.display(image)