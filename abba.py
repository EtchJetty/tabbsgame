from EnJinn.comnd import lbreak, optlist, what, cmd, inventory, gold, textSpeedGLOBAL, textWidthGLOBAL, name, wrapp, addInv,storyProg, vardef

varlist = ["doorState","garageState","roomID"]
storyProg = vardef(storyProg, varlist)

storyProg.update({"roomID":1})

from EnJinn.comnd import textInit

import sys
settings = sys.argv

localSpeed = settings[1] 
localWidth = settings[2]

textInit(localSpeed, localWidth)


game = 1
while game == 1:
    while storyProg["roomID"] == 1:
        lbreak()
        avail_locs = ["GARAGEDOOR"]
        room_objs = ["DASHBOARD"]
        wrapp("You're sitting in a gorgeous device.")
        wrapp("Invented by a genius, it allows you to drive thousands of miles without a single drop of petrol.")
        if "WALLET" not in inventory:
           room_objs.append("WALLET")
           wrapp("Your wallet sits on the dash.")
        wrapp("You stroke your photograph of Elon Musk, as you do every time you sit in your car.")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
        cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if "WALLET" not in inventory and cmd == "WALLET" or cmd == "WA" and "WALLET" not in inventory:
            wrapp("You put your wallet in your ITEMS.")
            room_objs.remove("WALLET")
            addInv(inventory, "WALLET")
        elif cmd == "DASHBOARD" or cmd == "DA":
            wrapp("You click on the dashboard.")
            wrapp("Yup, the map confirms it; you're in your garage.")
            wrapp("You can't wait until they release Grand Theft Auto: Tesla Edition, the version rumored to be totally playable from inside your car.")
            if storyProg["garageState"] == 0: 
                wrapp("While you're messing with the dash, you open the garage door via the Tesla's on-screen garage door opener.")
                storyProg["garageState"] = 1
            else:
                wrapp("The garage door is already open.")
        elif cmd == "GARAGEDOOR" and storyProg["garageState"] == 1 or cmd == "G" and storyProg["garageState"] == 1:
            wrapp("You exit your car and walk outside.") 
            storyProg["roomID"] = 2
        elif cmd == "GARAGEDOOR" and storyProg["garageState"] == 0 or cmd == "G" and storyProg["garageState"] == 0:
            wrapp("You exit your car, but the garage door is not open.")
            wrapp("You return to the warmth of the Tesla's heated interior.")
    while storyProg["roomID"] == 2:
        lbreak()
        avail_locs = ["GARAGEDOOR","HOUSEDOOR"]
        room_objs = ["DEADGRASS"]
        wrapp("You are now outside.")
        wrapp("From your position right next to the front door, the dead grass on the lawn is clearly visible.")
        wrapp("You see the front door.")
        if storyProg["doorState"] == 0:
            wrapp("Unfortunately, it is locked.")
            wrapp("You remember leaving your house key in your wallet.")
            if "WALLET" not in inventory:
                wrapp("Now where did you put it?")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
        cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)

        if cmd == "GARAGEDOOR" or cmd == "G":
            wrapp("You re-enter the garage.")
            storyProg["roomID"] = 1
        if cmd == "HOUSEDOOR" and storyProg["doorState"] == 0 or cmd == "H" and storyProg["doorState"] == 0:
            wrapp("You jiggle the doorknob. Locked.")
            if "WALLET" in inventory:
                wrapp("Luckily, you have a key.")
                wrapp("The door is unlocked in short order, and you walk inside.")
                storyProg["roomID"] = 3 
            else:
                wrapp("Where was that wallet again?")
        if cmd == "HOUSEDOOR" and storyProg["doorState"] == 1 or cmd == "H" and storyProg["doorState"] == 1:
            wrapp("You walk into the house.")
            storyProg["roomID"] = 3
        if cmd == "DEADGRASS" or cmd == "DE":
            wrapp("You look at the dead grass. Ugh.")
    while storyProg["roomID"] == 3:
        avail_locs = ["HOUSEDOOR"]
        room_objs = ["FAMILY"]
        wrapp("As you enter your house, your entire family greets you.")
        wrapp("\"Happy birthday, Abba!\"")
        wrapp("Type END to quit.")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
        cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)

        if cmd == "HOUSEDOOR" or cmd == "H":
            wrapp("You turn away from your loving family to take a breath of fresh air.")
            storyProg["roomID"] = 2
        if cmd == "FAMILY" or cmd == "FA":
            wrapp("You hug your family.")
            wrapp("Happy 46th!")
        if cmd == "END":
            wrapp("The end. Happy birthday!")
            exit()