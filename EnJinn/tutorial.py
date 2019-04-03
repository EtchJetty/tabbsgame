#!/usr/bin/python
#This is an experiment.
from comnd import lbreak, optlist, what, cmd, avail_locs, inventory, room_objs, gold, tutorialWhat, textSettings, wrapp, textSpeedGLOBAL, textWidthGLOBAL
storyProg = {}
name = "TutorialMan"
from comnd import textInit

import sys
settings = sys.argv

localSpeed = settings[1]
localWidth = settings[2]

textInit(localSpeed, localWidth)


def caveWhat(cmd, avail_locs):
    print("Here are your options:")
    print("(T)RAVEL")
    cmd = input("What do you do? ").upper()
    lbreak()
    while cmd == "TRAVEL" or cmd == "T":
        print("Below are all available movement options:")
        if avail_locs == []:
            print("None. You are trapped.")
        else:
            for location in range(len(avail_locs) - 1):
                print(end="(")
                print(avail_locs[location][:1], end="")
                print(end=")")
                print(avail_locs[location][1:], sep=', ', end=", ")
            print(end="(")
            print(avail_locs[-1][:1], end="")
            print(end=")")
            print(avail_locs[-1][1:])
        cmd = input("What do you do? ").upper()
        lbreak()
    return cmd


wrapp(
    "Welcome! Before we get started, have you ever played games like ZORK and HOMESTUCK?"
)
wrapp("Below are a list of your options:")
wrapp("(Y)ES, (N)O, SETTINGS, QUIT")
wrapp(
    "Type out your answer! You can type YES, NO, Y, or N, and these can be uppercase or lowercase. To edit text display settings, including disabling or changing the speed of the scrolling effect, type SETTINGS."
)
answ = input("What do you say? ").upper()
if answ == "SETTINGS":
    textSettings()
if answ == "QUIT":
    exit()
if answ == "YES" and answ == "Y":
    wrapp("Nerd.")
    wrapp(
        "Right, throw away everything you know about user input from those games."
    )
    wrapp("Also, Homestuck is a web experience. Not a video game. Sadly.")
if answ == "NO" and answ == "N":
    wrapp("Okay. Cool.")
    wrapp("You might actually be better off than the nerds.")
wrapp("So the way you interact with the game window is through COMMANDS.")
wrapp(
    "A command is listed in CAPITAL LETTERS, like the YES and NO options you saw earlier."
)
wrapp("Below are a list of your options:")
wrapp("(Y)ES, (N)O")
answ = input("Got it? ").upper()
if answ == "YES" or answ == "Y":
    wrapp("Right!")
else:
    wrapp("Seriously? You actually don't get it?")
    wrapp("Below are a list of your options:")
    wrapp("(C)ONFUSED, (J)OKING")
    answ = input("Be honest now: ").upper()
    if answ == "JOKING" or answ == "J":
        wrapp("Okay.")
        wrapp("Smartass.")
        wrapp("Moving on.")
    else:
        wrapp("Right, I don't think this game is for you.")
        wrapp(
            "If you can't type the simple command YES I don't know how to help you."
        )
        exit()
wrapp("Okay. So obviously, the game involves more commands than YES and NO.")
wrapp(
    "In fact, there are a lot of commands. For example, in the average room in the game, you can type the name of any place you want to travel to, any item you want to interact with, any person you want to talk to and more!"
)
wrapp("In order to make this less confusing, we introduced LOOKUP MENUS.")
wrapp("They look a little like this: ")
wrapp("\"Here are your options:\"")
wrapp("\"(T)RAVEL | (I)TEMS | (A)CT\"")
wrapp("Below are a list of your options: ")
wrapp("(Y)ES, (N)O")
answ = input("These will ALWAYS be accessible. Follow so far? ").upper()
if answ == "YES" or answ == "Y":
    wrapp("Neat.")
    wrapp(
        "So what you do is type the name of the menu into your command space.")
    wrapp("That gives you a list of commands related to the menu.")
if answ == "NO" or answ == "N":
    wrapp("Okay. It's really not hard.")
    wrapp("It's sort of like a menu on computers.")
    wrapp(
        "All you do is click on (well, type) the name of the menu, or the first letter."
    )
    wrapp("That menu has a list of things you can do.")
wrapp(
    "And you don't need to type TRAVEL each time if you know where you're going."
)
wrapp("Let's do an example. I'll get rid of all the menus but TRAVEL.")
wrapp("For reference, you can type TRAVEL or T, both work.")
storyProg.update({"roomID": 0})
storyProg.update({"minigame": 1})
while storyProg["minigame"] == 1:
    while storyProg["roomID"] == 0:
        lbreak()
        wrapp(
            "You are standing in a cave. You see in front of you the cave's opening."
        )
        avail_locs = ["OPENING"]
        cmd = caveWhat(cmd, avail_locs)
        if cmd == "OPENING" or cmd == "O":
            wrapp(
                "You make your way out of the cave, clambering up a small crag."
            )
            storyProg.update({"roomID": 1})
    while storyProg["roomID"] == 1:
        lbreak()
        wrapp("You are now outside the cave.")
        wrapp("To your right is a path leading downwards.")
        wrapp("To your left is a cliff, sheer and steep.")
        avail_locs = ["CLIFF", "PATH", "OPENING OF CAVE"]
        cmd = caveWhat(cmd, avail_locs)
        if cmd == "CLIFF" or cmd == "C":
            wrapp("You died. Instantly.")
            wrapp("I'm judging you pretty hard right now.")
            storyProg["minigame"] = 0
            storyProg["roomID"] = 420
        if cmd == "PATH" or cmd == "P":
            wrapp("You stumble down the path, watching your feet.")
            storyProg["roomID"] = 2
        if cmd == "OPENING OF CAVE" or cmd == "O":
            wrapp("You head back into the cave.")
            storyProg["roomID"] = 0
    while storyProg["roomID"] == 2:
        lbreak()
        wrapp("This is pretty much the end of this part of the tutorial.")
        wrapp("Try navigating back up the PATH without using TRAVEL!")
        avail_locs = ["END", "PATH"]
        cmd = caveWhat(cmd, avail_locs)
        if cmd == "END" or cmd == "E":
            storyProg.update({"minigame": 9999})
            storyProg.update({"roomID": 99999})
        if cmd == "PATH" or cmd == "P":
            wrapp("You walk back up the path.")
            storyProg.update({"roomID": 1})
wrapp("Nice job!")
wrapp("Here are your options:")
wrapp("(Y)ES, (N)O")
answ = input("Was that fun? ").upper()
if answ == "YES" or answ == "Y":
    wrapp("Great! I had fun making it.")
else:
    wrapp("Okay... well, at least you know how to TRAVEL.")
wrapp("TRAVEL and ACT work very similarly to each other.")
wrapp("If you want to ACT, you can type ACT to pull up the command list.")
wrapp("However, if you know the command or its shortcut, you can just do it.")
wrapp(
    "Also, adding on to this, the MENU button is for editing the text width, text speed, saving, and loading."
)
wrapp(
    "Feel free to ignore it; it's not vital to gameplay, unless you want to put the game down and pick it up later."
)
wrapp("Let's try this.")
storyProg.update({"minigame": 2})
storyProg.update({"roomID": 1})
while storyProg["minigame"] == 2:
    while storyProg["roomID"] == 1:
        lbreak()
        avail_locs = []
        room_objs = ["JOHN"]
        wrapp("You're standing across from JOHN.")
        wrapp("He knows how to end this part of the tutorial.")
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = tutorialWhat(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if cmd == "JOHN" or cmd == "JO":
            wrapp("John looks at you, and smiles.")
            wrapp("\"Ah! Fair traveller!\" says John.")
            wrapp(
                "\"Would you like to know how to end this part of the tutorial?\""
            )
            wrapp("Here are your options:")
            wrapp("(Y)ES, (N)O")
            resp = input("What do you say? ").upper()
            lbreak()
            if resp == "NO" or resp == "N":
                wrapp("John frowns, but says nothing.")
            elif resp == "YES" or resp == "Y":
                wrapp("\"Type \"END\" as a command!\" John exclaims.")
                wrapp(
                    "\"I have no idea what that means, but that's what I was told to say!\""
                )
            else:
                wrapp(
                    "John shakes his head. He has no idea what you meant by that."
                )
        elif cmd == "END":
            wrapp("You did it!")
            storyProg["minigame"] = 0
            storyProg["roomID"] = 999999999
wrapp("Finally, ITEMS is a bit of an odd duck.")
wrapp("Some items are not interactive. These are written in lowercase.")
wrapp("Interactive items are in UPPERCASE.")
wrapp(
    "A lowercase item, like a passport, will be with you, and useful for an ACTion."
)
wrapp(
    "An uppercase item, like a MAP, can be looked at regardless of room. This is also how you view flavor text on items that have them."
)
wrapp(
    "ITEMS also have no shortcuts. Sorry, but you have to type out the whole thing."
)
wrapp("That's it!")
storyProg.update({"minigame": 3})
storyProg.update({"roomID": 1})
while storyProg["minigame"] == 3:
    if storyProg["roomID"] == 1:
        lbreak()
        avail_locs = []
        room_objs = ["SAFE"]
        if "BROCHURE" not in inventory:
          room_objs.append("BROCHURE")
        if "safe keycard" not in inventory:
          room_objs.append("KEY")
        wrapp("You're standing in front of a safe.")
        wrapp("On a small table beside the safe is a keycard.")
        wrapp("Beside the keycard is a brochure.")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if cmd == "BROCHURE" and "BROCHURE" not in inventory or cmd == "BR" and "BROCHURE" not in inventory:
            wrapp(
                "You look at the brochure. It features attractive images of volcanoes and islands."
            )
            wrapp(
                "You take it for later perusal, putting it in your ITEMS pouch."
            )
            inventory.append("BROCHURE")
        elif cmd == "SAFE" and "safe keycard" not in inventory or cmd == "SA" and "safe keycard" not in inventory:
            wrapp("You try to pry open the safe with your bare hands.")
            wrapp("This is ineffective in general.")
        elif cmd == "SAFE" and "safe keycard" in inventory or cmd == "SA" and "safe keycard" in inventory:
            wrapp("You pry open the safe, revealing the end of the tutorial!")
            wrapp("Nice job!")
            storyProg.update({"minigame": 0})
            storyProg.update({"roomID": 99999})
        elif cmd == "KEY" and "safe keycard" not in inventory or cmd == "KE" and "safe keycard" not in inventory:
            wrapp("You take the key from the table, putting it in your ITEMS.")
            inventory.append("safe keycard")
wrapp("Here are your options:")
wrapp("(Y)ES, (N)O")
answ = input("Ready to play? ").upper()
if answ == "YES" or answ == "Y":
    wrapp("Okay!")
else:
    wrapp("Too bad!")
wrapp("One final note: you NEED to have proper capitalization.")
wrapp("Don't add spaces or anything. It has to be exact.")
wrapp("Have fun! Type the name of the gamemode to start playing.")
