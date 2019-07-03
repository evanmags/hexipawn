from typing import List
from random import choice

class Computer:
  def __init__(self):
    self.pieces = [0, 1, 2]

  def move(self, state, connection):
    # generate all possible combinations
    all_moves = []
    for piece in self.pieces:
      moves = self.piece_moves(state, piece)
      for move in moves:
        all_moves.append([piece, move])
    
    #query db for all moves that match the current board setup
    db = connection.cursor()
    db.execute("""SELECT "from", "to", "game_result"
                  FROM memory 
                  WHERE player_pieces = ? 
                  AND computer_pieces = ?""",
              (str(state.player.pieces), str(self.pieces)))

    moves = db.fetchall()          

    # add add moves from memory to adjust weighting
    for piece, to, res in moves:
      if res == 2:
        all_moves.append([piece, to])
    
    # choose move from weighted list
    (at, to) = choice(all_moves)
    self.pieces.remove(at)
    self.pieces.append(to)

    if to in state.player.pieces:
      state.player.pieces.remove(to)
    
    state.memory.append(([at, to], state.player.pieces[:], self.pieces[:]))

    state.rnd += 1

  def piece_moves(self, state, piece: int) -> List[int]:
    """
    takes in a game state and a selected location of a piece
    returns a list of integers representing result locations
    """
    pPieces = state.player.pieces
    moves = []

    # diagonal left
    if piece in [0, 1, 3, 4] and (piece + 4) in pPieces:
      moves.append(piece + 4)
    # diagonal right
    if piece in [1, 2, 3, 4] and (piece + 2) in pPieces:
      moves.append(piece + 2)

    # straight ahead
    if piece not in [6, 7, 8] and (piece + 3) not in pPieces:
      moves.append(piece + 3)
      
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

  def crossed_board(self):
    return any(x in self.pieces for x in [6, 7, 8])