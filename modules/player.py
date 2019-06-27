from typing import List, NewType

class Player:
  def __init__(self):
    self.pieces = [6, 7, 8]

  def move(self, state) -> None:
    """
    gets piece location and move location from user
    removes piece from pices and adds the new pieve location
    """
    at = self.get_player_piece(state)
    to = self.get_player_move(at, state)
    
    self.pieces.remove(at)
    self.pieces.append(to)

    if to in state.computer.pieces:
      state.computer.pieces.remove(to)

    state.memory.append(([at, to], self.pieces[:], state.computer.pieces[:]))

    state.rnd += 1

  def get_player_piece(self, state) -> int:
    """
    accepts GameState
    Prompts user for input and continues to prompt until player selects one of their pieces
    returns int representing piece location
    """
    while True:
      print("Your move: please select a piece: ")
      selectedPiece = self.valid_sanitized_input()
      if selectedPiece in self.pieces:
        return selectedPiece
      else:
        print("You do not have a piece at that location.")

  def get_player_move(self, at: int, state) -> List[int]:
    """
    prompts the user to select a board location to move their piece to
    continues to prompt until a valid move is selected
    returns a list containing the position of the piece and the move location.
    """
    moves = self.piece_moves(state, at)
    while True:
      print("Your move: please select a move (row/col)")
      move = self.valid_sanitized_input()
      if move in moves:
        return move
      else:
        print("That is not a valid move.")
  
  def piece_moves(self, state, piece: int) -> List[int]:
    """
    takes in a game state and a selected location of a piece
    returns a list of integers representing result locations
    """
    cPieces = state.computer.pieces
    moves = []

    # diagonal left
    if piece in [4, 5, 7, 8] and (piece - 4) in cPieces:
      moves.append(piece - 4)
    # diagonal right
    if piece in [3, 4, 6, 7] and (piece - 2) in cPieces:
      moves.append(piece - 2)

    # straight ahead
    if piece not in [0, 1, 2] and (piece - 3) not in cPieces:
      moves.append(piece - 3)
      
    return moves

  def has_moves(self, state) -> bool:
    """
    accepts a GameState,
    returns True iff any possible moves are found,
      otherwise False
    """
    for piece in self.pieces:
      moves = self.piece_moves(state, piece)
      if len(moves) > 0:
        return True

    return False

  def valid_sanitized_input(self) -> int:
    """
    prompts user for input,
    continutes to prompt until a valid board position is selected
    returns int
    """

    inp = input(">>> ")

    try:
      select = int(inp) - 1
    except:
      return self.valid_sanitized_input()

    if 0 > select > 8:
      print("Please select a valid location [1 -> 9]")
      return self.valid_sanitized_input()
    return select
  
  def crossed_board(self) -> bool:
    """
    checks for if any player pieces are in 'cross-board' positions
    returns boolean
    """
    return any(x in self.pieces for x in [0, 1, 2])
    