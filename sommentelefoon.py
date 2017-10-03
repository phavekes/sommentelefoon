#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import os
import time
import random
import pygame
import urllib2
import requests

# Test of we verbinding hebben
def internet_on():
    try:
        urllib2.urlopen('http://google.com/', timeout=1)
        return 1
    except urllib2.URLError as err: 
        return -1

#log naar het scherm, en eventueel naar het internet
def log(tekst):
    print tekst
    #Als we een internet verbinding hebben loggen we ook naar de server
    if INTERNET > 1:
        url = 'https://azijn.havekes.eu/telefoon/'
        payload = {'name': MIJNID, 'value': tekst}
        # POST with form-encoded data
        r = requests.post(url, data=payload)

#speel een MP3
def speel(bestand):
    pygame.mixer.music.load(bestand)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

#speel de gekozen som af
def speelSom(getal1, getal2):
    log("Wat is", getal1, "x", getal2,"?")
    speel("./sound/som " + str(getal1) + " keer "+str(getal2)+".mp3")

#haal het nummer op van de draaischijf
def getNummer():
    nPulsen = 0
    # Wacht op draaischijf / knop
    schijfContact = GPIO.input(SCHIJFPIN)
    aardContact = GPIO.input(AARDPIN) # Laag als ingedrukt!!!
    while schijfContact == False and aardContact == True:
        schijfContact = GPIO.input(SCHIJFPIN)
        aardContact = GPIO.input(AARDPIN)

    # Aardtoets ingedrukt
    if aardContact == False:
        return -1

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


def hoornCallback(channel):
    log("Hoorn!"+str(channel))
    # herstart het hele script
    GPIO.cleanup()
    python = sys.executable
    os.execl(python, python, * sys.argv)


#vars hierzo
SCHIJFPIN = 25
AARDPIN = 23
HOORNPIN = 24

#een nummertje, voor als er ooit meerdere telefoons zijn
MIJNID=1

#hou bij of we internetverbinding hebben
INTERNET=-1

#stel de pinnetjes goed in 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SCHIJFPIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(HOORNPIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(AARDPIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Gebruik een interrupt voor de hoorn,
# omdat deze op elk moment kan worden neergelegd
#GPIO.add_event_detect(HOORNPIN, GPIO.BOTH, callback = hoornCallback)

pygame.mixer.init()

while True:
    #test of we (nog) internetverbinding hebben
    INTERNET=internet_on();
    log(opgestart)
    try:
        # Wacht op hoorn
        log("Wacht op hoorn...")
        hoornContact = GPIO.input(HOORNPIN)
        while hoornContact == True:
            hoornContact = GPIO.input(HOORNPIN)
            print hoornContact
            time.sleep (1)

        # Welk tafeltje oefenen?
        log("Speelt welkomsttekst")
        speel("sound/kiestoon.wav")
        speel("sound/welkom.mp3")
        speel("sound/welketafel.mp3")
        tafeltje = getNummer()

        #Welke tafel is gekozen
        if tafeltje > -1:
            log("Gekozen voor tafel van "+str(tafeltje))
            speel("sound/gekozentafel.mp3")
            speel("sound/"+str(tafeltje)+".mp3")

        # Lijst om bij te houden welke sommen goed/fout beantwoord zijn
        sommen = []
        for som in range(10):
            sommen.append(0) # 0 is fout, 1 is goed
        aantalGoed = 0

        while aantalGoed < 10:
            # Bepaal opgave
            getal1 = random.randint(1,10)
            while sommen[getal1 - 1] == 1:
                getal1 = random.randint(1,10)

            if tafeltje == -1:
                getal2 = random.randint(1,10)
            elif tafeltje == 0:
                getal2 = 10
            else:
                getal2 = tafeltje
            log("Opgave is " + str(getal1) + " X " + str(getal2))
            uitkomst = getal1 * getal2
            nCijfers = len(str(uitkomst))

            speelSom(getal1, getal2)
            huidigCijfer = 0
            antwoord = ""

            # Wacht op antwoord
            while huidigCijfer < nCijfers:
                nummer = getNummer()
                if nummer > -1: # aan schijf gedraaid
                    antwoord = antwoord + str(nummer)
                    huidigCijfer = huidigCijfer + 1
                else: # aardtoets ingedrukt
                    speelSom(getal1, getal2)
                    huidigCijfer = 0
                    antwoord = ""
            print antwoord

            # Controleer antwoord
            reactie = random.randint(1,4)
            if int(antwoord) == uitkomst:
                aantalGoed = aantalGoed + 1
                sommen[getal1 - 1] = 1
                log("Goed")
                speel("sound/goed"+str(reactie)+".mp3")
            else:
                log("Jammer, de juiste uitkomst is ", uitkomst)
                speel("sound/fout"+str(reactie)+".mp3")
                speel("./sound/antwoord " + str(getal1) + " keer "+str(getal2)+".mp3")
            print
            time.sleep(1)
        log("10 antwoorden goed, afgelopen")
        speel("sound/einde.mp3")
        speel("sound/kiestoon.wav")
    except KeyboardInterrupt: # Ctrl+C
        GPIO.cleanup()