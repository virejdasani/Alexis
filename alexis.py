# Alexis - YOUR PERSONAL ROBOT BUTLER
'''
RULES
'''
# \033[36m (Blue) for all responses
# \033[1;32;40m (Green) for 'Enter Command: ' phrase

# KEYWORDS:
# "open" is reserved to open websites in the browser
# "search" is for wikipedia
# "google" is to google search


import datetime
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



finished = False
speechRecog = False


# LISTS
# Responses
helloResponse = ["\033[36mHello to you too!", "\033[36mHey!", "\033[36mHola amigo", "\033[36mGood to see you!"] 
howAreYouResponse = ["\033[36mJust doing my thing!", "\033[36mI am great!", "\033[36mAmazing!", "\033[36mFeeling awesome!"]
whatsUpResponse = ["\033[36mThe ceiling, the sky?", "\033[36mNothing much, just robot butler stuff...", "\033[36mJust personal assistant stuff..."]
agreeResponse = ["\033[36mSure thing", "\033[36mOkay", "\033[36mFor sure", "\033[36mAlright"]        
unrecognisedCommandResponse = ["\033[36mSorry, I don't know that", "\033[36mI'm not too sure about that one", "\033[36mHmm, I'm not sure I know that yet"]
exitResponse = ["\033[36mGoodbye", "\033[36mBye Bye!", "\033[36mSee you soon", "\033[36mCatch you later!"]
errorResponse = ["\033[36mAn error occured", "\033[36mSorry, there was an error", "\033[36mError, try again"]

# Inputs
agreeInput = ["yes", "y", "sure", "yep"]
disagreeInput = ["no", "n", "nope"]

# Function to greet differently depending on the time of day
def greet():

    # Get the current time 
    hour = datetime.datetime.now().hour

    # "\033[36m" shows the string in Cyan in the terminal
    # 12am to 11:59am
    if hour >= 0 and hour < 12 :
        greeting = "\033[36m\nGood Moning, I am Alexis, your personal robot butler "

    # 12pm to 5:59pm 
    if hour >= 12 and hour < 18:
        greeting = "\033[36m\nGood Afternoon, I am Alexis, your personal robot butler "

    # 6pm to 11:59pm 
    if hour >= 18  and hour != 0:
        greeting = "\033[36m\nGood Evening, I am Alexis, your personal robot butler "  
    
    return greeting

# This prints one of the above three greetings before taking user input
print(greet())    

    

# MAIN LOOP
while finished == False:

    while speechRecog == True:
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
                print (recognised)

            except sr.UnknownValueError:
                # This will prompt user for text input in green color and not go to the next line
                print("\n\033[1;32;40mSpeech not recognised to Type Commands, say 'type' or enter it here: ", end="")
                

            except sr.RequestError as e:
                # This will prompt user for text input in green color and not go to the next line
                print("\n\033[1;32;40mSpeech not recognised to Type Commands, say 'type' or enter it here: ", end="")

    # This is the default setting - typing commands
    # This is for when voice commands are disabled 
    while speechRecog == False:
        # This will prompt user for text input in green color and not go to the next line
        print("\n\033[1;32;40mType Command: ", end="")
        # Take input from user in yellow color   
        command = input("\033[33m").lower()



# ADD POSSIBLE USER COMMANDS HERE
    # GENERAL
        if "hi" in command or "hey" in command or "hello" in command or "hai" in command:
            print(random.choice(helloResponse))

        elif "how are you" in command or "hows it going" in command or "how's it going" in command or "how r u" in command:
            print(random.choice(howAreYouResponse)) 

        elif "whats up" in command or "what's up" in command or "ssup" in command or "what up" in command:
            print(random.choice(whatsUpResponse)) 
                

        elif "who are you" in command or "what are you" in command:
            print("\033[36mI am Alexis, your personal robot butler!") 

    # TicTacToe
        elif "tic tac toe" in command or "x and o" in command or "xo" in command or "x n o" in command or "x and 0" in command:
            # Execute the res/tictactoe.py file
            from res import tictactoe

    # WEB BASED
        # Open sites in browser
        elif "open " in command:
            if "youtube" in command or "yt" in command:
                print(random.choice(agreeResponse))
                webbrowser.open('www.youtube.com')
            
            elif "gmail" in command:
                print(random.choice(agreeResponse))
                webbrowser.open('mail.google.com')    

            elif "outlook" in command or "hotmail" in command:
                print(random.choice(agreeResponse))
                webbrowser.open('outlook.live.com')
                
            elif "github" in command or "gh" in command:
                print(random.choice(agreeResponse))
                webbrowser.open('www.github.com')    
                
            elif "netflix" in command:
                print(random.choice(agreeResponse))
                webbrowser.open('www.netflix.com')    

            elif "spotify" in command:
                print(random.choice(agreeResponse))
                webbrowser.open('www.spotify.com')

            elif "amazon" in command:
                print(random.choice(agreeResponse))
                webbrowser.open('www.amazon.com')

            elif "classroom" in command:
                print(random.choice(agreeResponse))
                webbrowser.open('www.classroom.google.com')

            elif "temp mail" in command or "fake email" in command or " temporary mail" in command or "tempmail" in command or "tempmail" in command or "tmpmail" in command or "tmpmail" in command:
                print(random.choice(agreeResponse))
                webbrowser.open('www.temp-mail.org/en/')

            elif "google" in command:
                print(random.choice(agreeResponse))
                webbrowser.open('www.google.com')                

            # This is to open websites that are not in the list
            else:
                if "www." in command or ".com" in command or ".in" in command or ".co" in command:
                    # It will open the url when command is: open {www.URL.com/co/in/etc}
                    webbrowser.open(command[5:])
                else:
                    print("This is not on our website list")
                    print("You can type 'open' followed by the url")

        # Google search
        elif "google " in command:
            print(random.choice(agreeResponse))
            webbrowser.open('https://www.google.com/search?q=' + command[7:])


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
                print(random.choice(errorResponse))
                    
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
                print(random.choice(errorResponse))

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
                print(random.choice(errorResponse))

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
            print(random.choice(exitResponse))
            finished = True    
            exit()
    # UNRECOGNISED COMMAND
        else:
            print(f"{random.choice(unrecognisedCommandResponse)}. Type 'help' to see the list of commands") 


#  MADE BY:_            _   _____                        _ 
#  \ \    / (_)        (_) |  __ \                      (_)
#   \ \  / / _ _ __ ___ _  | |  | | __ _ ___  __ _ _ __  _ 
#    \ \/ / | | '__/ _ \ | | |  | |/ _` / __|/ _` | '_ \| |
#     \  /  | | | |  __/ | | |__| | (_| \__ \ (_| | | | | |
#      \/   |_|_|  \___| | |_____/ \__,_|___/\__,_|_| |_|_|
#                     _/ |                                 
#                    |__/                                  
