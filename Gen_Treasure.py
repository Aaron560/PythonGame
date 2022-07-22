"""
Name: Aaron Ashcraft
Date: 11/17/2019
Programe: Gen_Treasure
"""
from Myutilities import *

"""generates a pice of treasure onto the board"""
def GenTreasure(board):
    import random
    treasure = {}
    TreasureNames = "Small Recording Device, Forbidden Scroll, Card Games, Modification Chip, Elucidator, Power Ranger Helment".split(",")
    TreasureRow = random.randint(0,len(board)-1)
    TreasureCol = random.randint(0,len(board[0])-1)
    treasure["row"] = TreasureRow
    treasure["col"] = TreasureCol
    treasure["name"] = TreasureNames[random.randint(0,len(TreasureNames)-1)]
    return treasure,board

"""Checks Aginst the players postion with the treasures and returns true if they match"""
def CheckTreasure(player, treasure):
    if player["row"] == treasure["row"] and player["col"] == treasure["col"]:
        return True
    else:
        return False

"""Generates Minor treasure that grants a minor stat increase"""
def MinorTreasure(player):
    minorTreasure = "Gems,Mushrooms,Coins,Shells,gauntlets,tokens,necklaces,old Glasses,map,bullets,horseshoes,gold teeth".split(",")
    randomNumber = random.randint(1,4) #chooses which stat will increase
    if randomNumber == 1:
        die = dieRoller(1,4)
        player["Attack"] += die
        print("You found "+minorTreasure[random.randint(0, len(minorTreasure)-1)]+". Your attack went up by "+str(die)+".")
        input() # Holds the screen till a key is pressed.
    elif randomNumber == 2:
        die = dieRoller(1,4)
        player["Defense"] += die
        print("You found "+minorTreasure[random.randint(0, len(minorTreasure)-1)]+". Your defense went up by "+str(die)+".")
        input()
    elif randomNumber == 3:
        die = dieRoller(2,4)
        player["Health"] += die
        print("You found "+minorTreasure[random.randint(0, len(minorTreasure)-1)]+". Your health went up by "+str(die)+".")
        input()
   
    """
    To trigger a Minor Treasure, roll a random 1d6 every time the player moves. If it is a 6, then give them a minor treasure. (Later, a roll of 1 will trigger combat)
    When creating an enemy for combat, we will be passing the length of the treasuresFound list in for the level variable. This will make your enemies harder as you find treasures. The player should be given the option to view found treasures. At the end of game, output all treasures found.
   
    """
