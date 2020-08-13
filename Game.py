"""
Name: Jessy Ashcraft
Date: 10/30/2019
Program: Game.py
"""
from Name_History import *
from Myutilities import *
from TaregtRoller import *
from Charecter_stat_generator import *
from BoardGenerator import *
from Gen_Treasure import *
from os import *
from random import *
import pickle
from codecs import open
import sys
import math


def Combat(player, enemy):
    while True:
        PlayerAttackRoll = dieRoller(1,20)
        EnemyAttackRoll = dieRoller(1,20)
        PlayerAttackBonus = (player['Attack']) //5
        EnemyAttackBonus = (enemy['Attack']) //5
        PlayerDefenseBonus = (player['Defense']) //5
        EnemyDefenseBonus = (enemy['Defense']) //5 
        
        
        while True:
            print("Enemy Health: " + str(enemy['Health']))
            print("Player Health: " + str(player['Health']))
            attacks = input("You have only learned four attack styles which do you choose You have a (hidden) attack. \n(P)ower Attack, (Q)uick Attack, (C)ounter, (N)ormal Attack: ").upper()
            if attacks == "P":
                PlayerAttackBonus *= 2
                EnemyAttackBonus *= 1.5
                break
                
            elif attacks == "Q":
                PlayerAttackBonus *= 2
                EnemyAttackBonus *= 1.5
                break
                
            elif attacks == "C":
                PlayerDefenseBonus *= 2.5
                PlayerAttackBonus = 0
                break
                
            elif attacks == "N":
                PlayerAttackBonus
                break
            
            elif attacks == "E":
                enemy["Health"] = 0
                
            else:
                print("oops sorry dumbass.")
            
        
        PlayerDamage = PlayerAttackRoll + PlayerAttackBonus - EnemyDefenseBonus - 10
        EnemyDamage = EnemyAttackRoll + EnemyAttackBonus - PlayerDefenseBonus - 10


        if player["Health"] <= 0:
            print("You Have Died!")
            input()
            sys.exit(0)
        
        elif enemy["Health"] <= 0:
            print("You've Slain an Enemy!")
            player["EnemiesKilled"] += 1
            print(str(player["EnemiesKilled"]))
            input()
            break
        
        if PlayerDamage <= 0:
            print("Your Skill With the Blade Needs Improveing")
            input()
            ClearScreen()
        else:
            enemy["Health"] -= PlayerDamage

        if EnemyDamage <= 0:
            print("The Enemies Training is Lacking! Strike while you can.")
            input()
            ClearScreen()
        else:
            player["Health"] -= EnemyDamage

def NewGame():
        player = PlayerPicker()
        row = input("Enter a number of rows: ")
        while row.isdigit() == False:
            print("Invalid Number. Try Again")
            row = input("Enter a number of rows: ")
        row = int(row)
        col = input("Enter a number of columns: ")
        while col.isdigit() == False:
            print("Invalid Number. Try Again")
            col = input("Enter a number of col: ")
        col = int(col)
        board = CreateBoard(row, col)
        board, player = PlacePlayer(board, player)
        treasure = GenTreasure(board)
        print("Attack: "+str(player['Attack']))
        print("Defense: "+str(player['Defense']))
        print("Health: "+str(player['Health']))
        treasure, board = GenTreasure(board)
        return player, board, treasure


def LoadGame():
    game = pickle.load(open("save.p", "rb"))
    return game['player'], game['board'], game['treasure']

def Main():
    while True:
        print("""\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


                    """)
        mainMenu = input("Hello And Welcome to THE GAME! press (H)elp or Enter to continue: ").upper()
        if mainMenu == "H":
            print("Hello You are Viewing the Help Menu Here this explains how you do things within the game. \nIn This Game You Control a player. \nYou move this player around using WASD. \nYou Acsess you inventory using I. \nYou can save your current progress by pressing Q. \nYou will be battling randomly generated enemies for combat. \nYour current Goal is to get 5 kills to win the game. \nIf you are done Reading this menu press enter.")
            input()
        ClearScreen()
    
        
        gameChoice = input("(N)ew Game or (L)oad Game: ").upper()
        if gameChoice == "N":
            player, board, treasure = NewGame()
            break
        elif gameChoice == "L":
            player, board, treasure = LoadGame()
            break
        else:
            print("Invalid input")
        
    while (True):
        ShowBoard(board)
        print("Attack: "+str(player['Attack']))
        print("Defense: "+str(player['Defense']))
        print("Health: "+str(player['Health']))
        print("Currentrow: "+str(player['row']))
        print("Currentcol: "+str(player['col']))
        if player["EnemiesKilled"] == 5:
            print("Congraulations You Have Beat the Game!!!!")
            sys.exit(0)

        CommandPlayer(player, board, treasure)
        die = dieRoller(1,6)
        if die == 6:
            MinorTreasure(player)
        
        elif die == 1:
            enemy = GenPlayer(len(player['Treasure']))
            ClearScreen()
            print("You Have Encountered an enemy!!")
            print("---------------------------------")
            print("The enemy is Near!!")
            print("Name: " + str(enemy["Name"]))
            print("Attack: "+str(enemy['Attack']))
            print("Defense: "+str(enemy['Defense']))
            input()
            Combat(player, enemy)
            
        ClearScreen()
        if CheckTreasure(player,treasure): 
            player["Treasure"].append(treasure["name"])
            treasure, board = GenTreasure(board)
       

         
Main()



#enemy = GenPlayer(len(player['Treasure']))
#Call the GenPlayer function to create an enemy, passing in the length of your treasures found list as the level


#elif die == 1:
#ClearScreen()
#print("You Have Encountered an enemy!!")
#print("The enemy is Near!!")
#print(enemy)