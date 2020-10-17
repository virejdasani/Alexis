import datetime

finished = False


while finished == False:

    def greet():
        # Get the current time 
        hour = datetime.datetime.now().hour
        # Check what part of the 24 hrs it is

        # 12am to 11:59am
        if hour >= 0 and hour < 12 :
            greeting = "Good Moning, \nEnter Command: "

        # 12pm to 5:59pm 
        if hour >= 12 and hour < 18:
            greeting = "Good Afternoon, \nEnter Command: "

        # 6pm to 11:59pm 
        if hour >= 18  and hour < 0:
            greeting = "Good Afternoon, \nEnter Command: "  

        return greeting

            

    # Take input from user    
    command = input(greet()).lower()


    # Add possible user commands here
    if "hi" in command :
        greet()
    elif "bye" in command:
        print("Goodbye")
        finished = True    
    else:
        print("I didn't get that")    