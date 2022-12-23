from colorama import Fore,Back,Style
import platform,os

OsName = platform.uname()[0]

def banner():
    if OsName == "Android":
      os.system("cls")
    else:
      os.system("clear")
    print(Fore.LIGHTWHITE_EX+"WELCOME TO GOLDPHISH!")   
    print(Fore.LIGHTWHITE_EX+"***************FEATURES****************")  
    print(Fore.LIGHTWHITE_EX+"• Obtain Device Information Without Any Permission !")
    print(Fore.LIGHTWHITE_EX+"• Access Location [SMARTPHONES ONLY]")
    print(Fore.LIGHTWHITE_EX+"• Access Webcam and directly send the image to you!")
    print(Fore.LIGHTWHITE_EX+"• Access Microphone")
    print(Fore.LIGHTWHITE_EX+"*********MADE BY A REAL RONALD D. GREAT*********")
    print(Fore.LIGHTWHITE_EX+"")
    print(Fore.LIGHTWHITE_EX+"Steps on how to run GoldPhish on any terminals")
    print(Fore.LIGHTWHITE_EX+"First thing to do is Read the ReadMe on GoldPhish github")
    print(Fore.LIGHTWHITE_EX+"2. type python3 goldphish.py to run the script")
    print(Fore.LIGHTWHITE_EX+"3. Make another session and host a NGROK link using 2525 port")
    print(Fore.LIGHTWHITE_EX+"4. Copy the link and give it to the target")
    
    print(Style.RESET_ALL)

banner()
