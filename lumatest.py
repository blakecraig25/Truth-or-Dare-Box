import board
import digitalio
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont

# Define the SPI and pins
SPI_PORT = 0
SPI_DEVICE = 0
CS_PIN = digitalio.DigitalInOut(board.CE0)
DC_PIN = digitalio.DigitalInOut(board.D25)
RESET_PIN = digitalio.DigitalInOut(board.D24)

# Initialize the display
display = st7789.ST7789(
    board.SPI(),
    cs=CS_PIN,
    dc=DC_PIN,
    rst=RESET_PIN,
    baudrate=24000000,
    width=240,
    height=240,
    x_offset=0,
    y_offset=80,
)

# Initialize the buffer
image = Image.new("RGB", (240, 240), (0, 0, 0))
draw = ImageDraw.Draw(image)

# Set the font
font = ImageFont.load_default()

# Draw some text
draw.text((20, 20), "Hello, world!", font=font, fill=(255, 255, 255))

# Display the image on the screen
display.image(image)