import os
import time
import pyttsx3, pyfiglet
import command

def games():
    os.system("color 30")    
    print('''
                                              ___   _   __  __ ___ ___
                                            / __| /_\ |  \/  | __/ __|
                                           | (_ |/ _ \| |\/| | _|\__ \\\

                                            \___/_/ \_\_|  |_|___|___/''')
    print("=="*60 , end="")
    pyttsx3.speak("hey harry . WELCOME TO THE GAMES MENU")
    
    while True:
        os.system("color 30")
        os.system("cls")
        print('''
     ==============================================================================================================
    |    [1]    NFS RIVALS                                                                                         |
    |==============================================================================================================|
    |    [2]    NFS MOST WANTED 2                                                                                  |
    |==============================================================================================================|
    |    [3]    NFS THE RUN                                                                                        |
    |==============================================================================================================|
    |    [4]    BACK                                                                                               |
     ==============================================================================================================  
                   ''')
    
        print("=="*60 , end="")
        pyttsx3.speak("HERE ARE SOME OF THE games")   
        time.sleep(1)
        pyttsx3.speak("harry , WHICH game you want to play")
        a = input("TELL ME SOMETHING: ")
        
        if (("open" in a) or ("start" in a) or ("play" in a)):
            pyttsx3.speak("WELCOME TO NFS RIVALS")
            os.chdir("C:/Program Files (x86)/EA Games/Need for Speed(TM) Rivals/")
            os.system("NFS14.exe")

            
        elif (("open" in a) or ("start" in a) or ("play" in a)):
            pyttsx3.speak("WELCOME TO NFS MOST WANTED 2")
            os.chdir("C:/Program Files (x86)/EA Games/Need for Speed(TM) Rivals/")
            os.system("NFS14.exe") 

        elif (("open" in a) or ("start" in a) or ("play" in a)):
            pyttsx3.speak("WELCOME TO NFS THE RUN")
            os.chdir("C:/Program Files (x86)/EA Games/Need for Speed(TM) Rivals/")
            os.system("NFS14.exe")

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