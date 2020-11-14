
# Initialising the game board to empty strings
board = {
    '1': '  ', '2': '   ', '3': '  ',
    '4': '  ', '5': '   ', '6': '  ',
    '7': '  ', '8': '   ', '9': '  '
}

# The x for the left and right columns 
LRx = ' X'
# The x for the centre column
Cx = ' X '
# The o for the left and right columns 
LRo = ' O'
# The o for the centre column
Co = ' O '


boardEnd = '------------------------------------'


# Prints the board showing the numbers for the input
print(' 1 | 2 | 3 ')
print('---+---+---')
print(' 4 | 5 | 6 ')
print('---+---+---')
print(' 7 | 8 | 9 ')
print(boardEnd)
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

while won == False:

    if board['1'] == LRx and board['2'] == Cx and board['3'] == LRx:
        print('Player 1 wins!')
        break 
    
    if moves > 8:
        break

    while player == 1 and won == False:

        
        # Check if tie
        if moves > 8:
            break
        
        # Display the board with any changes
        print(board['1'] + ' |' + board['2'] + '|' + board['3'])
        print('---+---+---')
        print(board['4'] + ' |' + board['5'] + '|' + board['6'])
        print('---+---+---')
        print(board['7'] + ' |' + board['8'] + '|' + board['9'])


        # Check if there is a winner
        # For player 1
        # First row
        if board['1'] == LRx and board['2'] == Cx and board['3'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # Second row
        elif board['4'] == LRx and board['5'] == Cx and board['6'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # Third row
        elif board['7'] == LRx and board['8'] == Cx and board['9'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # First column
        elif board['1'] == LRx and board['4'] == LRx and board['7'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # Second column
        elif board['2'] == LRx and board['5'] == LRx and board['8'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # Third column
        elif board['3'] == LRx and board['6'] == LRx and board['9'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # Diagonal - top left to bottom right
        elif board['1'] == LRx and board['5'] == Cx and board['9'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # Diagonal - bottom left to top right
        elif board['7'] == LRx and board['5'] == Cx and board['3'] == LRx:
            print('Player 1 wins!')
            won = True
            break

        # For player 2
        # First row
        elif board['1'] == LRo and board['2'] == Co and board['3'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # Second row
        elif board['4'] == LRo and board['5'] == Co and board['6'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # Third row
        elif board['7'] == LRo and board['8'] == Co and board['9'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # First column
        elif board['1'] == LRo and board['4'] == LRo and board['7'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # Second column
        elif board['2'] == LRo and board['5'] == LRo and board['8'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # Third column
        elif board['3'] == LRo and board['6'] == LRo and board['9'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # Diagonal - top left to bottom right
        elif board['1'] == LRo and board['5'] == Co and board['9'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # Diagonal - bottom left to top right
        elif board['7'] == LRo and board['5'] == Co and board['3'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        else:

            # Take input for the number of the square to
            ip = input('Player 1:\n')
            moves += 1

            # Try getting input: if it is between 1 & 9, 
            try:
                if ip in board and board[ip] == '  ' or board[ip] == '   ':

                    # Check to see which 'X' to insert (LRx or Cx)
                    if ip == '2' or ip == '5' or ip == '8':
                        board[ip] = Cx

                        # Check if the board is full 
                        if moves > 8:
                            break

                        # Change player
                        player = 2 
                        print(boardEnd)
                    else:
                        board[ip] = LRx

                        # Check if the board is full 
                        if moves > 8:
                            break

                        # Change player
                        player = 2   
                        print(boardEnd)

                # Check if that box is taken 
                elif board[ip] == ' X' or board[ip] == ' X ' or board[ip] == ' O' or board[ip] == ' O ':
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

        print(board['1'] + ' |' + board['2'] + '|' + board['3'])
        print('---+---+---')
        print(board['4'] + ' |' + board['5'] + '|' + board['6'])
        print('---+---+---')
        print(board['7'] + ' |' + board['8'] + '|' + board['9'])

        # Check if there is a winner
        # For player 1
        # First row
        if board['1'] == LRx and board['2'] == Cx and board['3'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # Second row
        elif board['4'] == LRx and board['5'] == Cx and board['6'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # Third row
        elif board['7'] == LRx and board['8'] == Cx and board['9'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # First column
        elif board['1'] == LRx and board['4'] == LRx and board['7'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # Second column
        elif board['2'] == LRx and board['5'] == LRx and board['8'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # Third column
        elif board['3'] == LRx and board['6'] == LRx and board['9'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # Diagonal - top left to bottom right
        elif board['1'] == LRx and board['5'] == Cx and board['9'] == LRx:
            print('Player 1 wins!')
            won = True
            break
        # Diagonal - bottom left to top right
        elif board['7'] == LRx and board['5'] == Cx and board['3'] == LRx:
            print('Player 1 wins!')
            won = True
            break

        # For player 2
        # First row
        elif board['1'] == LRo and board['2'] == Co and board['3'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # Second row
        elif board['4'] == LRo and board['5'] == Co and board['6'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # Third row
        elif board['7'] == LRo and board['8'] == Co and board['9'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # First column
        elif board['1'] == LRo and board['4'] == LRo and board['7'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # Second column
        elif board['2'] == LRo and board['5'] == LRo and board['8'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # Third column
        elif board['3'] == LRo and board['6'] == LRo and board['9'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # Diagonal - top left to bottom right
        elif board['1'] == LRo and board['5'] == Co and board['9'] == LRo:
            print('Player 2 wins!')
            won = True
            break
        # Diagonal - bottom left to top right
        elif board['7'] == LRo and board['5'] == Co and board['9'] == LRo:
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
                if ip in board and board[ip] == '  ' or board[ip] == '   ':

                    # Check to see which 'O' to insert (LRo or Co)
                    if ip == '2' or ip == '5' or ip == '8':
                        board[ip] = Co

                        # Check if the board is full 
                        if moves > 8:
                            break

                        # Change player
                        player = 1 
                        print(boardEnd)
                    else:
                        board[ip] = LRo

                        # Check if the board is full 
                        if moves > 8:
                            break

                        # Change player
                        player = 1  
                        print(boardEnd)

                # Check if that box is taken 
                elif board[ip] == ' X' or board[ip] == ' X ' or board[ip] == ' O' or board[ip] == ' O ':
                    print('That spot is taken')   
                    moves -= 1     


            # If the input is not from the board (1-9)
            except KeyError as identifier:
                if "exit" in ip:
                    exit(1)
                else:    
                    print('INVALID')
                    moves -= 1
                    break


print('DONE')
