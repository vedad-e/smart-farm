from time import sleep
import RPi.GPIO as GPIO
import os
#from random import randint
import random

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

# Koračni motor 28BYJ-48 konstruiran je na način da motor u
# Unutarnjih 8 koraka potrebno za jedan okret. 
# ali treba 512 x 8 koraka da bi se osa zarotirala jednom
# okreće se za 360°.

# Definicija koraka 1 - 8 preko pinova IN1 do IN4 Postoji kratka pauza između svakog kretanja motora tako da
#armatura motora dosegne svoj položaj.
def Step1():
    GPIO.output(IN4, True)
    sleep (time)
    GPIO.output(IN4, False)

def Step2():
    GPIO.output(IN4, True)
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN4, False)
    GPIO.output(IN3, False)

def Step3():
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN3, False)

def Step4():
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)

def Step5():
    GPIO.output(IN2, True)
    sleep (time)
    GPIO.output(IN2, False)

def Step6():
    GPIO.output(IN1, True)
    GPIO.output(IN2, True)
    sleep (time)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)

def Step7():
    GPIO.output(IN1, True)
    sleep (time)
    GPIO.output(IN1, False)

def Step8():
    GPIO.output(IN4, True)
    GPIO.output(IN1, True)
    sleep (time)
    GPIO.output(IN4, False)
    GPIO.output(IN1, False)

# Okrenite u smjeru suprotnom od kazaljke na satu
#FJA left
def left(step):
    for i in range (step):   
            #os.system('clear') # previše usporava kretanje motora.
            Step1()
            Step2()
            Step3()
            Step4()
            Step5()
            Step6()
            Step7()
            Step8()  
            print ("Steps left: " + str(i))

# Okrenite u smjeru kazaljke na satu
def right(step):
        for i in range (step):
            #os.system('clear') # previše usporava kretanje motora. 
            Step8()
            Step7()
            Step6()
            Step5()
            Step4()
            Step3()
            Step2()
            Step1()  
            print ("Steps right: " + str(i))
        
# Ovdje se odlučuje hoće li se ići lijevo ili desno
#if random.randint(0, 2) >= 1:
    # Ovdje se određuje koliko daleko se motor okreće.
    #left(random.randint(100, 1024))
#else:
    #right(random.randint(100, 1024))
#right(1990)
#GPIO.cleanup()
