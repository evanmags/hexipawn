from modules.moves import check_possible_moves

def game_not_over(board, up, notup):
  if len(check_possible_moves(board, up, notup)) == 0:
    return {
      'bool': False,
      'winner': notup
    }

  if len(check_possible_moves(board, notup, up)) == 0:
    return {
      'bool': False,
      'winner': up
    }

  return {
    'bool': True,
    'winner': None
  }