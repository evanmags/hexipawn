#!/usr/bin/env python3

from modules.game_state import Game_State
from modules.memory import memory
from modules.moves import check_possible_moves

def main():
  game = init_game()
  if game == None:
    return
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

def init_game():
  
  print("\nWELCOME TO HEXIPAWN\n")
  print("Below you will see a board, when selecting pieces and moves\nuse the numbers in each square to select them.")
  print(f" 1 | 2 | 3 ")
  print(f"-----------")
  print(f" 4 | 5 | 6 ")
  print(f"-----------")
  print(f" 7 | 8 | 9 \n")

  print("RULES:\t1. You can only move one space at a time.")
  print("\t2. You can only move diagonal to capture a piece.")
  print("\t3. To win you can either reach the opposite side.")
  print("\t   of the board, capture all of your players pieces,")
  print("\t   pieces, or cause your opponent to no longer have")    
  print("\t   any valid moves.\n")    


  print("ENJOY!!\n")
  
  if (input("Type Y to play or N to quit: ").upper() == "N"):
    return print("sorry to see you go.")
  else:
    return Game_State.new()

def check_replay():
  if input("Would you like to play again?") == "Y":
    return main()
  
  else:
    print("thanks for playing!")
    return

if __name__ == "__main__":
  main()