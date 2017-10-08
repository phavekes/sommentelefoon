#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import os
import time
import random
import pygame
import urllib2
import requests

#vars hierzo
SCHIJFPIN = 25
AARDPIN = 23
HOORNPIN = 24

#stel de pinnetjes goed in 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SCHIJFPIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(HOORNPIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(AARDPIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
  aardContact = GPIO.input(AARDPIN)
  print aardContact
  time.sleep(1)
  
