# RULES
'''
\033[34m (Orange) for all responses
\033[1;32;40m (Green) for 'Enter Command: ' phrase
'''


import datetime
import random
import webbrowser

finished = False


# LISTS
# Responses
helloResponse = ["\033[34mHello to you too!", "\033[34mHey!", "\033[34mHola amigo", "\033[34mGood to see you!"] 
howAreYouResponse = ["\033[34mJust doing my thing!", "\033[34mI am great!", "\033[34mAmazing!", "\033[34mFeeling awesome!"]
agreeResponse = ["\033[34mSure thing", "\033[34mOkay", "\033[34mFor sure", "\033[34mAlright"]        
unrecognisedCommandResponse = ["\033[34mSorry, I don't know that", "\033[34mI'm not too sure about that one", "\033[34mHmm, I'm not sure I know how to do that yet"]

# Function to greet differently depending on the time of day
def greet():

    # Get the current time 
    hour = datetime.datetime.now().hour

    # "\033[34m" shows the string in orange in the terminal
    # 12am to 11:59am
    if hour >= 0 and hour < 12 :
        greeting = "\033[34m\nGood Moning, "

    # 12pm to 5:59pm 
    if hour >= 12 and hour < 18:
        greeting = "\033[34m\nGood Afternoon, "

    # 6pm to 11:59pm 
    if hour >= 18  and hour != 0:
        greeting = "\033[34m\nGood Evening, "  
    
    return greeting

# This prints one of the above three greetings before taking user input
print(greet())    

# MAIN LOOP
while finished == False:

    # This will prompt user for input in green color and not go to the next line
    print("\n\033[1;32;40mEnter Command: ", end="")
    # Take input from user in yellow color   
    command = input("\033[33m").lower()


# ADD POSSIBLE USER COMMANDS HERE
# GENERAL
    if "hi" in command or "hey" in command or "hello" in command:
        print(random.choice(helloResponse))

    elif "how are you" in command or "hows it going" in command or "how's it going" in command:
        print(random.choice(howAreYouResponse))


# WEB BASED
    # Open in browser
    elif "open youtube" in command or "get youtube" in command or "open yt" in command or "get yt" in command:
        print(random.choice(agreeResponse))
        webbrowser.open('www.youtube.com')

    elif "open google" in command or "get google" in command:
        print(random.choice(agreeResponse))
        webbrowser.open('www.google.com')
    
    elif "open gmail" in command or "get gmail" in command:
        print(random.choice(agreeResponse))
        webbrowser.open('www.gmail.com')    

    elif "open github" in command or "get github" in command or "get gh" in command or "open gh" in command:
        print(random.choice(agreeResponse))
        webbrowser.open('www.github.com')    
        

# EXIT
    elif "bye" in command or "goodbye" in command:
        print("Goodbye")
        finished = True    
# UNRECOGNISED
    else:
        print("Sorry, I don't know that one") 