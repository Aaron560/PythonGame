"""
Name: Aaron Ashcraft
Date: 10/30/2019
Program: BoardGenerator
"""

import random
import sys
import pickle
# makes a function to generate a game board based on player inputs.
def CreateBoard(row, col):
    
    board = []
  
    for i in range(row):
        board.append([])
        for j in range(col):
            board[i].append(".")
      
    return board
# Shows the board after its created.
def ShowBoard(board):
    for row in board:
        seperate =  " "
        print(seperate.join(row))
# places players charecter on the created board at random areas of the board.
def PlacePlayer(board, player):
    import random
    playerrow = random.randint(0,len(board[0])-1) #col = len of board starting with sub 0
    playercol = random.randint(0,len(board)-1) #row = length of board 
    player["row"] = playerrow #assigns row number to dictionary
    player["col"] = playercol #assigns column number to dictionary
    board[playerrow][playercol] = "@" #makes player an @ sign
    return board, player


# allows commanding of player and other menus.
def CommandPlayer(player, board, treasure):
    oldPlayer = "."
    newPlayer = "@"

    while(True):
        ValidInputs = ["W", "S", "A", "D"]
        Playermove = input("What direction do you want to go? (W)up, (S)down, (A)left, (D)right or (I)for inventory or (Q)to save the Game. ").upper()

        if Playermove in ValidInputs:
            break
        elif Playermove == "I":
            print("Treasures obtained")
            print(player["Treasure"])
            print("----------------")
            print("Enemies Killed")
            print(player["EnemiesKilled"])
            print("----------------")
            input()
        if Playermove == "Q":
            SaveGame(player, board, treasure)
            input("Game Saved, Thanks For Playing!!")
            sys.exit(0)

    board[player["row"]][player["col"]] = "."
        
    if Playermove == "W":
        if player["row"] == 0:
            player["row"] = len(board) - 1
        else:
            player["row"] -= 1
    elif Playermove == "S":
        if player["row"] == len(board) - 1:
            player["row"] = 0
        else:
            player["row"] += 1
    elif Playermove == "A":
        if player["col"] == 0:
            player["col"] = len(board[0]) - 1
        else:
            player["col"] -= 1
    elif Playermove == "D":
        if player["col"] == len(board[0]) - 1:
            player["col"] = 0
        else:
            player["col"] += 1
   
    
        
    board[player["row"]][player["col"]] = "@"
    return player, board

# Saves the game
def SaveGame(player, board, treasure):
    game = {'player': player,
            'board': board,
            'treasure': treasure}
    pickle.dump(game, open("save.p","wb"))
