#!/usr/bin/python3
"""
Name: Cheslyn Williams
Student Number: WLLCHE013
Prac: 1
Date: 28 July 2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO

#variables
binary = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
decimal = 0

#Show Binary Number on LEDs
def display(value):
    GPIO.output(17, binary[value][0])
    GPIO.output(27, binary[value][1])
    GPIO.output(22, binary[value][2])
    
#Increase Binary Counter
def increase(channel):
    global decimal
    decimal += 1 
    if decimal == 8:
        decimal = 0
    display(decimal)
    
#Decrease Binary Counter
def decrease(channel):
    global decimal
    decimal -= 1
    if decimal == -1:
        decimal = 7
    display(decimal)
    
# Logic that you write
def main():
    #Setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
        
    #Push Button Press
    GPIO.add_event_detect(23, GPIO.RISING, callback=increase, bouncetime=200)
    GPIO.add_event_detect(24, GPIO.RISING, callback=decrease, bouncetime=200)
    
    #Keeps the program running while no input is given 
    x = input()
    
    #Remove Event Detection
    GPIO.remove_event_detect(23)
    GPIO.remove_event_detect(24)
    
# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
