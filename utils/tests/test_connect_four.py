import pytest
import numpy as np

from connect_four import ConnectFour

# Test board initialization
def test_board_initialization():
    game = ConnectFour()
    assert (game.player_one_board == np.zeros((6,7))).all()
    assert (game.player_two_board == np.zeros((6,7))).all()


# Test state detection (win, lose, draw)

# Test move selection (Legal and illegal)
