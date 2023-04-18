import requests
import json
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

BUTTON_T = 14
BUTTON_D = 15
BUTTON_PG = 16
BUTTON_PG13 = 17
BUTTON_R = 18
BUTTON_YES = 19
BUTTON_NO = 20

GPIO.setup(BUTTON_T, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_D, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PG, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PG13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_R, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_YES, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_NO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
    # wait for button T or D to be pressed to select Truth or Dare
    while True:
        if not GPIO.input(BUTTON_T):
            ToD = "T"
            break
        elif not GPIO.input(BUTTON_D):
            ToD = "D"
            break

    # wait for button PG, PG13, or R to be pressed to select the rating
    while True:
        if not GPIO.input(BUTTON_PG):
            rating = "PG"
            break
        elif not GPIO.input(BUTTON_PG13):
            rating = "PG13"
            break
        elif not GPIO.input(BUTTON_R):
            rating = "R"
            break

    question = get_question(ToD, rating)
    if question:
        print(question)

    # wait for button Yes or No to be pressed to continue
    while True:
        if not GPIO.input(BUTTON_YES):
            break
        elif not GPIO.input(BUTTON_NO):
            break

    # display question on the screen
    # assuming the screen is connected via SPI and using the st7789 driver
    # modify the code as needed to match your actual hardware
    # ...
    # sleep for a short time to avoid continuous display updates
    sleep(0.1)
