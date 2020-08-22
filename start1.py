import os, time, pyfiglet
import main
import pyttsx3
import command, getpass
def start1():
    os.system("cls")
    print("\n\n\n\t\t         @@@@@@@   @@@  @@@    @@@@@@    @@@@@@@             @@@  @@@   @@@@@@@")
    print("\t\t        @@@@@@@@   @@@  @@@   @@@@@@@@   @@@@@@@             @@@  @@@   @@@@@@@@")
    print("\t\t        !@@        @@!  @@@   @@!  @@@     @@!               @@!  @@@   @@!  @@@")
    print("\t\t        !@!        !@!  @!@   !@!  @!@     !@!               !@!  @!@   !@!  @!@")
    print("\t\t        !@!        @!@!@!@!   @!@!@!@!     @!!    @!@!@!@!@  @!@  !@!   @!@  !@!")
    print("\t\t        !!!        !!!@!!!!   !!!@!!!!     !!!    !!!@!@!!!  !@!  !!!   !@!  !!!")
    print("\t\t        :!!        !!:  !!!   !!:  !!!     !!:               :!:  !!:   !!:  !!!")
    print("\t\t        :!:        :!:  !:!   :!:  !:!     :!:                ::!!:!    :!:  !:!")
    print("\t\t         ::: :::   ::   :::   ::   :::      ::                 ::::      :::: ::")
    print("\t\t         :: :: :    :   : :    :   : :      :                   :       :: :  :\n\n\n")
    print("=="*60,end="")
    user = input('''\n
                     _   _ ___ ___ ___ _  _   _   __  __ ___ _
                    | | | / __| __| _ \ \| | /_\ |  \/  | __(_)
                    | |_| \__ \ _||   / .` |/ _ \| |\/| | _| _
                     \___/|___/___|_|_\_|\_/_/ \_\_|  |_|___(_)    ''')
    passwd = getpass.getpass('''
                     ___  _   ___ _____      _____  ___ ___ _
                    | _ \/_\ / __/ __\ \    / / _ \| _ \   (_)
                    |  _/ _ \\\__ \__ \\\ \/\/ / (_) |   / |) |
                    |_|/_/ \_\___/___/ \_/\_/ \___/|_|_\___(_)     ''')
    
    
    main.loading()
    if user == "milind" and passwd == "1234":
        main.happy()
        pyttsx3.speak("you are SUCCESSFULLY LOGIN")
        next1("color 17")
        pyttsx3.speak("hey harry , WELCOME TO THE menu section")
        command.commands()
    else:
        main.sad()
        pyttsx3.speak("incorrect details, please try again")
    
def next1(text):
    os.system("cls")
    os.system(text)
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
    os.system("color 17")    
    time.sleep(0.08)
    print("=="*60,end="")
    print('''                           __      _____ _    ___ ___  __  __ ___   __  __ ___ _  _ _   _
                           \ \    / / __| |  / __/ _ \|  \/  | __| |  \/  | __| \| | | | |
                            \ \/\/ /| _|| |_| (_| (_) | |\/| | _|  | |\/| | _|| .` | |_| |
                             \_/\_/ |___|____\___\___/|_|  |_|___| |_|  |_|___|_|\_|\___/

    ''')
    print("=="*60,end=" \n")

    
def next(text):
    os.system("cls")
    os.system(text)
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
    os.system("color 17")    
    time.sleep(0.08)
    print("=="*60,end="")
