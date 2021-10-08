import webbrowser
import random
from utils import response_consts as resconst


def open_website(command: str) -> None:
    """
    This function takes a string containing a potential command to perform tab opening
    :param command: Takes in a command in the format "open WEBSITE" where WEBSITE is a shorthand string or full url
    :return: Nothing is returned by the method
    """
    if "youtube" in command or "yt" in command:
        print(random.choice(resconst.agreeResponse))
        webbrowser.open('www.youtube.com')

    elif "gmail" in command:
        print(random.choice(resconst.agreeResponse))
        webbrowser.open('mail.google.com')

    elif "outlook" in command or "hotmail" in command:
        print(random.choice(resconst.agreeResponse))
        webbrowser.open('outlook.live.com')

    elif "github" in command or "gh" in command:
        print(random.choice(resconst.agreeResponse))
        webbrowser.open('www.github.com')

    elif "netflix" in command:
        print(random.choice(resconst.agreeResponse))
        webbrowser.open('www.netflix.com')

    elif "spotify" in command:
        print(random.choice(resconst.agreeResponse))
        webbrowser.open('www.spotify.com')

    elif "amazon" in command:
        print(random.choice(resconst.agreeResponse))
        webbrowser.open('www.amazon.com')

    elif "classroom" in command:
        print(random.choice(resconst.agreeResponse))
        webbrowser.open('www.classroom.google.com')

    elif "temp mail" in command or "fake email" in command or " temporary mail" in command or "tempmail" in command or "tempmail" in command or "tmpmail" in command or "tmpmail" in command:
        print(random.choice(resconst.agreeResponse))
        webbrowser.open('www.temp-mail.org/en/')

    elif "google" in command:
        print(random.choice(resconst.agreeResponse))
        webbrowser.open('www.google.com')

    elif "twitter" in command:
        print(random.choice(resconst.agreeResponse))
        webbrowser.open('www.twitter.com')
     
    elif "instagram" in command:
        print(random.choice(resconst.agreeResponse))
        webbrowser.open('www.instagram.com')

    # This is to open websites that are not in the list
    else:
        if "www." in command or ".com" in command or ".in" in command or ".co" in command:
            # It will open the url when command is: open {www.URL.com/co/in/etc}
            webbrowser.open(command[5:])
        else:
            print("This is not on our website list")
            print("You can type 'open' followed by the url")
