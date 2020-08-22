import pyfiglet, os, time, pyttsx3
from pygame import mixer
from tqdm import tqdm
import start1
def start():
    os.system("cls")
    print("\n\n\n\t\t         @@@@@@@   @@@  @@@    @@@@@@    @@@@@@@             @@@  @@@   @@@@@@@")
    time.sleep(0.1)
    os.system("color 6")
    print("\t\t        @@@@@@@@   @@@  @@@   @@@@@@@@   @@@@@@@             @@@  @@@   @@@@@@@@")
    time.sleep(0.1)
    os.system("color 7")
    print("\t\t        !@@        @@!  @@@   @@!  @@@     @@!               @@!  @@@   @@!  @@@")
    time.sleep(0.1)
    os.system("color b")
    print("\t\t        !@!        !@!  @!@   !@!  @!@     !@!               !@!  @!@   !@!  @!@")
    time.sleep(0.1)
    os.system("color 9")
    print("\t\t        !@!        @!@!@!@!   @!@!@!@!     @!!    @!@!@!@!@  @!@  !@!   @!@  !@!")
    time.sleep(0.1)
    os.system("color a")
    print("\t\t        !!!        !!!@!!!!   !!!@!!!!     !!!    !!!@!@!!!  !@!  !!!   !@!  !!!")
    time.sleep(0.1)
    os.system("color e")
    print("\t\t        :!!        !!:  !!!   !!:  !!!     !!:               :!:  !!:   !!:  !!!")
    time.sleep(0.1)
    os.system("color 5")
    print("\t\t        :!:        :!:  !:!   :!:  !:!     :!:                ::!!:!    :!:  !:!")
    time.sleep(0.1)
    os.system("color f")
    print("\t\t         ::: :::   ::   :::   ::   :::      ::                 ::::      :::: ::")
    time.sleep(0.1)
    os.system("color 6")
    print("\t\t         :: :: :    :   : :    :   : :      :                   :       :: :  :\n\n\n")
    os.system("color a")    
    back_song()
    time.sleep(0.08)

def back_song():
    mixer.init()
    mixer.music.load("song.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()
    time.sleep(5)   
    mixer.music.pause()

def loading():
    print("\n\n")
    for i in tqdm (range(101),
                desc="\t\t\tLoading",
                ascii=False,
                ncols=75):
        time.sleep(0.02)
    
def sad():
    print("=="*60, end="")
    print('''\n\n
                                   _
                                  | |
                                  | | _  _    __   __   ,_    ,_    _   __ _|_
                               _  |/ / |/ |  /    /  \_/  |  /  |  |/  /    |
                                \_/\/  |  |_/\___/\__/    |_/   |_/|__/\___/|_/
                        ''')
def happy():
    print("=="*60,end="")
    print('''\n\n
                                            
                                                     _          _       _
                    ()                              | |        | |   \_|_)            o
                    /\         __   __   _   ,   ,  | |        | |     |     __   __,     _  _
                   /  \|   |  /    /    |/  / \_/ \_|/  |   |  |/     _|    /  \_/  | |  / |/ |
                  /(__/ \_/|_/\___/\___/|__/ \/  \/ |__/ \_/|_/|__/  (/\___/\__/ \_/|/|_/  |  |_/
                                                    |\                             /|
                                                    |/                             \|

                        ''')

if __name__ =='__main__': 
    start()
    i=0
    while i < 2:
        start1.start1()
        i+=1
    else:
        pyttsx3.speak("you have tried maximum chances")
        os.system("exit")
    