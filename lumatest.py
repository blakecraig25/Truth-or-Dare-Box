import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from st7789v import ST7789V

# create an instance of the ST7789V display with the correct settings for your display
display = ST7789V(port=0, cs=0, dc=9, backlight=None, rotation=0, spi_speed_hz=80 * 1000 * 1000)

# create a new PIL image and a drawing object
image = Image.new("RGB", (display.width, display.height), "white")
draw = ImageDraw.Draw(image)

# choose a font (you can download a font file and place it in your project directory)
font = ImageFont.load_default()

# draw some text on the image
draw.text((10, 10), "Hello, world!", font=font, fill=(0, 0, 0))

# display the image on the screen
display.display(image)
