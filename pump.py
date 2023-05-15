import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

def pump_on():
    GPIO.output(23, GPIO.LOW) 
    time.sleep(2) #10sec ukljuceno
    print("Pumpa ukljucena")

def pump_off():
    GPIO.output(23, GPIO.HIGH)
    time.sleep(2)
    print("Pumpa iskljucena")
    
#while True:  
  #  pump_on()
    #print("Pumpa ukljucena")
   # time.sleep(2)
    #pump_off()
    #print("Pumpa iskljucena")
    #time.sleep(2)

#GPIO.cleanup()

