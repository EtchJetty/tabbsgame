#!/usr/bin/python
#This is an experiment.
from EnJinn.comnd import instaWrapp, textSettings
import subprocess
import platform
#This is imported for use in the subprocesses AKA different games.

instaWrapp("NOTE: If you load a save file from an incompatible gamemode, you are likely to crash your game.")
#Initialize your gamemode!

game = ""
localSpeed, localWidth = ["0.0", "48"]

def gamemode(game, localSpeed):
  instaWrapp("Available gamemodes: TABBS (main game), HELP (tutorial), DRAWER (demo), ABBA (easter egg)")
  instaWrapp("Type the name of the mode you would like to play. If you would like to edit display settings, including disabling the scrolling effect featured in all gamemodes, type SETTINGS or S.")
  if localSpeed == "0.0": 
    instaWrapp("The text scrolling effect is currently disabled.")
  if localSpeed != "0.0":
    instaWrapp("The text scrolling effect is currently enabled.")
  game = input("What gamemode are you trying to access? ").upper()
  return game


#Another note: all input()s are .upper()'d. Just makes it easier.

#Below are the initial values for certain game objects, like the drawer and door.

#As a final note: cyclomatic complexity is not real. Ignore the green line below.
while platform.system() == "Linux" or platform.system() == "Darwin":
    if game == "HELP":  #This part runs the tutorial.
        #I haven't found an easier way to do this.
        instaWrapp("Loading...")
        subprocess.run(["python3", "EnJinn/tutorial.py",localSpeed,localWidth])
    if game == "ABBA":
        subprocess.run(["python3", "abba.py",localSpeed,localWidth])
    if game == "DRAWER":
        subprocess.run(["python3", "drawerGame.py",localSpeed,localWidth])
    if game == "TABBS":
        instaWrapp("Work in progress!")
        instaWrapp("Loading...")
        subprocess.run(["python3", "Tabbs.py",localSpeed,localWidth])
    if game == "TEST":
        subprocess.run(["python3", "test.py"])
    if game == "BASH":
        subprocess.run(["bash"])
    if game == "OLDTABBS":
        subprocess.run(["python3", "whileLooptabbs.py"]) 
    if game == "SETTINGS" or game == "S":
        localSpeed, localWidth = textSettings()       
        localSpeed = str(localSpeed*100)
        localWidth = str(localWidth)
        game = "yeet"
    else:
        game = gamemode(game, localSpeed)

while platform.system() == "Windows":
    if game == "HELP":  #This part runs the tutorial.
        #I haven't found an easier way to do this.
        instaWrapp("Loading...")
        subprocess.run(["python", "EnJinn/tutorial.py",localSpeed,localWidth])
    if game == "ABBA":
        subprocess.run(["python", "abba.py",localSpeed,localWidth])
    if game == "DRAWER":
        subprocess.run(["python", "drawerGame.py",localSpeed,localWidth])
    if game == "TABBS":
        instaWrapp("Work in progress!")
        instaWrapp("Loading...")
        subprocess.run(["python", "Tabbs.py",localSpeed,localWidth])
    if game == "TEST":
        subprocess.run(["python", "test.py"])
    if game == "BASH":
        subprocess.run(["bash"])
    if game == "OLDTABBS":
        subprocess.run(["python", "whileLooptabbs.py"]) 
    if game == "SETTINGS" or game == "S":
        localSpeed, localWidth = textSettings()       
        localSpeed = str(localSpeed*100)
        localWidth = str(localWidth)
        game = "yeet"
    else:
        game = gamemode(game, localSpeed)

print("If you see this message, you're probably running on an unsupported OS. Try running the .py file for your desired gamemode directly.")
print("If you do that, be aware you have to run the files via command line with two params: speed and text width, in that order.")
print("For example, to run drawerGame.py with a speed of 4 and width of 48, you'd put into a Linux terminal:")
print("\"python3 drawerGame.py 4 4\"")
print("Additionally, the game does not work on certain outdated shells, including the default for Windows. If you get stdin/stdout errors, this is due to your shell selection.")