import numpy as np

from scipy.signal import convolve2d
import os 

class ConnectFour():
    def __init__(self):
        """
        Initializes the player boards
        """
        self.player_one_board = self.initialize_board()
        self.player_two_board = self.initialize_board()

    def _clear(self): # private method to clear terminal lines for overwriting old game board in terminal
        os.system('cls' if os.name=='nt' else 'clear')

    def initialize_board(self):
        """
        Initializes an empty board of 6x7

        Returns:
            _type_: _description_
        """
        board = np.zeros((6,7))
        return board

    def make_move(self, board, selected_column):
        """
        Checks the location of the move given a specified column on the board

        Args:
            board (np.ndarray): 6x7 board containing all player moves 
            selected_column (int): specifies a column within the board

        Returns:
            None: Returns None if the column has been completly filled up
            Tuple: Returns the (X,Y) coordinates if a move can be made
        """
        try:
            selected_column = int(selected_column)
        except:
            return None

        if selected_column < 0 or selected_column > 6:
            return None

        x_loc = selected_column
        y_loc = None
        board_column = board.T[selected_column]

        for i in range(len(board_column)-1, -1, -1):
            if board_column[i] == 0:
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

    def display_board(self,grid_size,board_info,empty_char = '~', player1_char = 'X', player2_char = 'O'):
        """
        Display a board in a larger more user friendly format

        Args:
            grid_size 2-tuple (rows, columns): Size of desired board grid
            board_info (np.ndarray): Board containing both players moves information
            empty_char (optional, default ~): character to represent empty board slot
            player1_char (optional, default X): character to represent player 1 placed slot
            player2_char (optional, default O): character to represent player 2 placed slot

        Returns:
            None: prints updated board to console
        """
        # First row
        print(f" ", end='')
        for j in range(grid_size[1]):
            print(f"| {j} ", end='')
        print("| ")
        print((grid_size[1]*4+4)*"-")

        # Other rows
        for i in range(grid_size[0]):
            print(f" ", end='')
            for j in range(grid_size[1]):
                if board_info[i][j] == 1:
                    print(f"| {player1_char} ", end='')
                elif board_info[i][j] == 2:
                    print(f"| {player2_char} ", end='')
                else:
                    print(f"| {empty_char} ", end='')
            print("| ")


    def start_game(self):
        """
        Main code to run the connect four game
        """
        turn_counter = 0
        game_over = False
        winning_player = None
        player1_icon = 'X' # Character in grid to represent player 1, Must be ONE letter character or else grid will be misaligned
        player2_icon = 'O' # Character in grid to represent player 2, Must be ONE letter character or else grid will be misaligned
        while not game_over:
            merged_board = self.get_merged_board()
            self._clear() #clear terminal so one board exists
            self.display_board((6,7),merged_board, player1_char=player1_icon, player2_char=player2_icon)
            player = (turn_counter % 2) + 1
            turn_counter += 1
            if player == 1:
                player_icon = player1_icon
            else:
                player_icon = player2_icon
            #Ask for player input
            selection = input(f"Player {player} ({player_icon}), select your column (0-6):")
            
            # Check for surrender
            if selection == "ff":
                winning_player = 1 if player == 2 else 2
                print(f"Player {player} has forfeited! Player {winning_player} wins!")
                game_over = True
                break

            # Process selected move
            move = self.make_move(merged_board, selection)
            while move is None:
                selection = input("\tThat was an invalid move, select your column (0-6):")
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
            self.display_board((6,7),merged_board, player1_char=player1_icon, player2_char=player2_icon)
            print(f"Player {winning_player} has won!")
        self.winning_player = winning_player
        return