#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.

def init_device():
    global ev3
    global right_motor
    global line_sensor
    global touch_sensor

    ev3 = EV3Brick()


    # Initialize the gripper motor.
    global gripper_motor
    gripper_motor = Motor(Port.C)

    # Initialize the color sensor.
    line_sensor = ColorSensor(Port.S2)

    # Initialize the touch sensor.
    touch_sensor = TouchSensor(Port.S1)



def color_detect():

    # If the Touch Sensor is pressed, it will start the color sensor
    # and say the color

    # Wait until the Touch Sensor is pressed.
    while not touch_sensor.pressed():
        # yield "waiting"
        wait(10)


    # get the color sensor value
    color = line_sensor.color()

    # if color is not None
    if color == None:
        ev3.speaker.say("No color detected")
        # yield "no color detected"
        return
    
    print(color)

    # Color.BLACK, Color.BLUE, Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE, Color.BROWN
    color_name = str(color).split(".")[1].lower()
    print(color_name)
    # say the color in a whole sentence
    ev3.speaker.say("The color is " + color_name + " your majesty")
    #yield "color detected"


def run_color_detect():
    # Run the color_detect function in the background.
    ev3.speaker.say("Press the touch sensor to detect color")
    # yield "initiated color detect function"

    while True:
        color_detect()
        # yield from color_detect()

def morse_table():
    global morse_dict
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
        ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
        '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
    }

def morse_say(text: str):
    for char in text:
        if char.upper() in morse_dict:
            morse_code = morse_dict[char.upper()]
            for morse in morse_code:
                if morse == '.':
                    ev3.speaker.beep(220, 280)
                    wait(100)
                elif morse == '-':
                    ev3.speaker.beep(220, 500)
                    wait(100)
                else:
                    wait(500)
        else:
            wait(500)

def international_spell_table():
    global international_spell_dict
    international_spell_dict = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf',
        'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November',
        'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
        'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu',
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
        '8': 'Eight', '9': 'Nine',
        '.': 'Stop', ',': 'Comma', '?': 'Question mark', "'": 'Apostrophe', '!': 'Exclamation mark', '/': 'Slash',
        '(': 'Left parenthesis', ')': 'Right parenthesis', '&': 'Ampersand', ':': 'Colon', ';': 'Semicolon',
        '=': 'Equal', '+': 'Plus', '-': 'Hyphen', '_': 'Underscore', '"': 'Quotation mark', '$': 'Dollar sign',
        '@': 'At sign'
    }

def international_spell_say(text: str):
    for char in text:
        if char.upper() in international_spell_dict:
            spell = international_spell_dict[char.upper()]
            ev3.speaker.say(spell)
        else:
            wait(500)


def learn_gripper():
    global gripper_pos_closed
    global gripper_pos_open
    gripper_pos_closed = gripper_motor.angle()
    gripper_pos_open = gripper_pos_closed - 120


def open_gripper():
    gripper_motor.run_target(100, gripper_pos_open)

def close_gripper():
    gripper_motor.run_target(150, gripper_pos_closed)

def run_gripper():
    ev3.speaker.say("Press the touch sensor to open the gripper")
    while True:
        if touch_sensor.pressed():
            open_gripper()
            ev3.speaker.say("Gripper opened")
            wait(1000)
            close_gripper()
            ev3.speaker.say("Gripper closed")
            wait(1000)


init_device()
morse_table()
international_spell_table()
learn_gripper()

# morse_say("Hi EV3")
# international_spell_say("Hi EV3")


# run_color_detect()
run_gripper()

