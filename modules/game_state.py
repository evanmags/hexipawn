from modules.piece import Piece
from modules.computer import Computer

class Game_State:
  def __init__(self, board, rnd):
    self.board = board
    self.rnd = rnd or 0
    self.memory = []
    self.computer = Computer()
    self.player = Player()

  @classmethod
  def new(self):
    board = [None] * 9
    i = 0
    while i < 3:
      board[i] = Piece("C", i)
      board[i + 6] = Piece("P", i + 6)
      i += 1
    return Game_State(board, 0)

  # print the game board
  def print_board(self):
    x = 1
    row_str = ''
    for piece in self.board:
      if piece != None:
        piece = piece.symbol
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
    self.memory.append([self.rnd, [p.at, to]])
    board = list(self.board)
    board[p.at] = None
    board[to] = Piece(p.symbol, to)
    return Game_State(board, self.rnd + 1)
  
  def game_over(self):
    pass