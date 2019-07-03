from modules.computer import Computer
from modules.game_state import Game_State


computer = Computer()
state = Game_State.new()

def test_constructor():
  assert computer.pieces == [6, 7, 8]

def test_move():
  assert type(computer.move(state)) == type(state)
  assert state != computer.move(state)

def test_cross_board():
  assert computer.crossed_board() == False