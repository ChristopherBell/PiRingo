# Flash Demo with an additional example for the fairy lights board

import time
import random
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

SWITCH1_PIN = 19
SWITCH2_PIN = 21
LEDS = [7, 11, 12, 13, 15, 16, 18, 22, 24, 26, 8, 10]

LEDOFF = 1
LEDON = 0
NUMLEDS = 12

def setupgpio():

    a = 0
    while a < NUMLEDS:
        GPIO.setup(LEDS[a], GPIO.OUT)
        a += 1
    GPIO.setup(SWITCH1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWITCH2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def randomflash(val):

    count = 0
    a = 0

    while count < val:
        b = random.randrange(0, NUMLEDS)
        GPIO.output(LEDS[a], LEDOFF)
        GPIO.output(LEDS[b], LEDON)

        a = b
        count += 1
        time.sleep(0.1)
    alloff()


def alloff():

    for val in LEDS:
        GPIO.output(val, LEDOFF)


def allon():

    for val in LEDS:
        GPIO.output(val, LEDON)


def chase1(val):

    a = 0
    count = 0

    while count < val:
        b = a -1

        if b < 0:
            b = NUMLEDS - 1

        GPIO.output(LEDS[b], LEDOFF)
        GPIO.output(LEDS[a], LEDON)

        a = a + 1

        if a >= NUMLEDS:
            a = 0

        time.sleep(0.1)
        count += 1


def chase2(val):

    a = 0
    c = 0
    count = 0

    while count < val:
        b = a - 1

        if b < 0:
            b = NUMLEDS - 1

        d = c + 1

        if d >= NUMLEDS:
            d = 0

        GPIO.output(LEDS[b], LEDOFF)
        GPIO.output(LEDS[a], LEDON)
        GPIO.output(LEDS[d], LEDOFF)
        GPIO.output(LEDS[c], LEDON)

        a += 1

        if a >= NUMLEDS:
            a = 0

        c -= 1

        if c < 0:
            c = NUMLEDS - 1

        time.sleep(0.1)
        count += 1
    alloff()

# Below is the code for the fairy lights board

def blue(val):

    GPIO.output(LEDS[0], val)
    GPIO.output(LEDS[5], val)
    GPIO.output(LEDS[7], val)


def red(val):

    GPIO.output(LEDS[1], val)
    GPIO.output(LEDS[6], val)
    GPIO.output(LEDS[11], val)


def yellow(val):

    GPIO.output(LEDS[2], val)
    GPIO.output(LEDS[4], val)


def clear(val):

    GPIO.output(LEDS[3], val)
    GPIO.output(LEDS[9], val)


def green(val):

    GPIO.output(LEDS[8], val)
    GPIO.output(LEDS[10], val)

# You can change the order of light
# switch on by modifying the alternate
# function below.

def alternate(val):

    count = 0

    while count < val:
        red(LEDON)
        blue(LEDOFF)
        yellow(LEDOFF)
        green(LEDOFF)
        clear(LEDOFF)

        time.sleep(0.3)

        blue(LEDON)
        red(LEDOFF)
        yellow(LEDOFF)
        green(LEDOFF)
        clear(LEDOFF)

        time.sleep(0.3)

        yellow(LEDON)
        red(LEDOFF)
        blue(LEDOFF)
        green(LEDOFF)
        clear(LEDOFF)

        time.sleep(0.3)

        green(LEDON)
        red(LEDOFF)
        blue(LEDOFF)
        yellow(LEDOFF)
        clear(LEDOFF)

        time.sleep(0.3)

        clear(LEDON)
        red(LEDOFF)
        blue(LEDOFF)
        yellow(LEDOFF)
        green(LEDOFF)

        time.sleep(0.3)
        count += 1
    alloff()


setupgpio()
alloff()
randomflash(50)
chase1(50)
chase2(50)
alternate(20)

GPIO.cleanup()
    
