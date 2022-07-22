"""
Name: Aaron Ashcraft
Date: 10/9/2019
Program: Name and Assignment
"""

def GenName():
    import random
    firstSyl = "Jun, Mugi, *#()@*)Q#*, NASA, Shuichi, Megan, Welcom To Chillies, Thanos, Minecraft".split(",")
    secondSyl = "eral, landon, joseph, edward, Poasy, Steve".split(",")
    title = "the Ultimate Dectective, the Ultimate Astrounaut, the Ultimate Magician, the Ultimate Ocultist, the Ultimate Princesses, the Empress, the Emperor, the Chariot, the Hermit, the Hanged Man, of Strength, the Wheel of Fortune, of Jusice, of Death, of Temperance, the Devil, the Tower, the Moon, the Judgement, the World".split(",")
    name = firstSyl[random.randint(0, len(firstSyl)-1)] + secondSyl[random.randint(0, len(secondSyl)-1)] + title[random.randint(0, len(title)-1)]
    return name


def GenHistory():#generates random history
    import random

    Background = [
    ("If NewYork is the 'city that never sleeps', then Los Angeles is the 'city that’s always passed out on the couch'.")]

    Job = [("I work as a type-writter during the day and a Goofy clown who juggles people's garlic bread at night.")]
   
    FunFact = [("The Scaryiest thing iv ever seen would have to be the Dragons in my Wii-U.")]
    
    history = str(Background) + str(Job) + str(FunFact)
    
    return history
