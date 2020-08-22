import os
import numpy as np
import time, pyfiglet, pyjokes, pyautogui
import pyttsx3, wikipedia, requests
from googlesearch  import search
import speech_recognition as sr
import start1 , browsers, editors, games, cv2
from bs4 import BeautifulSoup as BS
import searching

def commands():
    while True:
        os.system("color 17")
        os.system("cls")
        print()
        print('''
     ==============================================================================================================
    |    [1]    BROWSERS                                                                                           |
    |==============================================================================================================|        |    [2]    PLAY MOVIES                                                                                        |
    |==============================================================================================================|
    |    [3]    EDITORS                                                                                            |
    |==============================================================================================================|
    |    [4]    SYSTEM INFO                                                                                        |
    |==============================================================================================================|
    |    [5]    IP ADDRESS                                                                                         |
    |==============================================================================================================|
    |    [6]    GAMES                                                                                              |
    |==============================================================================================================|
    |    [7]    CAMERA                                                                                             |
    |==============================================================================================================|
    |    [8]    SEARCH WITH COMMAND LINE                                                                           |
    |==============================================================================================================|
    |    [9]    WIKIPEDIA SUMMARY                                                                                  |
    |==============================================================================================================|
    |    [10]   TREE                                                                                               |
    |==============================================================================================================|
    |    [11]   COVID19 UPDATES                                                                                    |
    |==============================================================================================================|
    |    [12]   JOKES                                                                                              |
    |==============================================================================================================|
    |    [13]   SCREENSHOT                                                                                         |
    |==============================================================================================================|
    |    [14]   ATTRIB                                                                                             |
    |==============================================================================================================|
    |    [15]   PING                                                                                               |
    |==============================================================================================================|
    |    [16]   NETWORK PORTS                                                                                      |
    |==============================================================================================================|
    |    [18]   SEARCH WITH BROWSER                                                                                |
    |==============================================================================================================|        |    [19]   PYTHON                                                                                             |
     ==============================================================================================================
            ''')
            
        print("=="*60 , end=" ")   
        time.sleep(1)
        pyttsx3.speak("which option you want to choose ?")
        a = input("TELL ME SOMETHING: ")
    
        if (("open" in a) or ("start" in a)) and (("browser" in a) or ("browsers" in a)):
            start1.next("color cb")
            browsers.browsers()
        
        elif (("play" in a) or ("start" in a) or ("open" in a)) and (("movie" in a) or ("Race2" in a)):
            os.chdir("C:/Users/milind verma/Downloads/Race2/")
            os.system("Race2.mp4")
            input("\nPRESS ENTER TO CONTINUE....")
        
        elif ((("open" in a) or ("show" in a)) and ("editors" in a)):
            start1.next("color 95")
            editors.editors()
        
        elif ((("open" in a) or ("show" in a)) and ("system" in a)):
            os.system("msinfo32")
            input("\nPRESS ENTER TO CONTINUE....")
        
        elif ((("open" in a) or ("search" in a)) and ("url" in a)):
            count = 0
            try :
                from googlesearch import search
            except ImportError:
                print("No Module named 'google' Found")
            for i in search(query=a,tld='co.in',lang='en',num=10,stop=10,pause=2):
                count += 1
                print(i + '\n')
            input("\nPRESS ENTER TO CONTINUE....")
        
        elif("camera" in a):
            os.system("start microsoft.windows.camera:")
            input("\nPRESS ENTER TO CONTINUE....")
        
        elif ("about" in a):
            query = a
            result = wikipedia.summary(a, sentences=10)
            print(result)
            input("\nPRESS ENTER TO CONTINUE....")

        elif ((("open" in a) or ("show" in a)) and ("ip" in a)):
            os.system("ipconfig")
            input("\nPRESS ENTER TO CONTINUE....")

        elif ((("open" in a) or ("start" in a)) and ("games" in a)):
            start1.next("color 30")
            games.games()
        
        elif ((("open" in a) or ("show" in a)) and ("tree" in a)):
            os.system("tree")
            input("\nPRESS ENTER TO CONTINUE....")
        
        elif ((("open" in a) or ("show" in a)) and ("attribute" in a)):
            os.system("attrib")
            input("\nPRESS ENTER TO CONTINUE....")
        
        elif ((("open" in a) or ("show" in a)) and  (("ports" in a) or ("port"  in a))):
            os.system("netstat")    
            input("\nPRESS ENTER TO CONTINUE....")

        elif (("open" in a) or ("searching" in a)) and (("browser" in a) or ("webbrowser" in a) or ("browsers" in a)):
            start1.next("color f5")
            searching.searching()
        
        elif (("ping" in a)):
            os.system("ping")
            input("\nPRESS ENTER TO CONTINUE....")
        
        elif ("covid" in a):
            def get_info(url):
                data = requests.get(url)
                soup = BS(data.text,'html.parser')
                total = soup.find("div",class_ = "maincounter-number").text
                total = total[1: len(total) - 2]
                other = soup.find_all("span",class_ ="number-table")
                recovered = other[2].text
                deaths = other[3].text
                deaths = deaths[1:]
                ans = {'Total Cases': total, 'Recovered Cases': recovered, 'Total Deaths': deaths}
                return ans
            url = "https://www.worldometers.info/coronavirus/"
            ans = get_info(url)
            for i,j in ans.items():
                print(i + " : " + j)
            input("\nPRESS ENTER TO CONTINUE....")
        
        elif (("joke" in a)):
            print(pyjokes.get_joke())
            input("\nPRESS ENTER TO CONTINUE....")
        
        elif (("screenshot" in a)):
            image = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
            cv2.imwrite("mmmmm.png", image)
            input("\nPRESS ENTER TO CONTINUE....")

        elif (("python" in a)):
            os.system("python")
            input("\nPRESS ENTER TO CONTINUE....")
        
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
            
            commands()