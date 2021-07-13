
class TicTacToe():
    def __init__(self):
        # Initialising the game board to empty strings
        self.board = {
            '1': '  ', '2': '   ', '3': '  ',
            '4': '  ', '5': '   ', '6': '  ',
            '7': '  ', '8': '   ', '9': '  '
        }

        # The x for the left and right columns
        self.LRx = ' X'
        # The x for the centre column
        self.Cx = ' X '
        # The o for the left and right columns
        self.LRo = ' O'
        # The o for the centre column
        self.Co = ' O '

        self.boardEnd = '------------------------------------'

    def start_game(self):
        """
        This method is used to start the game after the class has been created
        :return: Nothing is returned
        """
        # Prints the board showing the numbers for the input
        print(' 1 | 2 | 3 ')
        print('---+---+---')
        print(' 4 | 5 | 6 ')
        print('---+---+---')
        print(' 7 | 8 | 9 ')
        print(self.boardEnd)
        print("Type 'exit' to exit")

        # Player 1 starts
        player = 1
        # Symbol is X for Player 1
        symbol = 'X'
        # The number of plays (cannot be greater than 9)
        moves = 0
        # To check if there is a winner
        won = False

        # Switch symbol depending on the player (1 = X, 2 = O)
        if player != 1:
            symbol = 'O'

        while not won:
            if self.board['1'] == self.LRx and self.board['2'] == self.Cx and self.board['3'] == self.LRx:
                print('Player 1 wins!')
                break

            if moves > 8:
                break

            while player == 1 and won == False:
                # Check if tie
                if moves > 8:
                    break

                # Display the board with any changes
                print(self.board['1'] + ' |' + self.board['2'] + '|' + self.board['3'])
                print('---+---+---')
                print(self.board['4'] + ' |' + self.board['5'] + '|' + self.board['6'])
                print('---+---+---')
                print(self.board['7'] + ' |' + self.board['8'] + '|' + self.board['9'])

                # Check if there is a winner
                # For player 1
                # First row
                if self.board['1'] == self.LRx and self.board['2'] == self.Cx and self.board['3'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # Second row
                elif self.board['4'] == self.LRx and self.board['5'] == self.Cx and self.board['6'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # Third row
                elif self.board['7'] == self.LRx and self.board['8'] == self.Cx and self.board['9'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # First column
                elif self.board['1'] == self.LRx and self.board['4'] == self.LRx and self.board['7'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # Second column
                elif self.board['2'] == self.LRx and self.board['5'] == self.LRx and self.board['8'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # Third column
                elif self.board['3'] == self.LRx and self.board['6'] == self.LRx and self.board['9'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # Diagonal - top left to bottom right
                elif self.board['1'] == self.LRx and self.board['5'] == self.Cx and self.board['9'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # Diagonal - bottom left to top right
                elif self.board['7'] == self.LRx and self.board['5'] == self.Cx and self.board['3'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break

                # For player 2
                # First row
                elif self.board['1'] == self.LRo and self.board['2'] == self.Co and self.board['3'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # Second row
                elif self.board['4'] == self.LRo and self.board['5'] == self.Co and self.board['6'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # Third row
                elif self.board['7'] == self.LRo and self.board['8'] == self.Co and self.board['9'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # First column
                elif self.board['1'] == self.LRo and self.board['4'] == self.LRo and self.board['7'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # Second column
                elif self.board['2'] == self.LRo and self.board['5'] == self.LRo and self.board['8'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # Third column
                elif self.board['3'] == self.LRo and self.board['6'] == self.LRo and self.board['9'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # Diagonal - top left to bottom right
                elif self.board['1'] == self.LRo and self.board['5'] == self.Co and self.board['9'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # Diagonal - bottom left to top right
                elif self.board['7'] == self.LRo and self.board['5'] == self.Co and self.board['3'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                else:

                    # Take input for the number of the square to
                    ip = input('Player 1:\n')
                    moves += 1

                    # Try getting input: if it is between 1 & 9,
                    try:
                        if ip in self.board and self.board[ip] == '  ' or self.board[ip] == '   ':

                            # Check to see which 'X' to insert (LRx or Cx)
                            if ip == '2' or ip == '5' or ip == '8':
                                self.board[ip] = self.Cx

                                # Check if the board is full
                                if moves > 8:
                                    break

                                # Change player
                                player = 2
                                print(self.boardEnd)
                            else:
                                self.board[ip] = self.LRx

                                # Check if the board is full
                                if moves > 8:
                                    break

                                # Change player
                                player = 2
                                print(self.boardEnd)

                        # Check if that box is taken
                        elif self.board[ip] == ' X' or self.board[ip] == ' X ' or self.board[ip] == ' O' or self.board[ip] == ' O ':
                            print('That spot is taken')
                            moves -= 1

                    # If the input is not from the board (1-9) or exit

                    except KeyError as identifier:
                        if "exit" in ip:
                            exit(1)
                        else:
                            print('INVALID')
                            moves -= 1
                            break

            while player == 2 and won == False:
                # Check if tie
                if moves > 8:
                    break

                print(self.board['1'] + ' |' + self.board['2'] + '|' + self.board['3'])
                print('---+---+---')
                print(self.board['4'] + ' |' + self.board['5'] + '|' + self.board['6'])
                print('---+---+---')
                print(self.board['7'] + ' |' + self.board['8'] + '|' + self.board['9'])

                # Check if there is a winner
                # For player 1
                # First row
                if self.board['1'] == self.LRx and self.board['2'] == self.Cx and self.board['3'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # Second row
                elif self.board['4'] == self.LRx and self.board['5'] == self.Cx and self.board['6'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # Third row
                elif self.board['7'] == self.LRx and self.board['8'] == self.Cx and self.board['9'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # First column
                elif self.board['1'] == self.LRx and self.board['4'] == self.LRx and self.board['7'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # Second column
                elif self.board['2'] == self.LRx and self.board['5'] == self.LRx and self.board['8'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # Third column
                elif self.board['3'] == self.LRx and self.board['6'] == self.LRx and self.board['9'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # Diagonal - top left to bottom right
                elif self.board['1'] == self.LRx and self.board['5'] == self.Cx and self.board['9'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break
                # Diagonal - bottom left to top right
                elif self.board['7'] == self.LRx and self.board['5'] == self.Cx and self.board['3'] == self.LRx:
                    print('Player 1 wins!')
                    won = True
                    break

                # For player 2
                # First row
                elif self.board['1'] == self.LRo and self.board['2'] == self.Co and self.board['3'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # Second row
                elif self.board['4'] == self.LRo and self.board['5'] == self.Co and self.board['6'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # Third row
                elif self.board['7'] == self.LRo and self.board['8'] == self.Co and self.board['9'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # First column
                elif self.board['1'] == self.LRo and self.board['4'] == self.LRo and self.board['7'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # Second column
                elif self.board['2'] == self.LRo and self.board['5'] == self.LRo and self.board['8'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # Third column
                elif self.board['3'] == self.LRo and self.board['6'] == self.LRo and self.board['9'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # Diagonal - top left to bottom right
                elif self.board['1'] == self.LRo and self.board['5'] == self.Co and self.board['9'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                # Diagonal - bottom left to top right
                elif self.board['7'] == self.LRo and self.board['5'] == self.Co and self.board['9'] == self.LRo:
                    print('Player 2 wins!')
                    won = True
                    break
                else:

                    # Take input for the number of the square to
                    ip = input('Player 2:\n')
                    moves += 1

                    # Try getting input: if it is between 1 & 9,
                    try:
                        # Check if that box is empty
                        if ip in self.board and self.board[ip] == '  ' or self.board[ip] == '   ':

                            # Check to see which 'O' to insert (LRo or Co)
                            if ip == '2' or ip == '5' or ip == '8':
                                self.board[ip] = self.Co

                                # Check if the board is full
                                if moves > 8:
                                    break

                                # Change player
                                player = 1
                                print(self.boardEnd)
                            else:
                                self.board[ip] = self.LRo

                                # Check if the board is full
                                if moves > 8:
                                    break

                                # Change player
                                player = 1
                                print(self.boardEnd)

                        # Check if that box is taken
                        elif self.board[ip] == ' X' or self.board[ip] == ' X ' or self.board[ip] == ' O' or self.board[ip] == ' O ':
                            print('That spot is taken')
                            moves -= 1

                    # If the input is not from the board (1-9)
                    except KeyError as identifier:
                        if "exit" in ip:
                            return None
                        else:
                            print('INVALID')
                            moves -= 1
                            break

            print('DONE')
