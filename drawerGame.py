#!/usr/bin/python
#This is an experiment.
from EnJinn.comnd import lbreak,optlist,what,cmd,inventory,gold,textSpeedGLOBAL,textWidthGLOBAL,wrapp,storyProg, instaWrapp
#For future use of the engine, this is all that is needed. Put one of those (or just from EnJinn.comnd import *) to get all the features of the GUI!
name = "Drawer Dave"
#Initialize your gamemode!
gameStarted = 0 #This is the while loop that runs the actual game.

from EnJinn.comnd import textInit

import sys
settings = sys.argv

localSpeed = settings[1] 
localWidth = settings[2]

textInit(localSpeed, localWidth)

#Another note: all input()s are .upper()'d. Just makes it easier.

#Below are the initial values for certain game objects, like the drawer and door.

drawerState = "has something inside." 
doorState = "locked door"
roomID = 1
instaWrapp("NOTE: Saving does not work for this gamemode.")

#As a final note: cyclomatic complexity is not real. Ignore the green line below.
while gameStarted == 0:
    while roomID == 1: #A while loop. Each room is wrapped in one.
      lbreak()       #You'll start to notice a pattern.
      avail_locs = ["DOOR"] #Every room has these three lines of code. 
      room_objs = ["PAPER"] #These initialize room interaction. Also formatting.
      wrapp("You are standing in the bedroom. The door is ajar.") #This is exposition.
      wrapp("There is a piece of paper on the bed.")
      optlist() #After each room's exposition, run optlist() to show options.
      cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
        cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
      #Ok, so the above line is *extremely* important. This activates the command line.
      #I'll explain how it works. cmd is the variable representing the actual user input.
      #what is the function.
      if cmd == "DOOR" or cmd == "D": #An example of room travel.
        wrapp("You go through the open door.") #Every room has transition text.
        roomID = 2 #This is the actual roomID change. 
      elif cmd == "PAPER" or cmd == "PA": #You get the point
        wrapp("The paper has a cryptic message on it.")
        wrapp("You squint and make it out to say \"Aiden wuz here.\"")
    while roomID == 2:
      lbreak() #Initialising locations and objects. You getcha.
      avail_locs = ["DOOR", "HALL"]
      room_objs = ["DRAWER", "PHOTO"]
      wrapp("You are now in the hallway.")
      wrapp("Behind you is the bedroom.")
      wrapp("Something is at the end of the hall.")
      wrapp("There is a drawer. The drawer " + drawerState)
      wrapp("Atop the drawer is a photograph.")
      optlist()
      cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
        cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
      if cmd == "DOOR":
        wrapp("You go through back through the door.")
        roomID = 1
      elif cmd == "HALL" or cmd == "H":
        wrapp("You head further down to the end of the hall.")
        roomID = 3
      elif cmd == "PHOTO" or cmd == "PH":
        wrapp("The photo has a handsome, bearded man on it.")
        wrapp("It's signed: \"To my lovely wife Michelle.\"")
      elif cmd == "DRAWER" and drawerState == "has something inside." or cmd == "DR" and drawerState == "has something inside.":
        wrapp("You take a look in the drawer.")
        wrapp("There is a small key. You eagerly put the key in your ITEMS pouch.")
        drawerState = "is empty of items."
        inventory.append("key")
      elif cmd == "DRAWER" and drawerState == "is empty of items." or cmd == "DR" and drawerState == "is empty of items.":
        wrapp("The drawer coughs sadly.")
        wrapp("\"You took my key,\" it says.")
        wrapp("\"That was all I had.\"")
    while roomID == 3:
      lbreak()
      avail_locs = ["HALL", "END"]
      room_objs = ["PAINTING"]
      wrapp("You are at the end of the hallway.")
      wrapp("Behind you is the first part of the hall.")
      wrapp("Ahead is a " + doorState + ".")
      if doorState == "locked door" and "LOCK" not in room_objs:
        room_objs.append("LOCK")
      wrapp("There is a painting on the wall.")
      optlist()
      cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
        cmd, avail_locs, inventory, room_objs, storyProg, gold,
        textSpeedGLOBAL, textWidthGLOBAL, name)
      if cmd == "HALL" or cmd == "H":
        wrapp("You return to the room with the drawer.")
        roomID = 2
      elif cmd == "END" and doorState != "locked door":
        wrapp("You did it!")
        wrapp("You win!")
        game = "END"
        exit()
      elif cmd == "PAINTING":
        wrapp("The painting is of a very handsome man.")
        wrapp("The small caption next to it says,")
        wrapp("\"Facts don't care about your feelings.\"")
      elif cmd == "END" and doorState == "locked door":
        wrapp("Unfortunately, the door is locked.")
        wrapp("If only you had a key...")
        roomID = 3
      elif cmd == "LOCK" and "key" in inventory and "LOCK" in room_objs:
        wrapp("You open the lock with your key.")
        wrapp("The lock falls off the door and clatters to the ground before disappearing in a puff of magical smoke.")
        wrapp("The key is gone from your ITEMS.")
        inventory.remove("key")
        doorState = "lock-less door"
        room_objs.remove("LOCK")
      elif cmd == "LOCK" and "key" not in inventory and doorState == "locked door" and "LOCK" in room_objs:
        wrapp("You stare at the lock.")
        wrapp("Nothing happens.")