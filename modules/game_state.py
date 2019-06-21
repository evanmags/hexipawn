from modules.computer import Computer
from modules.player import Player
from modules.memory import memory

class GameState:
  def __init__(self):
    self.rnd = 0
    self.memory = []
    self.computer = Computer()
    self.player = Player()
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

  def over(self, justPlayed):
    if not self.computer.has_moves(self) and not self.player.has_moves(self):
      self.winner = justPlayed

    if self.player.crossed_board() or not self.computer.has_moves(self):
      self.winner = 'P'
      return True
    elif self.computer.crossed_board() or not self.player.has_moves(self):
      self.winner = 'C'
      return True
    else: 
      return False

  def save_memory(self):
    for rnd, move in enumerate(self.memory):
      if rnd in memory:
        contains = False
        for saved in memory[rnd]:
          if saved["move"] == move:
            contains = True
            if self.winner == "C":
              saved['score'] += 1
            elif self.winner == "P":
              pass
            else:
              saved["score"] += .5 
        if not contains:    
          memory[rnd].append({"move":move, "score": 0})
      else:
        memory[rnd] = [ {"move":move, "score": 0} ]

    with open('modules/memory.py', 'w+') as file:
      file.write(f"memory = {memory}")
      file.close()