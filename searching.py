import os
import time
import pyttsx3
import command
import webbrowser
from googlesearch import search
            
def searching():
    os.system("color f5")
    print("=="*60 , end="")    
    print('''                                     ___                  _      __  __
                                    / __| ___ __ _ _ _ __| |_   |  \/  |___ _ _ _  _
                                    \__ \/ -_) _` | '_/ _| ' \  | |\/| / -_) ' \ || |
                                    |___/\___\__,_|_| \__|_||_| |_|  |_\___|_||_\_,_|
    ''')
    print("=="*60 , end="")
    pyttsx3.speak("hey harry . WELCOME TO THE search MENU")
    time.sleep(1)
    pyttsx3.speak("i have some of the searching borwsers, so which one you want to use")
    while True:
        os.system("color f5")
        os.system("cls")
        print('''
     ==============================================================================================================
    |    [1]    SEARCH WITH GOOGLE                                                                                 |
    |==============================================================================================================|
    |    [2]    SEARCH WITH FIREFOX                                                                                |
    |==============================================================================================================|
    |    [3]    SEARCH WITH MICROSOFT EDGE                                                                         |
    |==============================================================================================================|
    |    [4]    BACK                                                                                               |
     ==============================================================================================================  
                   ''')
        print("=="*60 , end="") 
        time.sleep(1)  
        a = input("YOUR SEARCHING BROWSER: ")
        if ("chrome" in a):
            pyttsx3.speak("WHAT YOU WANT TO SEARCH")
            a = input("TELL SOMETHING: ")
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(a, tld="com", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % a)

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
           

        if (("firefox" in a) or ("mozilla" in a)):
            pyttsx3.speak("WHAT YOU WANT TO SEARCH")
            a = input("TELL SOMETHING: ")
            if ((("open" in a) or ("search" in a)) and ("redhat" in a)):
                os.system("firefox www.redhat.com")      
            elif ((("open" in a) or ("search" in a)) and ("yahoo" in a)):
                os.system("firefox www.yahoo.com")
            elif ((("open" in a) or ("play" in a)) and ("song" in a)):
                os.system("firefox https://www.youtube.com/watch?v=uEJuoEs1UxY")
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
                
        
        if (("edge" in a) or ("msedge" in a)):
            pyttsx3.speak("WHAT YOU WANT TO SEARCH")
            a = input("TELL SOMETHING: ")
            if ((("open" in a) or ("search" in a)) and ("redhat" in a)):
                os.system("msedge www.redhat.com")      
            elif ((("open" in a) or ("search" in a)) and ("yahoo" in a)):
                os.system("msedge www.yahoo.com")
            elif ((("open" in a) or ("play" in a)) or ("song" in a) or ("songs"  in a)):
                os.system("msedge https://www.youtube.com/watch?v=uEJuoEs1UxY")
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
               
                