"""
Name: Jessy Ashcraft
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

#while(True):
    #input(GenName())

#backGround = ["Raised By Wolves", "Killed By Clowns and Ressurected", "But A Math Scholar Homed you."]

#def Main():
    #userInput = input("Press (C)ontinue or (Q)uit: ")
    #if userInput == "C":
       #print(GenName + backGround)
    #else:
        #pass


    #return Main()


#def GenHistory():#generates random history
    #import random
    #inputs for background, job, and funfact.  Use in replace().
    #place = input("Enter a place: ")
    #thing = input("Enter a thing: ")
    #adj = input("Enter an adjective: ")
    #verb = input("Enter a verb: ")
    #creature = input("Enter a type of creature or animal: ")
    #celebrity = input("Enter a celebrity: ")

    #Background = [("I grew up in place where I learned how to play the carrot recorder. I also get super strength from eating Big Mac's.\n").replace("place", place),
    #("If place is the 'city that never sleeps', then Los Angeles is the 'city that’s always passed out on the couch'.").replace("place", place)
    #("I grew up trying to learn how to be pretty, but never got the hang of it, so now I pretend to be celebrity.\n").replace("celebrity", celebrity)]
    #Job = [("I work as a type-writter during the day and an adj clown who juggles people's garlic bread at night.\n").replace("adj", adj),
    #("I own a store in Boone County, but only sell things, and in my down time I watch Adam Sandler eat ramen noodles.\n").replace("things", thing),
    #("I play the bagpipes on the streets and allow people to verb items at me.\n").replace("verb", verb)]
    #FunFact = [("I have a thing that makes people immortal, but turns them into an octopus.").replace("thing", thing),
    #("I can use a thing to protect myself from mutated rats.").replace("thing", thing), 
    #("I have a coach named celebrity who teaches me how to become a professional paintball player.").replace("celebrity", celebrity) , 
    #("I went threw celebrity course intro to being a stunning michale jackson.").replace("celebrity", celebrity) ,
    #("George and Harold were usually responsible kids. Whenever anything bad happened, George and Harold were usually responsible.").replace("celebrity", celebrity),
    #("I can morph into a creature only when I sneeze a total of 6 times.").replace("creature", creature) ,
    #("The Scaryiest thing iv ever seen would have to be creature the thing i never wanted in my closet.").replace("creature", creature) ,] 
    #history = Background[random.randint(0, len(Background)-1)] + Job[random.randint(0, len(Job)-1)] + FunFact[random.randint(0, len(FunFact)-1)]
    #return history