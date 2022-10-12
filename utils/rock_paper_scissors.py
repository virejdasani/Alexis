import random

class RockPaperScissors():

    def start_game(self):
        computer = random.choice(["rock", "paper", "scissor"])
        while True:
            user = input("Select any one from -> rock paper scissor: ")
            if user in ["rock", "paper", "scissor"]:
                break
            else:
                print("Please select a valid choice")
        print(f'opponent choice : {computer}')
        if computer == user:
            print("Tie")
        elif computer == "paper" and user == "scissor":
            print(f'{user} cuts {computer}\ncongrats You win!')
        elif computer == "paper" and user == "rock":
            print(f'{computer} covers {user}\noops You lost!')
        elif computer == "scissor" and user == "paper":
            print(f'{computer} cuts {user}\noops You lost!')
        elif computer == "scissor" and user == "rock":
            print(f'{user} smashes {computer}\ncongrats You win!')
        elif computer == "rock" and user == "scissor":
            print(f'{computer} smashes {user}\noops You lost!')
        elif computer == "rock" and user == "paper":
            print(f'{user} covers {computer}\ncongrats You win!')
        self.playagain()

    def playagain(self):
        """ Ask user if he/she wants to play again or not """
        if input("Would you like to play again (Yes/No)? ").lower().startswith("y"):
            self.start_game()
        else:
            print("Bye")
