#!/usr/bin/env python3
import re
import os
from modules.game_state import Game_State
from modules.memory import memory
from modules.moves import check_possible_moves

def main(skipInit=False):
  game = init_game(skipInit)
  if game == None: return
  game.print_board()
  
  while True:
    # player moves
    game.player.move(game)
    game.print_board()
    print("\n" + ("#" * 15) + "\n")

    if game.over():
      print(f"The Winner is {game.winner}")
      break

    #computer moves
    game.computer.move(game)
    game.print_board()

    if game.over():
      print(f"The Winner is {game.winner}")
      break

  game.save_memory([])
  return check_replay()

def init_game(skip):
  if skip: return Game_State()

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
    return Game_State()
  else:
    return print("Sorry to see you go.")

def check_replay():
  if re.match("^(y|yes)$", input("Would you like to play again?"), flags=re.IGNORECASE):
    return main(True)
  else:
    return print("thanks for playing!")

if __name__ == "__main__":
  main()