from modules import check
check.dependency()
check.check_started()
from colorama import Back,Fore,Style
from modules import banner,control
check.check_update()


PORT = 2525 

while True:
    banner.banner()
    control.run_php_server(PORT)
    try:
        input(" "+Fore.WHITE+Back.RED+"PRESS CTRL + C TO EXIT OR TURN OFF THE WEBSITE "+Style.RESET_ALL)
        control.kill_php_proc()
        exit()
    
    except:
        control.kill_php_proc()
        exit()
