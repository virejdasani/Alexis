# Alexis - YOUR PERSONAL ROBOT BUTLER
import datetime
from datetime import date
import random
import webbrowser
import wikipedia
import speech_recognition as sr
import pytube
import random
from html import unescape

# For request errors
import requests
# For email
import smtplib
# For system stats
import psutil
# For getting password anonymously
import getpass
# For translator
from googletrans import Translator, LANGUAGES

from utils import response_consts as resconst
from utils.tictactoe import TicTacToe
from utils.rock_paper_scissors import RockPaperScissors
from utils.connect_four import ConnectFour
#For currency
from forex_python.converter import CurrencyRates

import pytz


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

# Variable to store the last displayed quote
last_quote = {"text": "", "author": ""}


# Inputs
agreeInput = ["yes", "y", "sure", "yep", "ok", "why not"]
disagreeInput = ["no", "n", "nope", "rather not"]


def greet() -> str:
    """
    Function to greet differently depending on the time of day
    :return: A color formatted string containing a response
    """
    # Get the current time 
    hour = datetime.datetime.now().hour
    greeting = "\033[36m\nHello, I am Alexis, your personal robot butler"

    # "\033[36m" shows the string in Cyan in the terminal
    # 12am to 11:59am
    if hour >= 0 and hour < 12 :
        greeting = "\033[36m\nGood Morning, I am Alexis, your personal robot butler"

    # 12pm to 5:59pm 
    if hour >= 12 and hour < 18:
        greeting = "\033[36m\nGood Afternoon, I am Alexis, your personal robot butler"

    # 6pm to 11:59pm 
    if hour >= 18 and hour != 0:
        greeting = "\033[36m\nGood Evening, I am Alexis, your personal robot butler"  
    
    return greeting

# This function  takes a string as an input and if the input string is fully in uppercase, 
# returns a new string lowercased and capitalized. If not returns string unchanged.
def upperToCapitalize(txtAct):
    if not txtAct.isupper():
        return txtAct
    txtAct = (txtAct.lower()).capitalize()
    return txtAct

def obtain_aliases(file = "res/aliases.txt") -> str:
    """
    This function returns every saved command alias.
    Args:
        file (str, optional): The file where the aliases are stored. Defaults to "res/aliases.txt".

    Returns:
        list:dict:str A list of dictionaries where the keys are the aliases and the valus ar the command that the alias points to.
    """
    with open(file, "r") as f:
        lines = f.readlines()
    returnDictionnary = {}
    for line in lines:
        returnDictionnary[line.split("=")[0]] = line.split("=")[1]
    return returnDictionnary

def save_aliases(aliases, file = "res/aliases.txt") -> str:
    """
    This subroutine saves command aliases.
    Args:
        aliases (list of dictionnaries): the aliases to be stored
        file (str, optional): The file where the aliases are to be stored. Defaults to "res/aliases.txt".
    """
    with open(file, "w") as f:
        for k, v in aliases.items():
            f.write(f"{k}={v}")

def apply_aliases(command, file = "res/aliases.txt") -> str:
    """
    This function returns the command passed as an argument with all aliases apllied
    Args:
        command (str): The user command to aplly aliases to.
        file (str, optional): The file in which the alliases are stored. Defaults to "res/aliases.txt".
    Returns:
        str: The command with all aliasess apllied
    """
    aliases = obtain_aliases()
    for k, v in aliases.items():
        command = command.replace(k, v)
    return command 

def get_setting(setting: str, file = "res/settings.txt") -> str:
    """
    This function obtains a specific setting's value from the specified file.
    Args:
        setting (str): The seting you are looking for the value of.
        file (str, optional): Settings file to consult (relative filepath as string required). Defaults to "res/setings.txt".

    Returns:
        str: The value of the queried setting.
    """
    with open(file, "r") as f:
        settings = f.readlines()
    for line in settings:
        if line.split("=")[0] == setting.upper():
            return line.split("=")[1].strip("\n")
    return None

def set_background_color(settingsFile = "res/settings.txt") -> str:
    backgroundColor = "\033[1;32;40m"
    colorMode = get_setting("COLORMODE", settingsFile)
    if colorMode == "dark":
        backgroundColor = "\033[1;32;40m"
    elif colorMode == "light":
        backgroundColor = "\033[1;32;255m"
    elif colorMode == "purple":
        backgroundColor = "\033[1;32;45m"
    elif colorMode == "red":
        backgroundColor = "\033[1;32;41m"
    elif colorMode == "green":
        backgroundColor = "\033[1;32;42m"
    elif colorMode == "blue":
        backgroundColor = "\033[1;32;44m"
    return backgroundColor

def execute_user_macro(macroNameAndArgs: str, file = "res/macros.txt"):
    """
    This function executes a user-written macro as specified in the passed file.
    Args:
        macroName (str): The name of the macro to execute.
        file (str, optional): The location of the macros file. Defaults to "res/macros.txt".

    Returns:
        any: The macro's return value if applicable or a string error message
    """
    macroName = macroNameAndArgs[0]
    arguments = macroNameAndArgs[1:]
    with open(file, "r") as f:
        text = f.read().split("</MACRO>")
    macros = {}
    # This large for loop tries to read the macros.txt file into macro names and arguments and macro code in a single dictionnary.
    for code in text:
        currentMacroName =""
        currentMacroContent = ""
        nameObtained = False
        for char in code:
            if char == ">":
                nameObtained = True
            elif char != "<" and not nameObtained:
                currentMacroName += char
            elif char != "<":
                currentMacroContent += char
        macroHeaders = currentMacroName.strip("\n").split(" ")
        macros[macroHeaders[0].lower()] = currentMacroContent.strip("\n"), macroHeaders[1:]
    if macroName in macros.keys():
        # This is the part that handles passing the arguments to the macro.
        macroArgs = {}
        for argumentIndex in range(len(arguments)):
            macroArgs[macros[macroName][1][argumentIndex]] = arguments[argumentIndex]
        return exec(macros[macroName][0], macroArgs)
    else:
        return "Sorry, I don't seem to remember what this macro is."

# Function to perform language translation
def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Function to print available languages
def print_available_languages():
    print("\033[36mAvailable Languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")

news_api_key = '102ebf59c0124b54a9c2e239549bf2a3'

def get_latest_news(api_key, country='us', category='general'):
   base_url = "https://newsapi.org/v2/top-headlines"
   params = {
       'country': country,
       'category': category,
       'apiKey': api_key
   }
   response = requests.get(base_url, params=params)
   if response.status_code == 200:
       articles = response.json()['articles']
       return articles[:5]  # Return top 5 news articles
   else:
       return f"Error: {response.status_code}"

def get_random_quote():
    """
    Function to fetch a random quote from ZenQuotes API
    :return: A dictionary containing quote text and author, or None if error
    """
    try:
        response = requests.get('https://zenquotes.io/api/random')
        if response.status_code == 200:
            data = response.json()
            # ZenQuotes returns a list with one quote object
            if isinstance(data, list) and len(data) > 0:
                return {"text": data[0]['q'], "author": data[0]['a']}
            else:
                return None
        else:
            return None
    except:
        return None

def save_quote_to_file(quote_text, quote_author, file="res/favorite_quotes.txt"):
    """
    Function to save a quote to the favorite quotes file
    :param quote_text: The text of the quote
    :param quote_author: The author of the quote
    :param file: The file path to save to
    """
    try:
        with open(file, "a") as f:
            f.write(f"{quote_text}|{quote_author}\n")
        return True
    except:
        return False

def get_saved_quotes(file="res/favorite_quotes.txt"):
    """
    Function to retrieve all saved quotes from file
    :param file: The file path to read from
    :return: A list of dictionaries containing quote text and author
    """
    try:
        with open(file, "r") as f:
            lines = f.readlines()
        quotes = []
        for line in lines:
            if "|" in line:
                parts = line.strip().split("|")
                quotes.append({"text": parts[0], "author": parts[1]})
        return quotes
    except FileNotFoundError:
        # File doesn't exist yet
        return []
    except:
        return []

def delete_quote_from_file(quote_number, file="res/favorite_quotes.txt"):
    """
    Function to delete a quote from the favorite quotes file
    :param quote_number: The number of the quote to delete (1-indexed)
    :param file: The file path
    :return: True if successful, False otherwise
    """
    try:
        quotes = get_saved_quotes(file)
        if quote_number < 1 or quote_number > len(quotes):
            return False

        # Remove the quote at the specified index
        quotes.pop(quote_number - 1)

        # Rewrite the file
        with open(file, "w") as f:
            for quote in quotes:
                f.write(f"{quote['text']}|{quote['author']}\n")
        return True
    except:
        return False


# MAIN LOOP
if __name__ == '__main__':
    # This prints one of the above three greetings before taking user input
    print(greet())
    backgroundColor = set_background_color()
    while not finished:
        while speechRecog:
            with sr.Microphone() as source:
                # Recognisers for speech recognition
                r1 = sr.Recognizer()
                r2 = sr.Recognizer()

                # This will prompt user for speech input in green color and not go to the next line
                print(f"\n{backgroundColor}Speak Command: ", end="")

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
                    print(f"\n{backgroundColor}Speech not recognised to Type Commands, say 'type' or enter it here: ", end="")

                except sr.RequestError as e:
                    # This will prompt user for text input in green color and not go to the next line
                    print(f"\n{backgroundColor}Speech not recognised to Type Commands, say 'type' or enter it here: ", end="")

        # This is the default setting - typing commands
        # This is for when voice commands are disabled
        while not speechRecog:
            # This will prompt user for text input in green color and not go to the next line
            print(f"\n{backgroundColor}Type Command: ", end="")
            # Take input from user in yellow color
            command = input("\033[33m").lower()
            # Apllies aliases
            command = apply_aliases(command)  
            # ADD POSSIBLE USER COMMANDS HERE
            # GENERAL
            if "dealias" in command or "de-alias" in command:
                aliases = obtain_aliases()
                alias = command.split(" ")[1]
                if alias not in aliases.values():
                    print("\033[36mThis alias does not exist.")
                else:
                    newAliases = {}
                    for k, v in aliases.items():
                        if v == alias:
                            continue
                        else:
                            newAliases[k] = v
                    save_aliases(newAliases)
                    print("\033[36mAlias removed successfuly.")
            elif "alias" in command:
                aliases = obtain_aliases()
                alias = command.split(" ")[1]
                aliasing_target = command.split(" ")[-1]
                if alias in aliases.keys():
                    print("\033[36mThis word already binds to a command.")
                else:
                    aliases[alias] = aliasing_target
                    save_aliases(aliases)
                    print("\033[36mAlias apllied.")
            
            elif "run" in command:
                returnValue = f"\033[36m{execute_user_macro(command.split(' ')[1:])}"
                if returnValue == "\033[36mNone":
                    print("\033[36mDone with execution.")
                else:
                    print(returnValue)
            
            elif "hi" in command or "hey" in command or "hello" in command or "hai" in command:
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
                format = get_setting("HOUR_FORMAT")
                time_now = datetime.datetime.now()
                if format == "12h":
                    current_time = time_now.strftime("%I:%M %p")
                else:
                    current_time = time_now.strftime("%H:%M")
                print("\033[36mIt's currently", current_time)

            # Date
            elif "date" in command:
                date_today = date.today()
                date_today = date_today.strftime("%B %d, %Y")
                print("\033[36mIt's", date_today)

            # News
            elif "news" in command:
               news = get_latest_news(news_api_key)
               for article in news:
                   print(article['title'], "-", article['description'])


            # System information / vitals
            elif "vitals" in command:
                try:
                    print("Diagnosing system to collect vital stats")

                    # Get CPU usage
                    print(f"The CPU usage is: {psutil.cpu_percent(4)} %") # We get the CPU usage for the past 4 seconds

                    # Get memory usage
                    print(f"RAM memory used: {psutil.virtual_memory()[2]} %")

                    # Get battery percentage
                    battery_status = psutil.sensors_battery()
                    print(f"Percentage of battery: {battery_status.percent} %")
                except:
                    print("An error occurred while collecting system vitals")

            # TicTacToe
            elif "tic tac toe" in command or "x and o" in command or "xo" in command or "x n o" in command \
                    or "x and 0" in command or "tictactoe" in command:
                game_instance = TicTacToe()
                game_instance.start_game()

            # RockPaperScissors
            elif "Rock Paper Scissors" in command or "rock paper scissors" in command or "rockpaperscissors" in command:
                game_instance = RockPaperScissors()
                game_instance.start_game()
            
            # ConnectFour
            elif "Connect Four" in command or "ConnectFour" in command or "connect four" in command or "connectfour" in command:
                game_instance = ConnectFour()
                game_instance.start_game()

            # Download YouTube video
            elif "download youtube video" in command or "download video" in command or "mp4" in command:
                # Ask for YouTube video link
                url = input("\033[33mEnter the URL of the video you want to download: ")
                try:
                    yt = pytube.YouTube(url)
                    ys = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
                    # Ask for the path to save the video
                    path = input("\033[33mEnter the path to save the video: ")
                    # Download the video
                    ys.download(path)
                    print("\033[36mVideo downloaded successfully!")
                except Exception as e:
                    print("\033[36mVideo download failed! Error: ", e)

            # Get YouTube video information
            elif "video stats" in command or "video info" in command or "video information" in command or "video statistics" in command:
                # Ask for YouTube video link
                url = input("\033[33mEnter the URL of the video you want to get information about: ")
                try:

                    yt = pytube.YouTube(url)
                    print("\033[36mTitle:          ", yt.title)
                    print("Views:          ", yt.views)
                    print("Length:         ", yt.length)
                    print("Publish Date:   ", yt.publish_date)
                    print("Author:         ", yt.author)
                    print("Age Restricted: ", yt.age_restricted)
                except Exception as e:
                    print("\033[36mVideo information retrieval failed! Error: ", e)

            # world clock
            elif "world clock" in command:
                dispTimezone = input("Enter the location of time zone in like (Canada/Eastern, Europe/Brussels, Etc/GMT-2): ")
                try: 
                    dispTime = datetime.datetime.now(pytz.timezone(dispTimezone))
                    print(f"current time in {dispTimezone}: {dispTime}")
                except pytz.UnknownTimeZoneError:
                    print("Can't find the place, try checking for typos or extra spaces")

            # WEB BASED
            # Open sites in browser
            elif "open " in command:
                if "http" in command:
                    webbrowser.open(command[5:])
                elif "tempmail" in command:
                    webbrowser.open("https://temp-mail.org/en/")
                elif "youtube" or "yt" in command:
                    webbrowser.open("https://youtube.com")
                elif "spotify" or "song" in command:
                    webbrowser.open("https://spotify.com")
                elif "github" or "gh" in command:
                    webbrowser.open("https://github.com")
                elif "gmail" in command:
                    webbrowser.open("https://mail.google.com/")
                elif "netflix" in command:
                    webbrowser.open("https://netflix.com")
                elif "amazon" in command:
                    webbrowser.open("https://amazon.com")
                elif "google classroom" or "classroom" in command:
                    webbrowser.open("https://edu.google.com/intl/en-GB/workspace-for-education/classroom/")
                elif "twitter" in command or command.endswith("x") or command.endswith("x."):
                    webbrowser.open("https://twitter.com")
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
            
            #Google Map of a Place
            elif "where is " in command:
                print(random.choice(resconst.agreeResponse))
                webbrowser.open('https://www.google.com/maps/search/' + command[9:])
            
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
            # Translator
            elif "translate" in command:
                try:
                    text_to_translate = input("\033[33mEnter the text to be translated: ")
                    target_language_input = input(
                        "\033[33mEnter the target language code or type 'help' to see the list of available languages: ").lower()

                    if target_language_input == "help":
                        print_available_languages()
                    else:
                        target_language = target_language_input
                        translated_text = translate_text(text_to_translate, target_language)
                        print("\033[36mTranslated Text:", translated_text)
                except Exception as e:
                    print("\033[36mTranslation failed! Error: ", e)

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
            
            # Advice
            elif "advice" in command:
                # Try getting a piece of random advice
                # uses Advice Slip API
                try:
                    r = requests.get("https://api.adviceslip.com/advice").json()
                    print (r['slip']['advice'])
                # In case of an error
                except:
                    print(random.choice(resconst.errorResponse))

            # Quote
            elif "quote" in command:
                # Quote save: saves the last displayed quote
                if "save" in command:
                    if last_quote["text"] == "":
                        print("\033[36mNo quote to save. Get a quote first!")
                    else:
                        if save_quote_to_file(last_quote["text"], last_quote["author"]):
                            print("\033[36m✓ Quote saved to your collection!")
                        else:
                            print(random.choice(resconst.errorResponse))

                # Quote list: shows all saved quotes
                elif "list" in command:
                    saved_quotes = get_saved_quotes()
                    if len(saved_quotes) == 0:
                        print("\033[36mYou don't have any saved quotes yet. Use 'quote save' to save a quote!")
                    else:
                        print("\033[36mYour saved quotes:")
                        for i, quote in enumerate(saved_quotes):
                            print(f"\033[36m{i+1}. \"{quote['text']}\" - {quote['author']}")

                # Quote delete: removes a quote from collection
                elif "delete" in command:
                    try:
                        # Extract the quote number from command
                        quote_num = int(command.split()[-1])
                        if delete_quote_from_file(quote_num):
                            print("\033[36m✓ Quote deleted successfully!")
                        else:
                            print("\033[36mInvalid quote number. Use 'quote list' to see all quotes.")
                    except ValueError:
                        print("\033[36mPlease specify a quote number. Example: 'quote delete 1'")
                    except:
                        print(random.choice(resconst.errorResponse))

                # Quote random: shows a random quote from saved collection
                elif "random" in command:
                    saved_quotes = get_saved_quotes()
                    if len(saved_quotes) == 0:
                        print("\033[36mYou don't have any saved quotes yet. Use 'quote save' to save a quote!")
                    else:
                        random_quote = random.choice(saved_quotes)
                        print(f"\033[36m\"{random_quote['text']}\" - {random_quote['author']}")

                # Quote (default): gets a random quote from API
                else:
                    try:
                        quote_data = get_random_quote()
                        if quote_data:
                            # Store the quote for potential saving
                            last_quote["text"] = quote_data["text"]
                            last_quote["author"] = quote_data["author"]
                            # Display the quote
                            print(f"\033[36m\"{quote_data['text']}\" - {quote_data['author']}")
                        else:
                            print(random.choice(resconst.errorResponse))
                    except:
                        print(random.choice(resconst.errorResponse))


            # Trivia
            elif "trivia" in command:
                # Try getting a Trivia question through an API
                try:
                    response = requests.get("https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple")
                    data = response.json()

                    if response.status_code == 200:
                        result = data["results"][0]

                        # Print the questions for the user to see
                        question = unescape(result["question"])
                        print(f"\033[36m{question}")
                        
                        # Print the options in a random order
                        correct_answer =  unescape(result["correct_answer"])
                        # print(correct_answer)
                        options = [unescape(option) for option in result["incorrect_answers"]]
                        options.append(correct_answer)
                        random.shuffle(options)

                        for i, option in enumerate(options):
                            print(f"\033[36m\t({i+1}) {option}")

                        # Request an option from the users
                        my_answer_id = input("\033[33mEnter your answer (A number from 1-4): ")

                        # Check if the answer is valid and correct
                        my_answer_id = int(my_answer_id) # This line of code will fail if they enter an invalid number
                        if my_answer_id not in range(1,5):
                            print("\033[36mEnter a valid number between 1 and 4 next time...")
                        elif correct_answer == options[my_answer_id-1]:
                            print("\033[36mCongratulations, you are correct!!!")
                        else:
                            print(f"\033[36mGood attempt, the correct answer was \"{correct_answer}\". Try again next time")
                        
                    else:
                        print (f'\033[36mError retrieving trivia data')
                    
                except Exception as e:
                    print("\033[36mError in trivia execution!:", e)


            #Weather
            elif "weather" in command:

                # Note: This API key is associated with a free plan and may have usage limitations.
                api_key = '42dd8eece458d27eca3c295e916b6c79' 
                city = input("\033[33mEnter the city for weather information: ")

                try:
                    params = {"q": city, "appid": api_key, "units": "metric"}  
                    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
                    data = response.json()
                    if response.status_code == 200:
                        temperature = data["main"]["temp"]
                        weather_description = data["weather"][0]["description"]
                        print (f'\033[36mWeather in {city}: {weather_description}, Temperature: {temperature}°C')
                    else:
                        print (f'\033[36mError retrieving weather data for {city}')
                
                except:
                    print(random.choice(resconst.errorResponse))
            
            # Stock Price
            elif "stock" in command:
                
                # Ask the user for the stock symbol
                stock_symbol = input("\033[33mEnter the stock symbol (e.g., AAPL): ").upper()

                # Note: This API key is associated with a free plan and may have usage limitations.
                api_key = "GT33YXVN95VQ810P"
                base_url = "https://www.alphavantage.co/query"

                try:
                    # Making a request to the API
                    response = requests.get(f'{base_url}?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={api_key}')
                    data = response.json()

                    # Extracting and printing the stock price
                    stock_info = data.get('Global Quote', {})
                    if stock_info:
                        stock_price = stock_info.get('05. price')
                        print(f'\033[36mCurrent stock price of {stock_symbol}: ${stock_price}')
                    else:
                        print(f'\033[36mStock information not found for {stock_symbol}')

                except Exception as e:
                    print(f'\033[36mError retrieving stock data: {e}')

            #Zip Code
            elif "zip" in command:
                #Get information about a zip code
                try:
                    zip_code = input("Type your zip code:\n")
                    r = requests.get(f'https://api.zippopotam.us/us/{zip_code}').json()
                    activity = r["places"][0]['place name'] + " " + r["places"][0]["state abbreviation"] + " " + r["country"]
                    print("\033[34m" +activity)
                    askForInput = True
                    while askForInput == True:
                        # If user wants to check another zip code
                        anotherOne = input("\033[36mDo you want to check another zip code?(Yes/No)\n").lower()
                        if anotherOne == "yes":
                            zip_code = input("Type your zip code:\n")
                            r = requests.get(f'https://api.zippopotam.us/us/{zip_code}').json()
                            activity = r["places"][0]['place name'] + " " + r["places"][0]["state abbreviation"] + " " + r["country"]
                            print("\033[34m" +activity)
                        else:
                            askForInput = False
                except:
                    print(random.choice(resconst.errorResponse))


            #currency conversion
            elif "convert currency" in command:
                try:
                    # Get the source currency, target currency, and amount from the user
                    source_currency = input("\033[33mEnter the source currency code (e.g., USD): ").upper()
                    target_currency = input("\033[33mEnter the target currency code (e.g., EUR): ").upper()
                    amount = float(input("\033[33mEnter the amount to convert: "))

                    # Perform the currency conversion
                    c = CurrencyRates()
                    exchange_rate = c.get_rate(source_currency, target_currency)
                    converted_amount = amount * exchange_rate

                    # Print the result
                    print(f"\033[36m{amount} {source_currency} is equal to {converted_amount} {target_currency}")
                except Exception as e:
                    print("\033[36mCurrency conversion failed! Error:", e)


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
