#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import os
import time
import random
import pygame
#import urllib2
#import requests

#vars hierzo
SCHIJFPIN = 25
AARDPIN = 23
HOORNPIN = 24


GPIO.setmode(GPIO.BCM)
GPIO.setup(SCHIJFPIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(HOORNPIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(AARDPIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#haal het nummer op van de draaischijf
def getNummer():
    nPulsen = 0
    # Wacht op draaischijf / knop
    schijfContact = GPIO.input(SCHIJFPIN)
    while schijfContact == False:
        schijfContact = GPIO.input(SCHIJFPIN)

    # Afhandelen van pulsen
    klaar = False
    while klaar == False and schijfContact == True:
        nPulsen = nPulsen + 1
        startTijd = time.time()
        time.sleep(0.1)
        schijfContact = GPIO.input(SCHIJFPIN)

        # Controleer tijd tussen twee pulsen
        while klaar == False and schijfContact == False:
            if time.time() - startTijd >= 0.2:
                klaar = True
            schijfContact = GPIO.input(SCHIJFPIN)
    return nPulsen % 10

while True:
  print getNummer()
  

