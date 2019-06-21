from modules.computer import Computer
from modules.player import Player
from modules.memory import memory

class GameState:
  def __init__(self, memory=[], oldState=None):
    self.rnd = (oldState.rnd + 1) if oldState else 0
    self.memory = memory
    self.computer = oldState.computer if oldState else Computer()
    self.player = oldState.player if oldState else Player()
    self.winner = None

  def print_board(self):
    print()

    for cell in range(9):
      # start each row in the board
      if cell in [0, 3, 6]:
        print("\t\t", end="")
      
      # print piece in each box
      if cell in self.computer.pieces:
        print(" C ", end="")
      elif cell in self.player.pieces:
        print(" P ", end="")
      else:
        print("   ", end="")

      # print row separators
      if cell in [2, 5]:
        print("\n\t\t", "-"*11, sep="")
      elif cell == 8:
        print("\n")
      else:
        print("|", end="")

  def over(self):
    if self.player.crossed_board() or self.computer.has_moves(self) == None:
      self.winner = 'P'
      return True
    elif self.computer.crossed_board() or self.player.has_moves(self) == None:
      self.winner = 'C'
      return True
    else: 
      return False

  def save_memory(self):
    for move in self.memory:
      if str(move[0]) in memory:
        contains = False
        for mmove in memory[f"{move[0]}"]:
          if mmove["move"] == move[1]:
            if self.winner == "C":
              mmove["score"] += 1
            elif self.winner == "P":
              pass
            else:
              mmove["score"] += .5
            contains = True  
        if contains == False:    
          memory[f"{move[0]}"].append({"move":move[1], "score": 0})

    file = open('memory.py', 'w+')
    file.write(f"memory = {memory}")
    file.close()