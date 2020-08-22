import os
import time
import pyttsx3, pyfiglet
import command

def browsers():
    os.system("color cb")   
    print('''                                     ___ ___  _____      _____ ___ ___  ___
                                    | _ ) _ \/ _ \ \    / / __| __| _ \/ __|
                                    | _ \   / (_) \ \/\/ /\__ \ _||   /\__ \\\
                                    
                                    |___/_|_\\\___/ \_/\_/ |___/___|_|_\|___/
                                    ''')
    print("=="*60 , end="")
    pyttsx3.speak("hey harry . WELCOME TO THE BROWSERS MENU")
    time.sleep(1)
    pyttsx3.speak("HERE ARE SOME OF THE BROWSERS")
    while True:
        os.system("color cb")
        os.system("cls")
        print('''
     ==============================================================================================================
    |    [1]    GOOGLE CHROME                                                                                      |
    |==============================================================================================================|
    |    [2]    MOZILLA FIREFOX                                                                                    |
    |==============================================================================================================|
    |    [3]    MICROSOFT EDGE                                                                                     |
    |==============================================================================================================|
    |    [4]    BACK                                                                                               |
     ==============================================================================================================  
                   ''')
    
        print("=="*60 , end="")   
        pyttsx3.speak("WHICH BROWSER SHOULD I OPEN")
        a = input("TELL ME SOMETHING: ")
        
        if ((("open" in a) or ("start" in a)) and ("chrome" in a)):
            pyttsx3.speak("CHROME SUCCESSFULLY OPENED")
            os.system("chrome")
            
        elif ((("open" in a) or ("start" in a)) and ("firefox" in a)):
            pyttsx3.speak("FIREFOX SUCCESSFULLY OPENED")
            os.system("firefox")
            time.sleep(1)
        
        elif ((("open" in a) or ("start" in a)) and (("edge" in a) or ("msedge" in a))):
            pyttsx3.speak("MICROSOFT EDGE SUCCESSFULLY OPENED")
            os.system("msedge")
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
