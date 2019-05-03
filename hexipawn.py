#!/usr/bin/env python3

import random
from modules.piece import Piece
from modules.computer import Computer
from modules.game_state import Game_State
from modules.memory import memory
from modules.moves import check_possible_moves


working_memory = []

def main():
  game = init_game()
  while True:
    # player moves
    game = get_player_piece(game)
    game.print_board()
    print("\n" + ("#" * 15) + "\n")
    
    # check if move ended game
    over = game_not_over(game.board, "P", "C")
    if not over['bool']:
      print(f"The Winner is {over['winner']}")
      break

    #computer moves
    game.computer.move(game)
    game.print_board()
    # check if moev ended game
    over = game_not_over(game.board, "P", "C")
    if not over['bool']:
      print(f"The Winner is {over['winner']}")
      break

  save_memory(memory, working_memory, over)
  return check_replay()

# game state stores board data,
# has creation metods to print its state, move a piece, and build a new game;




# the random brain for initial play with no librabry to reference.



def player_crossed_board(board):
  if board[0] != None and board[0].symbol == "P":
    return True
  elif board[1] != None and board[1].symbol == "P":
    return True
  elif board[2] != None and  board[2].symbol == "P":
    return True
  return False

def computer_crossed_board(board):
  if board[6] != None and board[6].symbol == "C":
    return True
  elif board[7] != None and board[7].symbol == "C":
    return True
  elif board[8] != None and  board[8].symbol == "C":
    return True
  return False
# uses check possible moves to determine if the player who is up can play 
# OR if the last player just won
def game_not_over(board, up, notup):
  if player_crossed_board(board):
    return {
      'bool': False,
      'winner': "P"
    }

  if computer_crossed_board(board):
    return {
      'bool': False,
      'winner': "C"
    }

  if len(check_possible_moves(board, up, notup)) == 0:
    return {
      'bool': False,
      'winner': notup
    }

  if len(check_possible_moves(board, notup, up)) == 0:
    return {
      'bool': False,
      'winner': up
    }

  return {
    'bool': True,
    'winner': None
  }

# safe function for the library (write to file)
def save(lib):
  file = open('library.py', 'w+')
  file.write(f"library = {memory}")
  file.close()

# update working library (ie current memory)
def update_library():
  pass

def init_game():
  game = Game_State.new()
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
  
  if (input("Type Y to play or N to quit: ") == "N"):
    return

  game.print_board()
  return game

def get_player_piece(state):
  while True:
    print("Your move: please select a piece (row/col)")
    select = sanitized_input()
    if valid_select(select, state.board, "P"):
      break
    else:
      print("You do not have a piece at that location.")
  return get_player_move(select, state)

def get_player_move(at, state):
  moves = check_possible_moves(state.board, "P", "C")
  while True:
    print("Your move: please select a move (row/col)")
    move = sanitized_input()
    if [at, move] in moves:
      p = state.board[at]
      return Game_State.move(state, p, move)
    else:
      print("That is not a valid move.")
  
def sanitized_input():
    select = int(input(">>> ")) - 1
    if select > 8 or select < 0:
      print("Please select a valid location (row/col)")
      return sanitized_input()
    return select

def valid_select(selected, pieces, you):
  if pieces[selected].symbol == you:
      return True
  return False


def check_replay():
  if input("Would you like to play again?") == "Y":
    return main()
  
  else:
    print("thanks for playing!")
    return

def save_memory(ltm, stm, state):
  for move in stm:
    if f"{move[0]}" in ltm:
      contains = False
      for mmove in ltm[f"{move[0]}"]:
        if mmove["move"] == move[1]:
          if state['winner'] == "C":
            mmove["score"] += 1
          elif state['winner'] == "P":
            pass
          else:
            mmove["score"] += .5
          contains = True  
      if contains == False:    
        ltm[f"{move[0]}"].append({"move":move[1], "score": 0})

  file = open('memory.py', 'w+')
  file.write(f"memory = {memory}")
  file.close()

if __name__ == "__main__":
  main()