import webbrowser
from time import sleep
import os
from datetime import datetime
from datetime import date
from selenium import webdriver

'''
TODO:
1. Add selenium automation for Spotify
'''


# *** Functions ***
def Thereis(objects):
    for obj in objects:
        if obj in log:
            return True

# Main Function
def Respond():
    if Thereis(["exit", "goodbye", "quit"]):
        exit()

    if Thereis(["cls", "clear"]):
        os.system("cls")

    if Thereis(["who are you", "what is your name", "what should i call you", "info"]):
        print("I am HelpBot! Here to help you with your daily tasks!")

    if Thereis(["what is the time", "current time", "tell me the time"]):
        f = datetime.now().strftime("%H:%M")
        print(f)

    if Thereis(["what is the date", "current date", "tell me the date"]):
        f = date.today()
        print(f)

    # Opening Websites
    if Thereis(["open discord"]):
        URL = "https://discord.com/app"
        webbrowser.open_new_tab(URL)
        sleep(2)
        print("Opening Discord...")

    if Thereis(["open spotify", "play music"]):
        URL = "https://open.spotify.com/"
        webbrowser.open_new_tab(URL)
        sleep(2)
        print("Opening Spotify...")

    if Thereis(["open classroom"]):
        URL = "https://classroom.google.com/"
        webbrowser.open_new_tab(URL)
        sleep(2)
        print("Opening Google Classroom...")

    if Thereis(["open youtube"]):
        URL = "https://www.youtube.com/"
        webbrowser.open_new_tab(URL)
        sleep(2)
        print("Opening Youtube...")

    if Thereis(["open github"]) and "desktop" not in log:
        URL = "https://github.com"
        webbrowser.open_new_tab(URL)
        sleep(2)
        print("Opening Github...")

    # Searching for things
    if Thereis(["search"]):
        search = log.split("search ")[-1]
        URL = f"https://www.bing.com/search?q={search}&cvid=74e79fbb3c5e4870949eab75ccdc0312&pglt=225&FORM=ANNTA1&PC=U531"
        webbrowser.open_new_tab(URL)
        sleep(2)
        print(f"Here is what I found for {search}")

    if Thereis(["search youtube for"]):
        search = log.split("search youtube for")[-1]
        URL = f"https://www.youtube.com/results?search_query={search}"
        webbrowser.open_new_tab(URL)
        sleep(2)
        print(f"Here is what I found for {search} on Youtube")

    # Opening programs
    if Thereis(["open github-desktop"]):
        os.startfile() # Add the appropiate path to file
        sleep(2)
        print("Opening GitHub Desktop...")

    if Thereis(["open bash", "open git-bash"]):
        os.startfile() # Add the appropiate path to file
        sleep(2)
        print("Opening Git Bash...")

    if Thereis(["open edge"]):
        os.startfile() # Add the appropiate path to file
        sleep(2)
        print("Opening Microsoft Edge...")

    if Thereis(["open sublime", "open st3"]):
        os.startfile() # Add the appropiate path to file
        sleep(2)
        print("Opening Sublime Text 3...")

    if Thereis(["open code", "open vscode"]) and 'insiders' not in log:
        os.startfile() # Add the appropiate path to file
        sleep(2)
        print("Opening Visual Studio Code...")

    if Thereis(["open chrome"]):
        os.startfile() # Add the appropiate path to file
        sleep(2)
        print("Opening Google Chrome...")

    if Thereis(["open zoom"]):
        os.startfile("C:\\Users\\Sapna\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
        sleep(2)
        print("Opening Zoom...")

    if Thereis(["open skype"]):
        os.startfile() # Add the appropiate path to file
        sleep(2)
        print("Open Skype...")

    if Thereis(["open code-insiders"]):
        os.startfile() # Add the appropiate path to file
        sleep(2)
        print("Opening Visual Studio Code Insiders...")

    # Opening Office applications
    if Thereis(["open word", "open ms word"]):
        os.startfile() # Add the appropiate path to file
        print("Opening Word 2013...")

    if Thereis(["open access", "open ms access"]):
        os.startfile() # Add the appropiate path to file
        print("Opening Access 2013...")

    if Thereis(["open excel", "open ms excel"]):
        os.startfile() # Add the appropiate path to file
        print("Opening Excel 2013...")

    if Thereis(["open infopath-designer", "open ms infopath-designer"]):
        os.startfile() # Add the appropiate path to file
        print("Opening InfoPath Designer 2013...")

    if Thereis(["open infopath-filler", "open ms infopath-filler"]):
        os.startfile() # Add the appropiate path to file
        print("Opening Infopath Filler 2013...")

    if Thereis(["open onedrive", "open ms onedrive"]):
        os.startfile() # Add the appropiate path to file
        print("Opening OneDrive 2013...")

    if Thereis(["open onenote", "open ms onenote"]):  
        os.startfile() # Add the appropiate path to file
        print("Opening Onenote 2013...")

    if Thereis(["open outlook", "open ms outlook"]):
        os.startfile() # Add the appropiate path to file
        print("Opening OutLook 2013...")

    if Thereis(["open powerpoint", "open ms powerpoint"]):
        os.startfile() # Add the appropiate path to file
        print("Opening Powerpoint 2013...")

    if Thereis(["open publisher", "open ms publisher"]):
        os.startfile() # Add the appropiate path to file
        print("Opening Publisher 2013...")

    # Searching Wikipedia
    if Thereis(["search wiki for"]):
        search = log.split("search wiki for ")[-1]
        URL = f"https://en.wikipedia.org/wiki/{search}"
        webbrowser.open(URL)
        sleep(2)
        print(f"Here is what I found on Wikipedia for {search}...")

    # To perform calculations
    if Thereis(["calculate"]):
        f = log.split("calculate ")[-1]
        print(int(f))

    # Joining Meetings
    if Thereis(["join meeting"]):
        f = log.split("join meeting ")[-1]

        #  You can add your links to meetings here 

    if Thereis(["open docs"]):
        webbrowser.open_new_tab("https://docs.google.com/document/u/0/")
        sleep(2)
        print("Opening Google Docs...")

    if Thereis(["open slides"]):
        webbrowser.open_new_tab("https://docs.google.com/presentation/u/0/")
        sleep(2)
        print("Opening Google Slides...")

    if Thereis(["open sheets"]):
        webbrowser.open_new_tab("https://docs.google.com/spreadsheets/u/0/")
        sleep(2)
        print("Opening Google Sheets...")

    if Thereis(["open forms"]):
        webbrowser.open_new_tab("https://docs.google.com/forms/u/0/")
        sleep(2)
        print("Opening Google Forms...")

    if Thereis(["open drive", "open google drive"]):
        webbrowser.open_new_tab(
            "https://drive.google.com/drive/my-drive?ths=true")
        sleep(2)
        print("Opening Google Drive...")

    if Thereis(["open gmail", "open mail"]):
        webbrowser.open_new_tab(
            "https://mail.google.com/mail/u/0/#inboxhttps://mail.google.com/mail/u/0/#inbox")
        sleep(2)
        print("Opening Gmail...")


print("How can I help you?")
while True:
    log = input("Enter command: ").lower()
    Respond()
    