def check_possible_moves(board, up, notup):
  moves = []
  for cell in board:
    if cell != None and cell.symbol == up:
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
  return moves 

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
      if board[position + 2] != None and board[position + 2].symbol == "P":
        if position != 0 and position != 3 and position != 6: # prevent jumping
          return True

  if you == "P":
    if position - 4 >= 0:
      if board[position - 4] != None and board[position - 4].symbol == "C":
        if position != 6:  # prevent jumping
          return True
  return False

def is_diagonal_right(board, position, you):
  if you == "C":
    if position + 4 < 9:
      if board[position + 4] != None and board[position + 4].symbol == "P":
        if position != 2: # prevent jumping
          return True

  if you == "P":
    if position - 2 >=0:
      if board[position - 2] != None and board[position - 2].symbol == "C":
        if position != 2 and position != 5 and position != 8: # prevent jumping
          return True
  return False
