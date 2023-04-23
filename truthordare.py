import requests
import json
import time
import keyboard
import RPi.GPIO as GPIO
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import st7735


# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# Set up SPI interface
serial = spi(port=0, device=0, gpio_DC=22, gpio_RST=13, gpio=GPIO.BCM)



# Set up LCD screen
serial = spi(port=0, device=0, gpio_DC=22, gpio_RST=13, gpio=spi.GPIO.BCM)
device = ssd1306(serial)
device.clear()

font24 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 24)

def get_question(ToD, rating):
    if ToD != "T" and ToD != "D":
        print("Error: Invalid Input for Truth Or Dare.")
        return
    if rating != "PG" and rating != "PG13" and rating != "R":
        print("Error: Invalid rating.")
        return

    if ToD == "T":
        response_truth = requests.get("https://api.truthordarebot.xyz/v1/truth?rating=" + rating)
        questions_dict_truth = json.loads(response_truth.content.decode('utf-8'))
        question = questions_dict_truth['question']
    elif ToD == "D":
        response_dare = requests.get("https://api.truthordarebot.xyz/v1/dare?rating=" + rating)
        questions_dict_dare = json.loads(response_dare.content.decode('utf-8'))
        question = questions_dict_dare['question']
    
    return question

while True:
    # Display screen one
    with canvas(device) as draw:
        draw.text((10, 10), "Starting truth or dare game...", font=font24, fill='black')
        draw.text((10, 40), "Please enter the desired game mode:", font=font24, fill='black')
        draw.text((10, 70), "'t' for Truth", font=font24, fill='black')
        draw.text((10, 100), "'d' for Dare", font=font24, fill='black')
        time.sleep(2)
    # wait for T or D key to be pressed to select Truth or Dare
    while True:
        if keyboard.is_pressed('t'):
            ToD = "T"
            break
        elif keyboard.is_pressed('d'):
            ToD = "D"
            break
    
    # Display screen two
    with canvas(device) as draw:
        draw.rectangle((0, 0, device.width, device.height), fill='white')
        draw.text((10, 10), "Please enter the desired rating:", font=font24, fill='black')
        draw.text((10, 40), "'e' for PG", font=font24, fill='black')
        draw.text((10, 70), "'m' for PG13", font=font24, fill='black')
        draw.text((10, 100), "'h' for R", font=font24, fill='black')
        time.sleep(2)
    # wait for PG, PG13, or R key to be pressed to select the rating
    while True:
        if keyboard.is_pressed('e'):
            rating = "PG"
            break
        elif keyboard.is_pressed('m'):
            rating = "PG13"
            break
        elif keyboard.is_pressed('h'):
            rating = "R"
            break

    question = get_question(ToD, rating)
    if question:
        print(question)

    # Display screen three
    with canvas(device) as draw:
        draw.rectangle((0, 0, device.width, device.height), fill='white')
        draw.text((10, 10), question, font=font24, fill='black')
        draw.text((10, 40), "Would you like to keep playing?", font=font24, fill='black')
        draw.text((10, 70), "Press 'y' to continue or 'n' to stop.", font=font24, fill='black')
        time.sleep(2)
    # wait for Y or N key to be pressed to continue
    while True:
        if keyboard.is_pressed('y'):
            break
        elif keyboard.is_pressed('n'):
            break

    # debounce delay to prevent multiple key presses
