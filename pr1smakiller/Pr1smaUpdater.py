import time
import os
print("[Pr1smaKiller Updater]")
print("by x04000")
print("")
print("Updating Pr1smaKiller...")
time.sleep(1)
try:
	os.system("wget https://raw.githubusercontent.com/x04000/Pr1smaKiller/main/pr1smakiller/version")
	os.system("mv version.1 version")
	os.system("cd ..")
	os.system("wget https://raw.githubusercontent.com/x04000/Pr1smaKiller/main/Pr1smaKiller.py")
	os.system("mv Pr1smaKiller.py.1 Pr1smaKiller.py")
except KeyboardInterrupt:
	print("[X] KeyboardInterrupt")
except:
	print("[X] A error ocurred during the updating")
time.sleep(1)
print("")
print("Please, restart Pr1smaKiller to apply the changes.")
print("")
print("If you experiment problems with Pr1smaKiller, please reinstall them.")
print("Operation finished!")