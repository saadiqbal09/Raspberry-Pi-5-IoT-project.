import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Relay_1 = 2
Relay_2 = 3

GPIO.setup(Relay_1, GPIO.OUT)
GPIO.output(Relay_1, GPIO.LOW)

GPIO.setup(Relay_2, GPIO.OUT)
GPIO.output(Relay_2, GPIO.LOW)

while(True):
    GPIO.output(Relay_1, GPIO.HIGH)
    GPIO.output(Relay_2, GPIO.LOW)
    time.sleep(2)
    GPIO.output(Relay_1, GPIO.LOW)
    GPIO.output(Relay_2, GPIO.HIGH)
    time.sleep(2)

