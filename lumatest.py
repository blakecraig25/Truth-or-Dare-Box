from luma.core.interface.serial import spi
from luma.lcd.device import st7735
from PIL import Image, ImageDraw, ImageFont

# create SPI interface
serial = spi(port=0, device=0, gpio_DC=22, gpio_RST=27)

# create LCD device
device = st7735(serial, rotate=0)

# create an image and draw text on it
image = Image.new(mode="RGB", size=device.size, color="white")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size=16)
draw.text((10, 10), "Hello, world!", font=font, fill="black")

# display the image on the LCD
device.display(image)

