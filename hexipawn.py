import random
from library import *

current_game_state = {
  "board": [],
  "round": 0,
  "result": None
}

def create_board():
  return [
    ["C", "C", "C"],
    [" ", " ", " "],
    ["P", "P", "P"]
  ]

def print_board(board):
  for row in board:
    row_string = '|'
    for cell in row:
      row_string += f" {cell} |"
    print(row_string)
  print(f"\n{'#'*13}\n")
      

def check_possible_moves(board, up, notup):
  pieces = []
  row = 0
  while row != len(board):
    cell = 0
    while cell != len(board[row]):
      if board[row][cell] == up:
        moves = []
        if row+1 < len(board):
          if board[row+1][cell] == " ":
            moves.append([row+1, cell])

          if cell+1 < len(board[row+1]) and board[row+1][cell+1] == notup:
            moves.append([row+1, cell+1])

          if cell-1  >= 0 and board[row+1][cell-1] == notup:
            moves.append([row+1, cell-1])
        
        if len(moves) > 0:
          pieces.append([[row, cell], moves])
      cell += 1
    row += 1
  return pieces
  # [ all pieces
  #   [ piece information
  #     [piece, location],
  #     [
  #       [possible, move]
  #       [possible, move]
  #     ]
  #   ]
  # ]

def choose_move(pieces):
  piece = random.randint(0, len(pieces) - 1)
  move = random.randint(0, len(pieces[piece][1]) - 1)

  return [pieces[piece][0], pieces[piece][1][move]]

def check_for_win(board):
  return 'no-change'

def move_piece(piece, arr, board):
  local = arr[0]
  move = arr[1]
  while board[int(local[0])][int(local[1])] != piece:
    local = input(f"Thats not your piece on square {int(local[0])}/{int(local[1])}, choose again: ").split('/')
    move = input(f"Where would you like to move it: ").split('/')
  board[int(local[0])][int(local[1])] = " "
  board[int(move[0])][int(move[1])] = piece
  print_board(board)
  return {
    'piece': piece,
    'from': local,
    'to': move,
    'result': check_for_win(board)
  }

def save(lib):
  file = open('library.py', 'w+')
  file.write(f"library = {library}")
  file.close()

def update_lib(lib, rndnum, board, move):
  rnd = f'round_{rndnum}'
  addMove = True
  if rnd in lib:
    for libBoard in lib[f'round_{rndnum}']:
      if board == libBoard['board']:
        for libMove in libBoard['moves']:
          if move == libMove:
            addMove = False
        if addMove:
          libBoard['moves'].append(move)
  else:
    lib[rnd] = [{
      'board': board,
      'moves': [move]
    }]

def game():
  # init game
  rndnum = 0
  board = create_board()
  print("Welcome to Hexipawn")
  print_board(board)
  update_lib(library, rndnum, board, {})
  print("The player goes first.")

  # start game
  while rndnum < 8:
    rndnum += 1
    up = "P"
    print("please enter all locations like this: ")
    print("row / col (1/2 or 3/3)")
    pfrom = input("which piece would you like to move? ").split('/')
    pto = input("where would you like to move it to? ").split('/')
    move = move_piece(up, [pfrom, pto], board)
    update_lib(library, rndnum, board, move)
    rndnum += 1
    up = "C"
    move = move_piece(up, choose_move(
      check_possible_moves(board, up, "P")
      ),
      board
    )
    update_lib(library, rndnum, board, move)

  save(library)

game()
