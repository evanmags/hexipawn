#!/usr/bin/env python3

import re
import os
import sqlite3
from modules.game_state import GameState

def main(skipInit=False):
  game = init_game(skipInit)
  if game == None: return
  game.print_board()
  
  connection = sqlite3.connect('hexipawn_memory.db')

  while not game.over("C"):
    # player moves
    game.player.move(game)
    game.print_board()
    print(("#" * 45) + "\n")

    if game.over("P"): break
    
    #computer moves
    game.computer.move(game, connection)
    game.print_board()
    print(("#" * 45) + "\n")

  print(f"The Winner is {game.winner}")

  game.save_memory(connection)

  if check_replay(): return main(True)

def init_game(skip):
  if skip: return GameState()

  os.system('clear')

  print("\nWELCOME TO HEXIPAWN\n")
  print("Below you will see a board, when selecting pieces and moves\nuse the numbers in each square to select them.\n")
  print(f"\t\t 1 | 2 | 3 ")
  print(f"\t\t-----------")
  print(f"\t\t 4 | 5 | 6 ")
  print(f"\t\t-----------")
  print(f"\t\t 7 | 8 | 9 \n")

  print("RULES:\t1. You can only move one space at a time.")
  print("\t2. You can only move diagonal to capture a piece.")
  print("\t3. To win you can either reach the opposite side.")
  print("\t   of the board, capture all of your players pieces,")
  print("\t   pieces, or cause your opponent to no longer have")    
  print("\t   any valid moves.\n")    


  print("ENJOY!!\n")

  if re.match("^(y|yes)$", input("Type Y to play or N to quit: "), flags=re.IGNORECASE):
    return GameState()
  else:
    return print("Sorry to see you go.")

def check_replay():
  if re.match("^(y|yes)$", input("Would you like to play again?"), flags=re.IGNORECASE):
    return True
  print("thanks for playing!")
  return False

if __name__ == "__main__":
  main()