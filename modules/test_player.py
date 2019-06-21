from modules.player import Player
from modules.memory import memory
from modules.game_state import Game_State


state = Game_State()
player = state.player

def test_constructor():
  assert player.pieces == [6, 7, 8]

def test_has_moves_True():
  assert player.has_moves(state) == True

def test_has_moves_False():
  state.computer.pieces = [3, 4, 5]
  assert player.has_moves(state) == False

def test_cross_board():
  assert player.crossed_board() == False