# TODO add colors in the Q&A's in terminal
import datetime
import random

finished = False


# Lists
helloResponse = ["Hello to you too!", "Hey!", "Hola amigo", "Good to see you!"] 
howAreYouResponse = ["Just doing my thing!", "I am great!", "Amazing!", "Feeling awesome!"]


# Function to greet differently depending on the time of day
def greet():

    # Get the current time 
    hour = datetime.datetime.now().hour

    # "\033[1;32;40m" shows the string in green in the terminal
    # 12am to 11:59am
    if hour >= 0 and hour < 12 :
        greeting = "\033[1;32;40m\nGood Moning, "

    # 12pm to 5:59pm 
    if hour >= 12 and hour < 18:
        greeting = "\033[1;32;40m\nGood Afternoon, "

    # 6pm to 11:59pm 
    if hour >= 18  and hour != 0:
        greeting = "\033[1;32;40m\nGood Evening, "  
    
    return greeting

# This prints one of the above three greetings before taking user input
print(greet())    

# MAIN LOOP
while finished == False:

    # This will prompt user for input in green color 
    print("\033[1;32;40m\nEnter Command: ")
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