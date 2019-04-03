import random
from memory import *

working_memory = []


# piece class, stores location and type data
class piece():
  def __init__(self, sym, location):
    self.sym = sym
    self.at = location


# game state stores board data,
# has creation metods to print its state, move a piece, and build a new game;
class game_state:
  def __init__(self, board, rnd):
    self.board = board
    self.rnd = rnd or 0

  @classmethod
  # generate a new game
  def new(self):
    pieces = ["C", "P"]
    board = [None] * 9
    i = 0;
    while i < 3:
      board[i] = piece("C", i)
      board[i + 6] = piece("P", i + 6)
      i += 1
    return game_state(board, 0);

  # print the game board
  def print_board(self):
    x = 1
    row_str = ''
    for piece in self.board:
      if piece != None:
        piece = piece.sym
      if x % 3 != 0:
        row_str += f" {piece or ' '} |"
      else:
        row_str += f" {piece  or ' '} "
        print(row_str)
        row_str = ''
        if(x < 7):
          print("-"*11)
      x += 1
  # move a piece in the board
  def move(self, p, to):
    working_memory.append([self.rnd, [p.at, to]])
    board = list(self.board)
    board[p.at] = None
    p.at = to
    board[to] = p
    rnd = self.rnd + 1
    return game_state(board, rnd)

def is_directly_ahead(board, position, you):
  if you == "C":
    if position + 3 < 9 and board[position + 3] == None:
      return True
  if you == "P":
    if position - 3 >= 0 and board[position - 3] == None:
      return True
  return False

def is_diagonal_left(board, position, you):
  if you == "C":
    if position + 2 < 9:
      if board[position + 2] != None and board[position + 2].sym == "P":
        if position != 0 and position != 3 and position != 6: # prevent jumping
          return True

  if you == "P":
    if position - 4 >= 0:
      if board[position - 4] != None and board[position - 4].sym == "C":
        if position != 6:  # prevent jumping
          return True
  return False

def is_diagonal_right(board, position, you):
  if you == "C":
    if position + 4 < 9:
      if board[position + 4] != None and board[position + 4].sym == "P":
        if position != 2: # prevent jumping
          return True

  if you == "P":
    if position - 2 >=0:
      if board[position - 2] != None and board[position - 2].sym == "C":
        if position != 2 and position != 5 and position != 8: # prevent jumping
          return True
  return False
# used for both ceckign possible moved for the computer 
# AND checking for game wins
# returns a list of possible moves for any player
def check_possible_moves(board, up, notup):
  index = 0
  moves = []
  for cell in board:
    if cell != None and cell.sym == up:
      position = cell.at
      if up == "C":
        # moving one square ahead
        if is_directly_ahead(board, position, up):
          moves.append([cell.at, position + 3])

        # moving diagonally
        if is_diagonal_left(board, position, up): # prevent jumping
            moves.append([cell.at, position + 2])

        if is_diagonal_right(board, position, up):  # prevent jumping
              moves.append([cell.at, position + 4])

      if up == "P":
        # moving one square ahead
        if is_directly_ahead(board, position, up):
          moves.append([cell.at, position - 3])
        # moving diagonally
        if is_diagonal_right(board, position, up):  # prevent jumping
            moves.append([cell.at, position - 2])

        if is_diagonal_left(board, position, up):  # prevent jumping
            moves.append([cell.at, position - 4])
  return(moves);

# the random brain for initial play with no librabry to reference.
def choose_move(moves):
  # getting passed [[row, col], #, #]
  piece = random.randint(0, len(moves) - 1)
  return moves[piece]


def player_crossed_board(board):
  if board[0] == "P" or board[1] == "P" or board[2] == "P":
    return True
  return False

def computer_crossed_board(board):
  if board[6] == "C" or board[7] == "C" or board[8] == "C":
    return True
  return False
# uses check possible moves to determine if the player who is up can play 
# OR if the last player just won
def game_not_over(board, up, notup):
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
  game = game_state.new()
  # print("\nWELCOME TO HEXIPAWN\n")
  # print("Below you will see a board, when selecting pieces and moves\nuse the numbers in each square to select them.")
  # print(f" 1 | 2 | 3 ")
  # print(f"-----------")
  # print(f" 4 | 5 | 6 ")
  # print(f"-----------")
  # print(f" 7 | 8 | 9 \n")

  # print("RULES:\t1. You can only move one space at a time.")
  # print("\t2. You can only move diagonal to capture a piece.")
  # print("\t3. To win you can either reach the opposite side.")
  # print("\t   of the board, capture all of your players pieces,")
  # print("\t   pieces, or cause your opponent to no longer have")    
  # print("\t   any valid moves.\n")    


  # print("ENJOY!!\n")
  
  # if (input("Type Y to play or N to quit: ") == "N"):
  #   return;

  game.print_board()
  return game

def get_player_piece(state):
  while True:
    print("Your move: please select a piece (row/col)")
    select = sanitized_input()
    if valid_select(select, state.board, "P"):
      break;
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
      return game_state.move(state, p, move)
      break
    else:
      print("That is not a valid move.")
  

def sanitized_input():
    select = int(input(">>> ")) - 1
    if select > 8 or select < 0:
      print("Please select a valid location (row/col)")
      return sanitized_input()
    return select

def valid_select(selected, pieces, you):
  if pieces[selected].sym == you:
      return True
  return False

def computer_move(game):
    comp_moves = check_possible_moves(game.board, "C", "P")
    ch = choose_move(comp_moves)
    piece = game.board[ch[0]]
    return game.move(piece, ch[1])

def check_replay():
  if input("Would you like to play again?") == "Y":
    return game()
  
  else:
    print("thanks for playing!")
    return

def save_memory(ltm, stm):
  for move in stm:
    if f"{move[0]}" in ltm:
      contains = False
      for mmove in ltm[f"{move[0]}"]:
        if mmove["move"] == move[1]:
          mmove["score"] += 1;
          contains = True  
      if contains == False:    
        ltm[f"{move[0]}"].append({"move":move[1], "score": 0})

  file = open('memory.py', 'w+')
  file.write(f"memory = {memory}")
  file.close()


# main game
def game():
  game = init_game()

  while True:
    # player moves
    game = get_player_piece(game)
    game.print_board()
    print("\n" + ("#" * 15) + "\n")
    
    # check if move ended game
    if not game_not_over(game.board, "C", "P")['bool']:
      print(f"The Winner is {game_not_over(game.board, 'C', 'P')['winner']}")
      break
    print(working_memory)
    save_memory(memory, working_memory)
    #computer moves
    game = computer_move(game)
    game.print_board()
    print(working_memory)
    # check if moev ended game
    if not game_not_over(game.board, "P", "C")['bool']:
      print(f"The Winner is {game_not_over(game.board, 'P', 'C')['winner']}")
      break
  save_memory(memory, working_memory)
  return check_replay()

game()