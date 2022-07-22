"""
Name: Aaron Ashcraft
Date: 10/9/2019
Program: target roller asignment
"""
import random

def TargetRoller(times, sides, targets):
    targetotal = 0
    for i in range(times):
        roll = random.randint(1,sides)
        if roll >= targets:
            targetotal += 1
    return targetotal
