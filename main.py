from stepperTwo import leftTwo
from stepperTwo import rightTwo
from TwochannelRelay import pump_on
from TwochannelRelay import pump_off
from stepperOne import left
from stepperOne import right
from Ultrasonic import distance
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
#GPIO.cleanu
GPIO.setmode(GPIO.BCM)

# Korišteni pinovi ULN2003A za pinove Raspberry Pi
# dodijeljeno 
IN1=6 # IN1
IN2=13 # IN2
IN3=19 # IN3
IN4=26 # IN4

# Vrijeme čekanja kontrolira brzinu rada motora
# rotira.
time = 0.001

# Definiramo pinove izlaza
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)
# Svi su pinovi inicijalno postavljeni na False. Tako da se ne okreće
# Koračni motor odmah.
GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

IN1=17 # IN1
IN2=27 # IN2
IN3=22 # IN3
IN4=25 # IN4

# Vrijeme čekanja kontrolira brzinu rada motora
# rotira.
time = 0.001

# Definiramo pinove izlaza
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)
# Svi su pinovi inicijalno postavljeni na False. Tako da se ne okreće
# Koračni motor odmah.
GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

while True:
    pump_off()
    right(2000)
    dist=distance()
    sleep(3)
    if dist > 3 :
        pump_on()
        sleep(3)
        pump_off()
    else:
        pump_off()
    leftTwo(1000)
    dist=distance()
    sleep(3)
    if dist > 3 :
        pump_on()
        sleep(3)
        pump_off()
    else:
        pump_off()
    left(2000)
    dist=distance()
    sleep(3)
    if dist > 3 :
        pump_on()
        sleep(3)
        pump_off()
    else:
        pump_off()
    rightTwo(1000)
    dist=distance()
    sleep(3)
    if dist > 3 :
        pump_on()
        sleep(3)
        pump_off()
    else:
        pump_off()
    sleep(15)

