import requests
import json
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button_t = 14  # connect button T to GPIO14
button_d = 15  # connect button D to GPIO15
button_pg = 16  # connect button PG to GPIO16
button_pg13 = 17  # connect button PG13 to GPIO17
button_r = 18  # connect button R to GPIO18
button_yes = 19  # connect button Yes to GPIO19
button_no = 20  # connect button No to GPIO20

GPIO.setup(button_t, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_d, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pg, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pg13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_r, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_yes, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_no, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
        if not GPIO.input(button_t):
            ToD = "T"
            break
        elif not GPIO.input(button_d):
            ToD = "D"
            break

    # wait for button PG, PG13, or R to be pressed to select the rating
    while True:
        if not GPIO.input(button_pg):
            rating = "PG"
            break
        elif not GPIO.input(button_pg13):
            rating = "PG13"
            break
        elif not GPIO.input(button_r):
            rating = "R"
            break

    question = get_question(ToD, rating)
    if question:
        print(question)

    # wait for button Yes or No to be pressed to continue
    while True:
        if not GPIO.input(button_yes):
            break
        elif not GPIO.input(button_no):
            break

    # debounce delay to prevent multiple button presses
    time.sleep(0.1)
