import requests
import json
import time
import keyboard

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
    print("Starting truth or dare game...")
    print("Please enter the desired game mode:\n't' for Truth\n'd' for Dare")
    # wait for T or D key to be pressed to select Truth or Dare

    while True:
        if keyboard.is_pressed('t'):
            ToD = "T"
            break
        elif keyboard.is_pressed('d'):
            ToD = "D"
            break
    
    print("Please enter the desired rating:\n'e' for PG\n'm' for PG13\n'h' for R")
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

    # wait for Y or N key to be pressed to continue
    print("Would you like to keep playing? Press 'y' to continue or 'n' to stop.")
    while True:
        if keyboard.is_pressed('y'):
            break
        elif keyboard.is_pressed('n'):
            break

    # debounce delay to prevent multiple key presses
    time.sleep(0.1)
