"""
Name: Jessy Ashcraft
Date: 10/23/2019
Programm: Player stats
"""
from random import *
from Name_History import *
from Myutilities import *
from TaregtRoller import *

def GenPlayer(level):
    player = {}
    player["Name"] = GenName()
    player["History"] = GenHistory()
    player["Attack"] = dieRoller(3,6) + level + dieRoller(1,4)
    player["Defense"] = dieRoller(3,6) + level + dieRoller(1,4)
    player["Health"] = dieRoller(5,6) + level + dieRoller(1,4)
    player["row"] = 0
    player["col"] = 0
    player["Treasure"] = []
    player["EnemiesKilled"] = 0
    return player
    

def PlayerPicker():
    while True:
        player = GenPlayer(5)
        print("Name: "+player['Name'])
        print("History: "+player['History'])
        print("Attack: "+str(player['Attack']))
        print("Defense: "+str(player['Defense']))
        print("Health: "+str(player['Health']))
        print("row: "+str(player['row']))
        print("col: "+str(player['col']))
        userInput = input("Do you Want to keep This Character (Y)es or (N)o: ").upper()
        if userInput == "Y":
            break
        if userInput == "N":
            ClearScreen()
            continue
    return player
      