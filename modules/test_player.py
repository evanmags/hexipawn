from modules.player import Player
from modules.memory import memory
from modules.game_state import Game_State


player = Player()
state = Game_State.new()

def test_constructor():
  assert player.pieces == [0, 1, 2]

def test_move():
  assert type(player.move(state)) == type(state)
  assert state != player.move(state)

def test_cross_board():
  assert player.crossed_board() == False