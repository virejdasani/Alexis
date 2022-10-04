import random
class RockPaperScissors():
    def start():
        print('Rock Paper Scissors Game!')
        print('For Rock: Type 1\nFor Paper: Type 2\nFor Scissors: Type 3')

        option = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

        userInput = int(input('Your input:')) 
        #Gets the user input for the game

        alexisInput = random.randint(1,3)
        #Generating a random number for the bot

        if userInput == alexisInput:
            print('Draw!!\n' + 'We both picked '+option[alexisInput])

        elif userInput > alexisInput or (userInput == 1 and alexisInput == 3):
            print('You Won!\n' + 'I picked '+option[alexisInput]+' and you picked '+option[userInput])

        else:
            print('You Lose!\n' + 'I picked '+option[alexisInput]+' and you picked '+option[userInput])