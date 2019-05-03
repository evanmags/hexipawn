import random
from modules.memory import memory
from modules.moves import check_possible_moves

class Computer:
  def __init__(self):
    self.piece1 = 6
    self.piece2 = 7
    self.piece3 = 8

  def move(self, state):
    moves = check_possible_moves(state.board, "C", "P")
    for move in memory[f"{state.rnd}"]:
      if move['move'] in moves:
        for i in range(move['score']):
          moves.append(move['move'])
          i
    ch = self.choose_move(moves)
    piece = state.board[ch[0]]
    return state.move(piece, ch[1])

  def choose_move(self, moves):
    # getting passed an array of moves and picking one
    piece = random.randint(0, len(moves) - 1)
    return moves[piece]