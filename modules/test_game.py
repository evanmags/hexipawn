from modules.game_state import Game_State

game = Game_State.new()

def test_init():
  assert type(game.board) == list
  assert game.rnd == 0
  assert game.memory == []
  assert game.winner == ''

def test_over():
  assert game.over() == False