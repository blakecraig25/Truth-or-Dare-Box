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

#initial values:
ToD = " "
rate = " "
again = " "
count = 0

#disp = LCD_2inch.LCD_2inch(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
disp = LCD_2inch.LCD_2inch()
# Initialize library.
disp.Init()

def image(text, count, variable):
    # Clear display.
    disp.clear()

    # Create blank image for drawing.
    image1 = Image.new("RGB", (disp.height, disp.width ), "WHITE")
    draw = ImageDraw.Draw(image1)
    

    logging.info("draw text")
    Font3 = ImageFont.truetype("../Font/Font02.ttf",32)

    draw.rectangle([(0,65),(140,100)],fill = "WHITE")
    draw.text((5, 5), text, fill = "BLACK",font=Font3)
    image1=image1.rotate(180)
    disp.ShowImage(image1)

    if count == 1:
        while True:
            variable = input("Put in value: ")
            if variable == 't':
                variable = "T"
                return(variable)
                
            elif variable == 'd':
                variable = "D"
                return(variable)
    if count == 2:
        while True:
            variable = input("Put in value: ")
            if variable == 'e':
                variable = "PG"
                return(variable)
            elif variable == 'm':
                variable = "PG13"
                return(variable)
            elif variable == 'h':
                variable = "R"
                return(variable)
    if count == 3:
        while True:
            variable = input("Put in ""c"" to continue : ")
            if variable == 'c':
                return(question)
    if count == 4:
        while True:
            variable = input("Put in value: ")
            if variable == 'y':
                return(variable)
            elif variable == 'n':
                return(variable)
    
    return(variable)



def get_question(ToD, choice):
    if ToD != "T" and ToD != "D":
        print("Error: Invalid Input for Truth Or Dare.")
        return
    if choice != "PG" and choice != "PG13" and choice != "R":
        print("Error: Invalid rating.")
        return

    if ToD == "T":
        response_truth = requests.get("https://api.truthordarebot.xyz/v1/truth?rating=" + choice)
        questions_dict_truth = json.loads(response_truth.content.decode('utf-8'))
        question = questions_dict_truth['question']
    elif ToD == "D":
        response_dare = requests.get("https://api.truthordarebot.xyz/v1/dare?rating=" + choice)
        questions_dict_dare = json.loads(response_dare.content.decode('utf-8'))
        question = questions_dict_dare['question']
    
    return question

while True:
    text_start = "Starting truth or dare game\n..."
    count = 0
    q0 = image(text_start, count, ' ')
    time.sleep(3)
    print(q0)
    
    # wait for T or D key to be pressed to select Truth or Dare
    text_q1 = "Please enter the desired \ngame mode:\n\n't' for Truth\n'd' for Dare"
    count = 1
    q1 = image(text_q1, count, ToD)
    print(q1)
    
    # wait for PG, PG13, or R key to be pressed to select the rating
    text_q2 = "Please enter the desired \nrating:\n'e' for PG\n'm' for PG13\n'h' for R"
    count = 2
    q2 = image(text_q2, count, rate)
    print(q2)
    
    # print ToD response
    count = 3
    question = get_question(q1, q2)
    if question:
        r1 = image(question, count, ' ')
        print(r1)

    # wait for Y or N key to be pressed to continue
    count = 4
    text_response = "Would you like to keep \nplaying?\n\n'y' to continue\n'n' to stop."
    q4 = image(text_response, count, again)
    print(q4)
    while True:
        if q4 == 'y':
            break
        elif q4 == 'n':
            break
    
    # debounce delay to prevent multiple key presses
    time.sleep(0.1)

