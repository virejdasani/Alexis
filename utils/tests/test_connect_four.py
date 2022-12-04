import pytest, numpy as np
from unittest.mock import patch, call, Mock
import builtins
import sys
from utils.connect_four import ConnectFour


class TestConnectFour:
    def test_init(self):
        """
        Test that the game is initialized correctly
        :return:
        """
        game = ConnectFour()
        assert (game.player_one_board == np.zeros((6,7))).all()
        assert (game.player_two_board == np.zeros((6,7))).all()

    @pytest.mark.parametrize("move, expected_res", [
                                                        [[0],(0, 5)], 
                                                        [[1],(1, 5)], 
                                                        [[2],(2, 5)],
                                                        [[0,0],(0, 4)],
                                                        [[9],None], # Check illegal move
                                                        [[-1],None], # Check illegal move
                                                        [['dummyinputstring'],None] # Check illegal move
                                                        ])
    def test_make_move(self,move, expected_res):
        """
        Test that user input is correctly converted to a move, and that the move is valid and applied to the board.
        :return:
        """
        game = ConnectFour()
        for m in move:
            ret = game.make_move(game.player_one_board, m)
            if ret is None:
                break
            game.player_one_board[ret[1],ret[0]] = 1
        assert ret == expected_res

        
    @pytest.mark.parametrize("moves, expected_res", [
                                                    [[(0,0),(1,0),(2,0),(3,0)],True], #Check vertical win
                                                    [[(0,0),(0,1),(0,2),(0,3)],True], #Check horizontal win
                                                    [[(0,0),(1,1),(2,2),(3,3)],True], #Check diag win
                                                    [[(0,0),(2,2),(3,3)],False],      #Check impossible board is false
                                                    [[(0,0),(0,2),(0,3)],False]      #Check impossible board is false
                                                    ])
    def test_check_win_condition(self,moves, expected_res):
        """
        Test that the game correctly identifies a set of moves as a win condition
        :return:
        """

        game = ConnectFour()
        assert game.check_win_condition(game.player_one_board) == False
        for move in moves:
            game.player_one_board[move[0]][move[1]] = 1

        assert game.check_win_condition(game.player_one_board) == expected_res
        


    def test_get_merged_board(self):
        """
        Test that the merged board is correctly generated
        :return:
        """
        game = ConnectFour()
        game.player_one_board[0][0] = 1
        game.player_two_board[0][1] = 1
        merged_board = game.get_merged_board()
        assert merged_board[0][0] == 1
        assert merged_board[0][1] == 2

    @patch('builtins.input', side_effect=['ff'])
    def test_forfeit(self, mock_input):
        """
        Test that the game ends when player 1 forfeits
        :param mock_input:
        :return:
        """
        game = ConnectFour()
        game.start_game()
        assert game.winning_player == 2

    def test_player_2_forfeit(self):
        """
        Test that the game ends when player 2 forfeits.
        :return:
        """
        mock = Mock()
        mock.side_effect = ['0', 'ff']
        with patch('builtins.input', mock):
            game = ConnectFour()
            game.start_game()
            assert game.winning_player == 1



