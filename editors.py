import os
import time
import pyttsx3
import command
import speech_recognition as sr
import pyfiglet

def editors():
    os.system("color 95")    
    print('''                                     ___ ___ ___ _____ ___  ___  ___
                                    | __|   \_ _|_   _/ _ \| _ \/ __|
                                    | _|| |) | |  | || (_) |   /\__ \\\

                                    |___|___/___| |_| \___/|_|_\|___/
    ''')
    print("=="*60 , end="")
    pyttsx3.speak("hey harry . WELCOME TO THE EDITORS MENU")
    time.sleep(1)
    pyttsx3.speak("HERE ARE SOME OF THE editors")
    while True:
        os.system("color 95")
        os.system("cls")
        print('''
     ==============================================================================================================
    |    [1]    NOTEPAD                                                                                            |
    |==============================================================================================================|
    |    [2]    NOTEPAD++                                                                                          |
    |==============================================================================================================|
    |    [3]    WORDPAD                                                                                            |
    |==============================================================================================================|
    |    [4]    BACK                                                                                               |
     ==============================================================================================================  
                   ''')
    
        print("=="*60 , end="")   
        pyttsx3.speak("WHICH EDITOR SHOULD I OPEN")
        a = input("TELL ME SOMETHING: ")

        if ((("open" in a) or ("start" in a)) and (("notepad" in a) and ("++" not in a))):
            pyttsx3.speak("NOTEPAD SUCCESSFULLY OPENED")
            os.system("notepad")      
        elif ((("open" in a) or ("start" in a)) and (("notepad" in a) and ("++" in a))):
            pyttsx3.speak("NOTEPAD PLUS PLUS SUCCESSFULLY OPENED")
            os.system("notepad++")
        elif ((("open" in a) or ("start" in a)) and ("wordpad" in a)):
            pyttsx3.speak("WORDPRESS SUCCESSFULLY OPENED")
            os.system("wordpad")
            
        elif(("previous" in a) or ("return" in a) or ("back" in a)):
            os.system("cls")
            command.commands()
        else:
            print('''
                                   
                                M""MMM""MMM""M
                                M  MMM  MMM  M
                                M  MMP  MMP  M 88d888b. .d8888b. 88d888b. .d8888b.
                                M  MM'  MM' .M 88'  `88 88'  `88 88'  `88 88'  `88
                                M  `' . '' .MM 88       88.  .88 88    88 88.  .88
                                M    .d  .dMMM dP       `88888P' dP    dP `8888P88
                                MMMMMMMMMMMMMM                                 .88
                                                                        d8888P
                                MP""""""`MM                                     dP
                                M  mmmmm..M                                     88
                                M.      `YM .d8888b. .d8888b. 88d888b. .d8888b. 88d888b.
                                MMMMMMM.  M 88ooood8 88'  `88 88'  `88 88'  `"" 88'  `88
                                M. .MMM'  M 88.  ... 88.  .88 88       88.  ... 88    88
                                Mb.     .dM `88888P' `88888P8 dP       `88888P' dP    dP
                                MMMMMMMMMMM

                        ''')
            pyttsx3.speak("YOU HAVE SEARCHED SOMETHING IRRELEVANT")
            