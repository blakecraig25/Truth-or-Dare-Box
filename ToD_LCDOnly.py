#API and Code Imports
import requests
import json
import time
import keyboard

#Imports from LCD
import os
import sys
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_2inch
from PIL import Image,ImageDraw,ImageFont

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0
device = 0
logging.basicConfig(level=logging.DEBUG)

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
    text_start = "Starting truth or dare game..."
    
    image1 = Image.new("RGB", (disp.height, disp.width ), "WHITE")
    draw = ImageDraw.Draw(image1)
    logging.info("draw text")
    Font3 = ImageFont.truetype("../Font/Font02.ttf",32)
    draw.rectangle([(0,65),(140,100)],fill = "WHITE")
    draw.text((5, 68), text_start, fill = "BLACK",font=Font3)

    text_q1 = "Please enter the desired game mode:\n't' for Truth\n'd' for Dare"
    # wait for T or D key to be pressed to select Truth or Dare
    
    while True:
        if keyboard.is_pressed('t'):
            ToD = "T"
            break
        elif keyboard.is_pressed('d'):
            ToD = "D"
            break
    
    text_q2 = "Please enter the desired rating:\n'e' for PG\n'm' for PG13\n'h' for R"
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
        text_response = question + "\n\nWould you like to keep playing?\n Press 'y' to continue or 'n' to stop."
        print(text_response)

    # wait for Y or N key to be pressed to continue
    while True:
        if keyboard.is_pressed('y'):
            break
        elif keyboard.is_pressed('n'):
            break

    # debounce delay to prevent multiple key presses
    time.sleep(0.1)

