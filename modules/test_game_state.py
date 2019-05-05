from modules.game_state import Game_State

game = Game_State.new()

def test_init():
  assert type(game.board) == list
  assert game.rnd == 0
  assert game.memory == []
  assert game.winner == ''

def test_over():
  assert game.over() == False

def test_save_memory():
  game.save_memory(game)
  from modules.memory import memory
  assert memory != None
  assert type(memory) == dict