import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)


UP = 6
DOWN = 5
MID = 13
LEFT = 26
RIGHT = 16


GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(UP, GPIO.IN)
GPIO.setup(DOWN, GPIO.IN)
GPIO.setup(MID, GPIO.IN)
GPIO.setup(LEFT, GPIO.IN)
GPIO.setup(RIGHT, GPIO.IN)



while True:
    if(not(GPIO.input(UP))):
       print("UP")
       time.sleep(0.4)
    
    if(not(GPIO.input(DOWN))):
       print("DOWN")
       time.sleep(0.4)
       
    if(not(GPIO.input(MID))):
       print("MID")
       time.sleep(0.4)
       
    if(not(GPIO.input(RIGHT))):
       print("RIGHT")
       time.sleep(0.4)
    
    if(not(GPIO.input(LEFT))):
       print("LEFT")
       time.sleep(0.4)