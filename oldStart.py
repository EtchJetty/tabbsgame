#!/usr/bin/python
#This is an experiment.
from EnJinn.comnd import lbreak,optlist,what,cmd,avail_locs,inventory,room_objs,roomID,gold
#For future use of the engine, this is all that is needed. Put one of those (or just from EnJinn.comnd import *) to get all the features of the GUI!

#NOTE: The only feature this has that drawerGame.py does NOT have is the caseyBug variable and associated actions.

#It also does not have the fix implimented for devroute().


#This is imported for use in the subprocess of the Tutorial.
print("Available gamemodes: DRAWER, ABBA, HELP, TABBS")
#Initialize your gamemode!
game = input("Type START to begin. If you would like a tutorial, type HELP. ").upper()
gameStarted = 0 #This is the while loop that runs the actual game.

#Another note: all input()s are .upper()'d. Just makes it easier.


#Below are the initial values for certain game objects, like the drawer and door.
drawerState = "has something inside." 
doorState = "locked door"
caseyBug = "is wandering around."

while game == "START":
      gameStarted = 1 #Just making sure the game quits!
      while roomID == 1:
          lbreak() #You'll start to notice a pattern.
          avail_locs = ["DOOR"] #Every room has these three lines of code. 
          room_objs = ["PAPER","LADYBUG"] #These initialize room interaction.
          print("You are standing in the bedroom. The door is ajar.") #This is exposition.
          print("There is a piece of paper on the bed.")
          print("On the windowsill, a small ladybug " + caseyBug)
          optlist() #After each room's exposition, run optlist() to show options.
          cmd, roomID = what(cmd, avail_locs, inventory, room_objs, roomID, gold)
          #Ok, so the above line is *extremely* important. This activates the command line.
          #I'll explain how it works. cmd is the variable representing the actual user input.
          #what is the function.
          if cmd == "DOOR":
              print("You go through the open door.")
              roomID = 2
          elif cmd == "LADYBUG" and caseyBug == "is wandering around.":
              print("A small ladybug is wandering around on a shelf.")
              print("The moment it notices you, it flies away.")
              print("You realize it flew through a small crack in between the window and the sill.")
              print("The ladybug is free.")
              caseyBug = "has flown away."
          elif cmd == "LADYBUG" and caseyBug == "has flown away.":
              print("You look at the spot where the ladybug was.")
              print("You feel an odd mix of sadness and elation.")
              print("You hope the bug made it out okay.")
          elif cmd == "PAPER":
              print("The paper has a cryptic message on it.")
              print("You squint and make it out to say \"Aiden wuz here.\"")
      while roomID == 2:
          lbreak()
          avail_locs = ["DOOR", "HALL"]
          room_objs = ["DRAWER", "PHOTO"]
          print("You are now in the hallway.")
          print("Behind you is the bedroom.")
          print("Something is at the end of the hall.")
          print("There is a drawer. The drawer " + drawerState)
          print("Atop the drawer is a photograph.")
          optlist()
          cmd, roomID = what(cmd, avail_locs, inventory, room_objs, roomID, gold)
          if cmd == "DOOR":
              print("You go through back through the door.")
              roomID = 1
          elif cmd == "HALL":
              print("You head further down to the end of the hall.")
              roomID = 3
          elif cmd == "PHOTO":
              print("The photo has a handsome, bearded man on it.")
              print("It's signed: \"To my lovely wife Michelle.\"")
          elif cmd == "DRAWER" and drawerState == "has something inside.":
              print("You take a look in the drawer.")
              print(
                  "There is a small key. You eagerly put the key in your ITEMS pouch."
              )
              drawerState = "is empty of items."
              inventory.append("key")
          elif cmd == "DRAWER" and drawerState == "is empty of items.":
              print("The drawer coughs sadly.")
              print("\"You took my key,\" it says.")
              print("\"That was all I had.\"")
      while roomID == 3:
          lbreak()
          avail_locs = ["HALL", "END"]
          room_objs = ["PAINTING"]
          print("You are at the end of the hallway.")
          print("Behind you is the first part of the hall.")
          print("Ahead is a " + doorState + ".")
          if doorState == "locked door" and "LOCK" not in room_objs:
              room_objs.append("LOCK")
          print("There is a painting on the wall.")
          optlist()
          cmd, roomID = what(cmd, avail_locs, inventory, room_objs, roomID, gold)
          if cmd == "HALL":
              print("You return to the room with the drawer.")
              roomID = 2
          elif cmd == "END" and doorState != "locked door":
              print("You did it!")
              print("You win!")
              exit()
          elif cmd == "PAINTING":
              print("The painting is of a very handsome man.")
              print("The small caption next to it says,")
              print("\"Facts don't care about your feelings.\"")
          elif cmd == "END" and doorState == "locked door":
              print("Unfortunately, the door is locked.")
              print("If only you had a key...")
              roomID = 3
          elif cmd == "LOCK" and "key" in inventory and "LOCK" in room_objs:
              print("You open the lock with your key.")
              print(
                  "The lock falls off the door and clatters to the ground before disappearing in a puff of magical smoke."
              )
              print("The key is gone from your ITEMS.")
              inventory.remove("key")
              doorState = "lock-less door"
              room_objs.remove("LOCK")
          elif cmd == "LOCK" and "key" not in inventory and doorState == "locked door" and "LOCK" in room_objs:
              print("You stare at the lock.")
              print("Nothing happens.")