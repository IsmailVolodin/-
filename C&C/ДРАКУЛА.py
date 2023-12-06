#!/usr/bin/env python
#
#AUTHOR: IsmailVolodin
#VERSION: 1.0.0 [BETA]
#COUNTRY: Russian
#GITHUB: https://github.com/IsmailVolodin
#DISCORD: ismailvolodin_
#
#############
# LIBRARIES #
#############
import os
import time

BANNER = ("""

 ▓█████▄  ██▀███   ▄▄▄       ▄████▄   █    ██  ██▓    ▄▄▄      
 ▒██▀ ██▌▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██  ▓██▒▓██▒   ▒████▄    
 ░██   █▌▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓██  ▒██░▒██░   ▒██  ▀█▄  
 ░▓█▄   ▌▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓▓█  ░██░▒██░   ░██▄▄▄▄██ 
 ░▒████▓ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒▒█████▓ ░██████▒▓█   ▓██▒
  ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▒   ▓▒█░
  ░ ▒  ▒   ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░░▒░ ░ ░ ░ ░ ▒  ░ ▒   ▒▒ ░
  ░ ░  ░   ░░   ░   ░   ▒   ░         ░░░ ░ ░   ░ ░    ░   ▒   
    ░       ░           ░  ░░ ░         ░         ░  ░     ░  ░
  ░                         ░                                  

 AUTHOR: IsmailVolodin
 VERSION: 1.0.0 [BETA]
 COUNTRY: Russian
 GITHUB: https://github.com/IsmailVolodin
 DISCORD: ismailvolodin_
""")

os.system("cls")

def ДРАКУЛА():

    print(BANNER)
     
    print("")
    print(" [...] Идет запуск программного обеспечения [ДРАКУЛА]...")
    time.sleep(10)
    print("")
    os.system("ncat -lnvp 9001")

ДРАКУЛА()