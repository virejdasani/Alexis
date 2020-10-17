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

    # 12am to 11:59am
    if hour >= 0 and hour < 12 :
        greeting = "Good Moning, "

    # 12pm to 5:59pm 
    if hour >= 12 and hour < 18:
        greeting = "Good Afternoon, "

    # 6pm to 11:59pm 
    if hour >= 18  and hour != 0:
        greeting = "Good Evening, "  
    
    return greeting

print(greet())    

# MAIN LOOP
while finished == False:

        


    # Take input from user    
    command = input("Enter Command: ").lower()


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