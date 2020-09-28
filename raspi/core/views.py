from django.shortcuts import render, HttpResponse

#RASPI IMPORTS
import RPi.GPIO as GPIO
import time

#SETTING UP RASPI GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT) 

#RASPI Functions

def raspi_led():
    for i in range(10):
        GPIO.output(17, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(17, GPIO.LOW)
        sleep(0.2)


def home(request):
    raspi_led()
    return HttpResponse("Connected to Raspberry Pi!")
