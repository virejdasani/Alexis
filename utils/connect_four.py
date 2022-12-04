import numpy as np

from scipy.signal import convolve2d


class ConnectFour():
    def __init__(self):
        #initialize board
        self.player_one_board = self.initialize_board()
        self.player_two_board = self.initialize_board()
    
    def initialize_board(self):
        """
        Initializes an empty board of 6x7

        Returns:
            _type_: _description_
        """
        board = np.zeros((6,7))
        return board

    def make_move(self, board, selected_row):
        """
        Checks the location of the move given a specified row on the board

        Args:
            board (np.ndarray): 6x7 board containing all player moves 
            selected_row (int): specifies a row within the board

        Returns:
            None: Returns None if the row has been completly filled up
            Tuple: Returns the (X,Y) coordinates if a move can be made
        """
        try:
            selected_row = int(selected_row)
        except:
            return None

        if selected_row < 0 or selected_row > 6:
            return None

        x_loc = selected_row
        y_loc = None
        board_row = board.T[selected_row]

        for i in range(len(board_row)-1, -1, -1):
            if board_row[i] == 0:
                y_loc = i
                break

        if y_loc is None:
            return None
        return (x_loc, y_loc)

    def check_win_condition(self, board):
        """
        Checks to see if a player's board holds a winning move. To make this more efficient,
        instead of iterating we convolve the winner states as kernels across the player board.

        Args:
            board (np.ndarray): Numpy array containing the moves of one player

        Returns:
            bool: True if the board holds a winning move, False otherwise 
        """
        horiz_kernel = np.array([[1, 1, 1, 1]])
        vert_kernel = np.array([[1, 1, 1, 1]]).T
        diag_kernel_1 = np.eye(4, dtype=np.uint8)
        diag_kernel_2 = np.fliplr(diag_kernel_1)
        detection_kernels = [horiz_kernel, vert_kernel, diag_kernel_1, diag_kernel_2]

        for detection_kernel in detection_kernels:
            if (convolve2d(board, detection_kernel, mode="valid") == 4).any():
                return True
        return False

    def get_merged_board(self):
        """
        Merges the two player's boards to see all positions that have been played.

        Args:
            board1 (np.ndarray): Player one's board containing their moves
            board2 (np.ndarray): Player two's board containing their moves

        Returns:
            np.ndarray: Board containing both players moves with distinction
        """
        merged_board = np.zeros_like(self.player_one_board, dtype=np.int8)
        merged_board[self.player_one_board == 1] = 1
        merged_board[self.player_two_board == 1] = 2
        return merged_board

    def start_game(self):
        """
        Main code to run the connect four game
        """
        turn_counter = 0
        game_over = False
        winning_player = None
        while not game_over:
            merged_board = self.get_merged_board()
            print(f"\n{merged_board}")
            print(" ---------------")
            print(" |0|1|2|3|4|5|6|")

            player = (turn_counter % 2) + 1
            turn_counter += 1

            #Ask for player input
            selection = input(f"Player {player}, select your row (0-6):")
            
            # Check for surrender
            if selection == "ff":
                print(f"Player {player} has forfeited! Player {1 if player == 2 else 2} wins!")
                game_over = True
                break

            # Process selected move
            move = self.make_move(merged_board, selection)
            while move is None:
                selection = input("\tThat was an invalid move, select your row (0-6):")
                move = self.make_move(merged_board, selection)

            # Record player move
            if player == 1:
                player_board = self.player_one_board
            elif player == 2:
                player_board = self.player_two_board

            player_board[move[1]][move[0]]= 1
            if self.check_win_condition(player_board): 
                game_over = True
                winning_player = player

            if turn_counter == 42:
                game_over = True

        if winning_player is False:
            print("The board has been filled, it's a tie!")
        else:
            merged_board = self.get_merged_board()
            print(f"\n{merged_board}")
            print(f"Player {winning_player} has won!")