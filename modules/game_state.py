from modules.piece import Piece
from modules.computer import Computer
from modules.player import Player
from modules.memory import memory

class Game_State:
  def __init__(self, memory=[], oldState=None):
    self.rnd = oldState.rnd + 1 if oldState and oldState.rnd else 0
    self.memory = memory
    self.computer = oldState.computer if oldState and oldState.computer else Computer()
    self.player = oldState.player if oldState and oldState.player else Player()
    self.winner = ''

  @classmethod
  def new(self):
    board = [None] * 9
    i = 0
    while i < 3:
      board[i] = Piece("C", i)
      board[i + 6] = Piece("P", i + 6)
      i += 1
    return Game_State(board)

  # print the game board
  def print_board(self):
    for x in range(3):
      row_str = ''
      for y in range(3):
        cell = y + (x * 3)
        row_str += f" C " if cell in self.computer.pieces else f" P " if cell in self.player.pieces else '   '
        row_str += f"|" if (cell + 1) % 3 != 0 else ''
      print(row_str)
      if x < 2:
        print("-"*11)

  # move a piece in the board
  def move(self, p, to):
    board = []
    self.memory.append([self.rnd, [p.at, to]])
    board[p.at] = None
    board[to] = Piece(p.symbol, to)
    return Game_State(board, self)
  
  def over(self):
    if self.player.crossed_board() or self.computer.crossed_board():
      return True
    else:
      return False

  def save_memory(self, state):
    for move in self.memory:
      if f"{move[0]}" in memory:
        contains = False
        for mmove in memory[f"{move[0]}"]:
          if mmove["move"] == move[1]:
            if state['winner'] == "C":
              mmove["score"] += 1
            elif state['winner'] == "P":
              pass
            else:
              mmove["score"] += .5
            contains = True  
        if contains == False:    
          memory[f"{move[0]}"].append({"move":move[1], "score": 0})

    file = open('memory.py', 'w+')
    file.write(f"memory = {memory}")
    file.close()