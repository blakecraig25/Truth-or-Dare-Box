from luma.core.interface.serial import spi
from luma.lcd.device import st7735

# create SPI interface
serial = spi(port=0, device=0, gpio_DC=22, gpio_RST=27)

# create LCD device
device = st7735(serial, rotate=0)

# set background color
device.clear()

# set text color
device.text_color = (255, 255, 255)

# display text
device.draw_text(10, 10, "Hello, World!")

# update display
device.display()
