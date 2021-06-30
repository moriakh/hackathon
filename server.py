from flask import Flask, render_template
from clases import Unit, Spell
import time

app = Flask(__name__)

red_belt_ninja = Unit('Red Belt Ninja', 3, 'https://tuujee.com/wp-content/uploads/2020/04/Nike-Phantom-Campaign-Art-Chun-Lo_02.jpg', 3, 4)
hard_algorithm = Spell('Hard Algorithm', 2, 'http://artgnz.weebly.com/uploads/5/6/9/0/5690416/496706982.jpg', "Increase target's resilience by 3 points", 'resilience', 3)
black_belt_ninja = Unit('Black Belt Ninja', 4, 'https://i.ytimg.com/vi/ccnxUrCCQxE/hqdefault.jpg', 5, 4)
unhandled_promise = Spell('Unhandled Promise', 2, 'https://img.artpal.com/52108/2-16-11-7-4-30-5m.jpg', "Decrease target's resilience by 2 points",'resilience', -2)
pair_programming = Spell('Pair Programming', 3, 'http://ontoborn.com/blog/wp-content/uploads/2017/07/download.jpg', "Increase target's power by 2", 'power', 2)
cards_to_show = []

def turn1():
    cards_to_show = [red_belt_ninja]
    return cards_to_show

def turn2():
    # hard_algorithm.effect(red_belt_ninja)
    cards_to_show = [hard_algorithm, red_belt_ninja]
    return cards_to_show

def turn2play():
    hard_algorithm.effect(red_belt_ninja)
    cards_to_show = [hard_algorithm, red_belt_ninja]
    return cards_to_show
    
def turn3():
    cards_to_show = [black_belt_ninja]
    return cards_to_show

def turn4():
    # unhandled_promise.effect(black_belt_ninja)
    cards_to_show = [unhandled_promise, black_belt_ninja]
    return cards_to_show

def turn4play():
    unhandled_promise.effect(black_belt_ninja)
    cards_to_show = [unhandled_promise, black_belt_ninja]
    return cards_to_show

def turn5():
    # pair_programming.effect(red_belt_ninja)
    cards_to_show = [pair_programming, red_belt_ninja]
    return cards_to_show

def turn5play():
    pair_programming.effect(red_belt_ninja)
    cards_to_show = [pair_programming, red_belt_ninja]
    return cards_to_show

def turn6():
    # red_belt_ninja.attack(black_belt_ninja)
    cards_to_show = [red_belt_ninja, black_belt_ninja]
    return cards_to_show

def turn6play():
    red_belt_ninja.attack(black_belt_ninja)
    cards_to_show = [red_belt_ninja, black_belt_ninja]
    return cards_to_show

app.cont = 0
turns_list = [turn1, turn2, turn2play, turn3, turn4, turn4play, turn5, turn5play, turn6, turn6play]

@app.route("/")
def hello_world():
    # raise Exception('Algo salió mal')

    if app.cont <= 9:
        cards_to_show = turns_list[app.cont]()
    else:
        cards_to_show = [red_belt_ninja, black_belt_ninja]
    app.cont += 1
    return render_template('index.html', cards=cards_to_show)

app.run(debug=True)