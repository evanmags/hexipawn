from modules.moves import check_possible_moves

class Player:
  def __init__(self):
    self.pieces = [0, 1, 2]

  def move(self, state):
    return self.get_player_move(state)

  def get_player_piece(self, state):
    while True:
      print("Your move: please select a piece: ")
      select = self.valid_sanitized_input()
      if select in self.pieces:
        break
      else:
        print("You do not have a piece at that location.")
    return self.get_player_move(select, state)

  def get_player_move(self, at, state):
    moves = check_possible_moves(state.board, "P", "C")
    while True:
      print("Your move: please select a move (row/col)")
      move = self.valid_sanitized_input()
      if [at, move] in moves:
        p = state.board[at]
        return state.move(state, p, move)
      else:
        print("That is not a valid move.")
    
  def valid_sanitized_input(self):
    select = int(input(">>> ")) - 1
    if select > 8 or select < 0:
      print("Please select a valid location (row/col)")
      return self.valid_sanitized_input()
    return select
  
  def crossed_board(self):
    return any(x in self.pieces for x in [6, 7, 8])
    