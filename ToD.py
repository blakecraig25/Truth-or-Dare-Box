import requests
import json
import machine

button_t = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)  # connect button T to GPIO14
button_d = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)  # connect button D to GPIO15
button_pg = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)  # connect button PG to GPIO16
button_pg13 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)  # connect button PG13 to GPIO17
button_r = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)  # connect button R to GPIO18
button_yes = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)  # connect button Yes to GPIO19
button_no = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP)  # connect button No to GPIO20

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
        if not button_t.value():
            ToD = "T"
            break
        elif not button_d.value():
            ToD = "D"
            break

    # wait for button PG, PG13, or R to be pressed to select the rating
    while True:
        if not button_pg.value():
            rating = "PG"
            break
        elif not button_pg13.value():
            rating = "PG13"
            break
        elif not button_r.value():
            rating = "R"
            break

    question = get_question(ToD, rating)
    if question:
        print(question)

    # wait for button Yes or No to be pressed to continue
    while True:
        if not button_yes.value():
            break
        elif not button_no.value():
            break

