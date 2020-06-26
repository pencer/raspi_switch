#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import os

g_count = 0

ADRSIR_SW01 =  4 # SW1
ADRSIR_SW02 = 17 # SW2
ADRSIR_SW03 = 27 # SW3
ADRSIR_SW04 = 18 # SW9
ADRSIR_SW05 =  5 # SW5
ADRSIR_SW06 =  6 # SW6
ADRSIR_SW07 = 13 # SW7
ADRSIR_SW08 = 12 # SW8
ADRSIR_SW09 = 22 # SW9
ADRSIR_SW10 = 23 # SW10

BTN_A = ADRSIR_SW05
BTN_B = ADRSIR_SW10
BTN_C = ADRSIR_SW09

GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN_A,GPIO.IN)
GPIO.setup(BTN_B,GPIO.IN)
GPIO.setup(BTN_C,GPIO.IN)

try:
    while True:
        if not GPIO.input(BTN_A):
            if g_count == 0:
                g_count = 1
                os.system("/home/pi/kanachu/BusInfo/tenki.py")
        if not GPIO.input(BTN_B):
            if g_count == 0:
                g_count = 1
                os.system("/home/pi/kanachu/BusInfo/kanachu.py 12117 12101")
        #if not GPIO.input(BTN_C):
        #    if g_count == 0:
        #        g_count = 5
        #        print("0push button {}".format(BTN_C))
        #print(g_count)
        time.sleep(0.10)
        if g_count > 0:
            g_count -= 1
except KeyboardInterrupt:
    GPIO.cleanup()

