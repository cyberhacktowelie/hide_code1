code= '''#!/usr/bin/python3
#coding:utf-8
import requests
import os
import sys
import time
import json
import requests

logo="""

\033[1;92m███╗  ██╗       █████╗ ███╗  ██╗ █████╗ ███╗   ███╗
\033[1;92m████╗ ██║      ██╔══██╗████╗ ██║██╔══██╗████╗ ████║
\033[1;91m██╔██╗██║█████╗███████║██╔██╗██║██║  ██║██╔████╔██║
\033[1;91m██║╚████║╚════╝██╔══██║██║╚████║██║  ██║██║╚██╔╝██║
\033[1;92m██║ ╚███║      ██║  ██║██║ ╚███║╚█████╔╝██║ ╚═╝ ██║
\033[1;92m╚═╝  ╚══╝      ╚═╝  ╚═╝╚═╝ ╚══╝ ╚════╝  ╚═╝     ╚═╝
\033[1;31m---------------------------------------
\033[1;35mCREATED BY : \033[33mCyberHackTowelie
\033[1;35mGITHUB     : \033[1;33mgithub.com/cyberhacktowelie
\033[1;31m---------------------------------------
"""

def logop(z):
    for word in z + '\\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)

### WARNING MSG ####
warning = """
\033[1;31mWARNING :\033[1;33m DONT USE THIS TO HARM OTHERS ! THIS SCRIPT IS ONLY FOR EDUCATIONAL PURPOSES OR TO PRANK
"""

def war(z):
    for word in z + '\\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.03)

#### MENU #####
menu = """
\033[1;33m[1]\033[1;31m >>  \033[1;36mANONYMOUS-SMS \033[1;34m(V > 0.1.1)
\033[1;33m[2]\033[1;31m >>  \033[1;36mGET-UPDATE
\033[1;33m[3]\033[1;31m >>  \033[1;36mHELP 
\033[1;33m[4]\033[1;31m >>  \033[1;36mEXIT
"""


## ANONYMOUS0-SMS FUNTION ####

def main():
    #os.system('clear')
    print(chr(27) + "[2J")
    print (logo)
    war(warning)
    print
    print ("\033[1;31m[+] WITH COUNTRY CODE \033[1;31m[+]")
    print
    phn = input("\033[1;31m[+]\033[1;32m ENTER PHONE NUMBER :\033[1;36m ")
    msg = input ("\033[1;31m[+]\033[1;32m ENTER YOUR MSG     :\033[1;36m ")
    resp = requests.post('https://textbelt.com/text', {
   'phone': phn,
   'message': msg,
   'key': 'textbelt',
    })
    print(resp.json())
    
#### INTRO ######
def intro():
    #os.system('clear')
    print(chr(27) + "[2J")
    logop(logo)
    print
    print (menu)
    choise = input('\033[1;31m[~] \033[1;32mENTER AN OPTION :  \033[1;35m ')
    
    if choise == "1":
       #os.system('clear')
       print(chr(27) + "[2J")
       main()
    
    elif choise == "3":
       os.system("xdg-open https://m.facebook.com/nabil.404")
       intro()
    
    elif choise == "4":
         os.system("exit")
         print ("THANKS FOR USING : )")

	## UPDATE ###
    elif choise == "2":
         print ("\033[1;92m")
         #os.system('clear')
         print(chr(27) + "[2J")
         os.system('figlet UPDATE')
         os.system('apt update && apt upgrade && pip2 install requests && git clone https://github.com/cyberhacktowelie/N-ANOM && cd N-ANOM && python3 n-anom.py')
    else:
        print 
        print
        print ("\033[1;31mINVILED CHOISE ! ")
    
intro()
'''
full=[]
for char in code:
    character=""
    for i in range(0,ord(char)):
        character += '+'
    full.append(character)
print(full)

exec("".join([chr(len(i)) for i in full]))
