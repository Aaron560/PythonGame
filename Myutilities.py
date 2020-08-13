"""
Name:Jessy Ashcraft
Date:9/18/2019
Program:die roller
"""
import random
import os

def dieRoller(times, sides):
    total = 0 # accumulator value
    for i in range(times): # the range for times
        roll = random.randint(1, sides)
        total += roll
    return total

def ClearScreen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
#while (True):
    #t = int(input("enter the amount of times to roll.: "))
    #s = int(input("enter the amount of sides.: "))
    #print(DieRoller(t,s))
