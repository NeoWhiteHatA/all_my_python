import os
import platform
from modules.CyberScanner import portscanner
from modules.AircrackWifi import aircrackwifi
from modules.AirodumpWifi import airodumpwifi

mainlogo = r'''
'''
#main
def main():
    os.system('chmod +x*')
    os.system('clear')
    print(mainlogo)
    print('
          [1] Portscanner
          [2] Capture Handshake of the closest Networks
          [3] Capture Handshake of specific Network
          [4] Automated Metasploit
          Metasploit
          [99] Exit'
    )
menu_option = int(input('[option] ==>'))
if menu_option == 1:
    portscanner()
elif menu_option == 2:
    aircrackwifi()
elif menu_option == 3:
    airodumpwifi
elif menu_option == 4:
    automatedmetasploit()
elif menu_option == 99:
    exit()
else:
    print(
        'wrong command')
if __name__ == '__main__':
    main()
    print('[$] Creater by NeoWhiteHat with love')