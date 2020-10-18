# TODO add colors in the Q&A's in terminal
import datetime
import random

finished = False


# LISTS
# Responses
helloResponse = ["\033[34mHello to you too!", "\033[34mHey!", "\033[34mHola amigo", "\033[34mGood to see you!"] 
howAreYouResponse = ["\033[34mJust doing my thing!", "\033[34mI am great!", "\033[34mAmazing!", "\033[34mFeeling awesome!"]
        

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


    # Add possible user commands here
    if "hi" in command or "hey" in command or "hello" in command:
        print(random.choice(helloResponse))

    elif "how are you" in command or "hows it going" in command or "how's it going" in command:
        print(random.choice(howAreYouResponse))


    elif "bye" in command:
        print("Goodbye")
        finished = True    

    else:
        print("Sorry, I don't know that one") 