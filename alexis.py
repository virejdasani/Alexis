# Alexis - YOUR PERSONAL ROBOT BUTLER
import datetime
from datetime import date
import random
import webbrowser
import wikipedia
import speech_recognition as sr

# For request errors
import requests
# For email
import smtplib
# For getting password anonymously
import getpass
from utils import response_consts as resconst
from utils.tictactoe import TicTacToe

'''
RULES
'''
'''
# \033[36m (Blue) for all responses
# \033[1;32;40m (Green) for 'Enter Command: ' phrase
'''

# KEYWORDS:
'''
# "open" is reserved to open websites in the browser
# "search" is for wikipedia
# "google" is to google search
'''

finished = False
speechRecog = False


# Inputs
agreeInput = ["yes", "y", "sure", "yep"]
disagreeInput = ["no", "n", "nope"]


def greet() -> str:
    """
    Function to greet differently depending on the time of day
    :return: A color formatted string containing a response
    """
    # Get the current time 
    hour = datetime.datetime.now().hour
    greeting = "Hello, I am Alexis, your personal robot butler"

    # "\033[36m" shows the string in Cyan in the terminal
    # 12am to 11:59am
    if hour >= 0 and hour < 12 :
        greeting = "\033[36m\nGood Morning, I am Alexis, your personal robot butler "

    # 12pm to 5:59pm 
    if hour >= 12 and hour < 18:
        greeting = "\033[36m\nGood Afternoon, I am Alexis, your personal robot butler "

    # 6pm to 11:59pm 
    if hour >= 18 and hour != 0:
        greeting = "\033[36m\nGood Evening, I am Alexis, your personal robot butler "  
    
    return greeting

def upperToCapitalize(txtAct):
    """
    Function that takes a string as an input and if the input string is fully in uppercase, 
    returns a new string lowercased and capitalized. If not returns string unchanged.
    """
    if not txtAct.isupper():
        return txtAct
    txtAct = (txtAct.lower()).capitalize()
    return txtAct

# MAIN LOOP
if __name__ == '__main__':
    # This prints one of the above three greetings before taking user input
    print(greet())

    while not finished:
        while speechRecog:
            with sr.Microphone() as source:

                # Recognisers for speech recognition
                r1 = sr.Recognizer()
                r2 = sr.Recognizer()

                # This will prompt user for speech input in green color and not go to the next line
                print("\n\033[1;32;40mSpeak Command: ", end="")

                # Try to get speech input from user
                try:
                    audio = r1.listen(source)
                    recognised = r2.recognize_google(audio)
                    # Make the speech lowercase for simplicity
                    command = recognised.lower()
                    # Print exactly what user said
                    print(recognised)

                except sr.UnknownValueError:
                    # This will prompt user for text input in green color and not go to the next line
                    print("\n\033[1;32;40mSpeech not recognised to Type Commands, say 'type' or enter it here: ", end="")

                except sr.RequestError as e:
                    # This will prompt user for text input in green color and not go to the next line
                    print("\n\033[1;32;40mSpeech not recognised to Type Commands, say 'type' or enter it here: ", end="")

        # This is the default setting - typing commands
        # This is for when voice commands are disabled
        while not speechRecog:
            # This will prompt user for text input in green color and not go to the next line
            print("\n\033[1;32;40mType Command: ", end="")
            # Take input from user in yellow color
            command = input("\033[33m").lower()

            # ADD POSSIBLE USER COMMANDS HERE
            # GENERAL
            if "hi" in command or "hey" in command or "hello" in command or "hai" in command:
                print(random.choice(resconst.helloResponse))

            elif "how are you" in command or "hows it going" in command or "how's it going" in command or "how r u" in command:
                print(random.choice(resconst.howAreYouResponse))

            elif "whats up" in command or "what's up" in command or "ssup" in command or "what up" in command:
                print(random.choice(resconst.whatsUpResponse))

            elif "who are you" in command or "what are you" in command:
                print("\033[36mI am Alexis, your personal robot butler!")

            # Date and Time
            # Time
            elif "time" in command:
                time_now = datetime.datetime.now()
                current_time = time_now.strftime("%H:%M")
                print("\033[36mIt's currently", current_time)

            # Date
            elif "date" in command:
                date_today = date.today()
                date_today = date_today.strftime("%B %d, %Y")
                print("\033[36mIt's", date_today)

            # TicTacToe
            elif "tic tac toe" in command or "x and o" in command or "xo" in command or "x n o" in command \
                    or "x and 0" in command or "tictactoe" in command:
                game_instance = TicTacToe()
                game_instance.start_game()

            # WEB BASED
            # Open sites in browser
            elif "open " in command:
                if "http" in command:
                    webbrowser.open(command[5:])
                else:
                    webbrowser.open("https://" + command[5:])

            # Google search
            elif "google " in command:
                print(random.choice(resconst.agreeResponse))
                webbrowser.open('https://www.google.com/search?q=' + command[7:])
                
            # Amazon search
            elif "amazon " in command:
                print(random.choice(resconst.agreeResponse))
                webbrowser.open('https://www.amazon.com/s?k=' + command[7:])

            # eBay search
            elif "ebay " in command:
                print(random.choice(resconst.agreeResponse))
                webbrowser.open('https://www.ebay.com/sch/i.html?_nkw=' + command[5:])
                
            # Definition of a word
            elif "definition of " in command:
                print(random.choice(resconst.agreeResponse))
                webbrowser.open('https://www.dictionary.com/browse/' + command[14:])    
                
            # Synonym of a word
            elif "synonym of " in command:
                print(random.choice(resconst.agreeResponse))
                webbrowser.open('https://www.thesaurus.com/browse/' + command[11:])  
                
            # Wikipedia
            elif "search " in command:
                try:
                    searchTerm = command[7:]
                    print(wikipedia.summary(searchTerm))
                # If not found on wikipedia, it will do a google search for the command
                except:
                    print("An error occurred")
                    print(f"Googling {command}")
                    webbrowser.open('https://www.google.com/search?q=' + command[7:])

            # Send E-mails
            elif "send mail" in command or "send e-mail" in command or "send email" in command:
                # Outlook/Hotmail
                session = smtplib.SMTP('smtp.live.com', 587)

                session.starttls()
                try:
                    # Get the required details
                    mailID = input("\033[33mEnter your Outlook/Hotmail E-mail address\n").lower()
                    password = getpass.getpass("Enter Password\n")
                    reciepient = input("\033[33mEnter email of reciepient\n").lower()
                    msg = input("\033[33mEnter message\n")

                    # This is required for it to work
                    message = f"\n {msg}"
                    # Login
                    session.login(mailID, password)
                    # SEND
                    session.sendmail(mailID, reciepient, message)
                    session.quit()
                    print("\033[36mSent!")
                except:
                    print(random.choice(resconst.errorResponse))

            # API BASED
            # Bored
            elif "bored" in command:
                try:
                    r = requests.get('https://www.boredapi.com/api/activity').json()
                    activity = r['activity']
                    print("\033[36mTry this:\n" + activity)
                    # If there is a link in the json of the API
                    if (r['link'] != ""):
                        # Check if user wants to open that link
                        open_browser = input("\033[36mLearn more? (Yes/No)\n").lower()
                        if open_browser in agreeInput:
                            webbrowser.open(r['link'])
                # In case of an error
                except:
                    print(random.choice(resconst.errorResponse))

            # Jokes
            elif "joke" in command:
                # Try getting joke
                try:
                    r = requests.get('https://sv443.net/jokeapi/v2/joke/Miscellaneous,Pun,Spooky,Christmas?blacklistFlags=nsfw,racist,sexist&type=single').json()
                    activity = r['joke']
                    print("\033[34m" + activity)
                    askForInput = True
                    while askForInput == True:
                        # If user wants another joke
                        anotherOne = input("\033[36mAnother one?(Yes/No)\n").lower()
                        # Repeat same to display another joke
                        if anotherOne in agreeInput:
                            r = requests.get('https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,racist,sexist&type=single').json()
                            activity = r['joke']
                            print("\033[34m" + activity)
                            askForInput = True
                        else:
                            askForInput = False

                # In case of an error
                except:
                    print(random.choice(resconst.errorResponse))

            # Show 
            elif "show" in command:
                try:
                    obj = command[5:]
                    if obj == 'dog':
                        print(random.choice(resconst.agreeResponse))
                        r = requests.get('https://dog.ceo/api/breeds/image/random').json()
                        picture_url = r['message']
                        webbrowser.open(picture_url)
                    elif obj == 'cat':
                        print(random.choice(resconst.agreeResponse))
                        r = requests.get('https://api.thecatapi.com/v1/images/search').json()
                        picture_url = r[0]['url']
                        webbrowser.open(picture_url)
                    else:
                        print("\033[34m" + "The list available to show is: " + "\033[36m" + "dog, cat")
             
                # In case of an error        
                except:
                    print(random.choice(resconst.errorResponse))
                
            #Facts
            elif "fact" in command:                
                # Try getting a fact
                try:
                    r = requests.get('https://asli-fun-fact-api.herokuapp.com/').json()
                    activity = upperToCapitalize(r['data']['fact'])
                    print("\033[34m" + activity)
                    askForInput = True
                    while askForInput == True:
                        # If user wants another fact
                        anotherOne = input("\033[36mAnother one?(Yes/No)\n").lower()
                        # Repeat same to display another fact
                        if anotherOne in agreeInput:
                            r = requests.get('https://asli-fun-fact-api.herokuapp.com/').json()
                            activity = upperToCapitalize(r['data']['fact'])
                            print("\033[34m" + activity)
                            askForInput = True
                        else:
                            askForInput = False
                    
                # In case of an error
                except:
                    print(random.choice(resconst.errorResponse)) 

            # HELP
            # This will print everything in the file: AllCommands.txt
            elif "help" in command or "all commands" in command or "list command" in command:
                with open('res/AllCommands.txt', 'r') as f:
                    print(f.read())

            # TURN ON SPEECH RECOGNITION
            elif "speak" in command:
                print("Turning on Speech Recognition...")
                # Turn on speech recognition
                speechRecog = True


            # EXIT
            elif "bye" in command or "goodbye" in command or "abort" in command or "exit" in command or "stop" in command:
                print(random.choice(resconst.exitResponse))
                finished = True
                exit()
            # UNRECOGNISED COMMAND
            else:
                print(f"{random.choice(resconst.unrecognisedCommandResponse)}. Type 'help' to see the list of commands")


#  MADE BY:_            _   _____                        _ 
#  \ \    / (_)        (_) |  __ \                      (_)
#   \ \  / / _ _ __ ___ _  | |  | | __ _ ___  __ _ _ __  _ 
#    \ \/ / | | '__/ _ \ | | |  | |/ _` / __|/ _` | '_ \| |
#     \  /  | | | |  __/ | | |__| | (_| \__ \ (_| | | | | |
#      \/   |_|_|  \___| | |_____/ \__,_|___/\__,_|_| |_|_|
#                     _/ |                                 
#                    |__/                                  
