def lbreak():
    print("_____________________________")
storyProg = {}

varlist = []

def wip():
    wrapp("Room not complete yet!")
    wrapp("Use devroute to TP to a room that works.")
    wrapp("Ask your local gamedev for more information.")

def vardef(storyProg, varlist):
  for x in varlist:
    storyProg.update({x:0})
  return storyProg

import subprocess
name = ""
gold = 0
inventory = []
storyProg["roomID"] = 1
avail_locs = ["OPENING"]
room_objs = []
cmd = ""

textWidthGLOBAL = 48
textSpeedGLOBAL = 0.04

def textInit(speedlocal, widthlocal): 
  global textWidthGLOBAL
  global textSpeedGLOBAL
  speedlocal = float(speedlocal)/100
  textWidthGLOBAL = int(widthlocal)
  textSpeedGLOBAL = speedlocal

import json

def load(storyProg, gold, inventory):
  print("Loading...")
  with open('data.txt') as json_file:  
    saveFileContent = json.load(json_file)
    storyProg,gold,inventory = saveFileContent
  print("Load complete!")
  return storyProg, gold, inventory

def save(storyProg, gold, inventory):
  print("Saving...")
  saveFileContent = [storyProg,gold,inventory]
  with open('data.txt', 'w') as outfile:  
    json.dump(saveFileContent, outfile)
  print("Save complete!")
  print(json.dumps(saveFileContent))

import textwrap
import sys
import time

def addInv(inventory, Item):
  inventory.append(Item)
  wrapp("You got " + Item + "! It can be found in your ITEMS.")

def cashier(catalog, gold, cmd):
    for item in catalog:
        print(end="(")
        print("{}".format(item["itemName"][:1]), end="")
        print(end=")")
        print("{}".format(item["itemName"][1:]), end=" (")
        print("{}".format(item["status"]), end=")\n")
    print("Your gold: " + str(gold) + "G")
    print("Type Q or QUIT to quit.")
    instaWrapp("You will have an opportunity to confirm your purchase after selecting an item. Selecting an item allows you to view its description.")
    cmd = input("What do you want to buy? ").upper()
    return cmd

def instaWrapp(string):
  global textWidthGLOBAL
  #global textSpeedGLOBAL
  wrapper = textwrap.TextWrapper(width=textWidthGLOBAL)
  word_list = wrapper.wrap(text=string)
  for element in word_list:
      print(element)

def wrapp(string):
    global textWidthGLOBAL
    global textSpeedGLOBAL
    if textSpeedGLOBAL != 0:
        string = string + "\n"
        approachWidth = 0
        for element in string.split(" "):
            element = element + " "
            approachWidth = approachWidth + len(element)
            if textWidthGLOBAL - approachWidth < 1:
                element = "\n" + element
                approachWidth = len(element)
            for c in range(len(element)):
                sys.stdout.write(element[c])
                sys.stdout.flush()
                time.sleep(textSpeedGLOBAL)
        sys.stdout.write("\b")
    else:  #for non-scrolling text
        wrapper = textwrap.TextWrapper(width=textWidthGLOBAL)
        word_list = wrapper.wrap(text=string)
        for element in word_list:
            print(element)

def shop(itemname,catalog,gold):
    cmd = ""
    for item in catalog:
      if item["itemName"] == itemname:
        if item["status"] is not "SOLD":
          wrapp("{}".format(item["itemDesc"]))
          wrapp("Would you like to purchase this item for " + item["status"] + "? ")
          cmd = yesno(cmd)
          if cmd == "Y" or cmd == "YES":
            price = int(item["status"][:-1])
            if int(gold) - price < 0:
              wrapp("You don't have enough gold!")
            else:
              gold = int(gold)
              gold = gold - price
              addInv(inventory, item["itemName"])
              item["status"] = "SOLD"
        else:
          wrapp("You already bought this!")
    return gold


def optlist():
    print("Here are your options: ")
    wrapp("(T)RAVEL | (I)TEMS | (A)CT | MENU")

def textSettings():
  global textSpeedGLOBAL
  global textWidthGLOBAL
  print("NOTE: Text speed measured in hundredth of a second per character, and width in characters per line.")
  print("Define global text display settings now: ")
  settingsUnset = 0
  cmd = ""
  while settingsUnset == 0:
    badNumb = 0
    while badNumb == 0:
      rows, columns = subprocess.check_output(['stty', 'size']).split()
      column = str(columns)
      colum = int(column[2:-1])
      print("Your current shell width is " + str(colum) + " characters.")
      textWidthGLOBAL = input("(default 48) textWidth = ")
      try:
          if textWidthGLOBAL != "":
            tempVar = int(textWidthGLOBAL)
            time.sleep(tempVar/100)
      except (TypeError, ValueError):
          print("Please enter a valid number.")
      else:
          badNumb = 1
    if textWidthGLOBAL == "":
      textWidthGLOBAL = colum
    else:
      textWidthGLOBAL = int(textWidthGLOBAL)
    badNumb = 2
    while badNumb == 2:
      textSpeedGLOBAL = input("(default 4. 0 to disable scroll effect.) textSpeed = ")
      try: 
        if textSpeedGLOBAL != "":
          tempVar = int(textSpeedGLOBAL)
          time.sleep(tempVar/100)
      except (TypeError, ValueError):
        print("Please enter a valid number.")
      else:
        badNumb = 1
    if textSpeedGLOBAL == "":
      textSpeedGLOBAL = 0.04
    else:
      textSpeedGLOBAL = float(textSpeedGLOBAL)/100
    wrapp("Text width set to " + str(textWidthGLOBAL) +" and text speed set to " + str(textSpeedGLOBAL) + ". Are these settings acceptable?")
    cmd = yesno(cmd)
    if cmd == "YES" or cmd == "Y":
      settingsUnset = 1
  return textSpeedGLOBAL, textWidthGLOBAL


def what(cmd, avail_locs, inventory, room_objs, storyProg, gold, textSpeedGLOBAL, textWidthGLOBAL, name):
    cmd = input("What do you do? ").upper()
    lbreak()

    

    TIA = 0
    while TIA == 0:
        while cmd == "MENU":
            print("SAVE, LOAD, SETTINGS, QUIT")
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

        while cmd == "ITEMS" or cmd == "I":
            print("Below is a list of your items:")
            if inventory == []:
                print("Empty!")
            else:
                for Item in range(len(inventory) - 1):
                    print(inventory[Item], sep=', ', end=", ")
                print(inventory[-1])
            print("Current Gold: " + str(gold) + "GP")
            cmd = input("What do you do? ").upper()
            lbreak()

        while cmd == "ACT" or cmd == "A":
            print("Below is a list of interactable objects:")
            if room_objs == []:
                print("Nothing here is interactable.")
                print("Try TRAVELling!")
            else:
                for Item in range(len(room_objs) - 1):
                    print(end="(")
                    print(room_objs[Item][:2], end="")
                    print(end=")")
                    print(room_objs[Item][2:], sep=', ', end=", ")
                print(end="(")
                print(room_objs[-1][:2], end="")
                print(end=")")
                print(room_objs[-1][2:])
            cmd = input("What do you do? ").upper()
            lbreak()
        if cmd != "ACT" and cmd != "A" and cmd != "I" and cmd != "ITEMS" and cmd != "T" and cmd != "TRAVEL" and cmd != "MENU":
            TIA = 1
    if cmd == "BROCHURE" and "BROCHURE" in inventory:
        wrapp(
            "The brochure looks nice, but the contents make you think you don't want to go to San Jacinto anytime soon."
        )
    if cmd == "QUIT":
        wrapp("Are you sure you would like to quit?")
        cmd = yesno(cmd)
        if cmd == "YES" or cmd == "Y":
            exit()
    if cmd == "SETTINGS":
      textSettings()
    if cmd == "SAVE":
        save(storyProg, gold, inventory)
    if cmd == "LOAD":
        storyProg, gold, inventory = load(storyProg, gold, inventory)
    if cmd == "WALLET" and "WALLET" in inventory:
        wrapp("You check your wallet.")
        wrapp("Your ID proudly states that you're 46 now!")
        wrapp("Beside it is your house key.")
    if cmd == "ADDGOLD":
        gold = int(input("Gold new total? "))
    if cmd == "DEVROUTE":
        wrapp("DEVROUTE: debugged by Noam")
        wrapp(
            "WARNING: if you tp to a room that does not exist you get trapped in the eternal void of space"
        )
        print("You are currently in room " + str(storyProg["roomID"]))
        storyProg["roomID"] = int(input("RoomID? "))
        print("Teleporting to " + str(storyProg["roomID"]) + "...")
        if storyProg["roomID"] == 420:
            print("blaze dude")

    if cmd[:9] == "DEVROUTE(":
        wrapp("DEVROUTE: debugged by Noam")
        wrapp(
            "WARNING: if you tp to a room that does not exist you get trapped in the eternal void of space"
        )
        print("You are currently in room " + str(storyProg["roomID"]))
        tempStor = cmd[9:]
        storyProg["roomID"] = int(tempStor[:-1])
        print("Teleporting to " + str(storyProg["roomID"]) + "...")
        if storyProg["roomID"] == 420:
            print("blaze dude")

    if cmd == "BACKPACK" and "BACKPACK" in inventory:
        wrapp("Your backpack!")
        wrapp(
            "Made by Gertrude from Dad's old bottomless bag and two leather straps, it's able to carry anything at all while leaving your hands free to do whatever! It can fit a wallet, a wardrobe, and even a whale! The power of magic is amazing!"
        )

    if cmd == "MAGIC SWORD" and "MAGIC SWORD" in inventory:
        wrapp("A magic sword. Useful for heroes and the adventuring type, but quite unwieldy. Made by the blacksmith on commission, but the commissioner never returned to pick up the sword. That's what happens to heroes...")

    if cmd == "MAGIC WAND" and "MAGIC WAND" in inventory:
      wrapp("A magic wand from a far-off realm. Or so the Blacksmith claims. It glows a little, but you vaguely remember the guard complaining about his old lance being reused in a project.")

    if cmd == "RIDDLER'S FLASK" and "RIDDLER'S FLASK" in inventory:
        wrapp("An item given to the Smith by a passing traveller. Used often in deserts like the mythical Sahara, at least according to the traveller. The smith did his own investigation, and found that the item was cursed to never relieve thirst while containing infinite liquid. Really only useful for looking nice.")

    if cmd == "MOM'S SANDWICH" and "MOM'S SANDWICH" in inventory:
        wrapp("A homemade sandwich from mom.")
        wrapp("A lot of love was put into this.")
    return cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory


def talkwhat(cmd, TalkOptions):
    if TalkOptions == []:
        wrapp("Awkward silence reigns. Somehow you have no talking options.")
        wrapp("I'd report this to your local gamedev.")
        cmd = input("What do say? ").upper()
        lbreak()
    else:
        for i in range(len(TalkOptions) - 1):
            print(end="(")
            print(TalkOptions[i][:1], end="")
            print(end=")")
            print(TalkOptions[i][1:], sep=', ', end=", ")
        print(end="(")
        print(TalkOptions[-1][:1], end="")
        print(end=")")
        print(TalkOptions[-1][1:])
        cmd = input("What do you say? ").upper()
        lbreak()
    return cmd

def tutorialWhat(cmd, avail_locs, inventory, room_objs, storyProg, gold, textSpeedGLOBAL, textWidthGLOBAL, name):
  print("Here are your options:")
  print("(T)RAVEL | (A)CT | MENU")
  cmd = input("What do you do? ").upper()
  lbreak()
  TIA = 0
  while TIA == 0:
    while cmd == "MENU":
            print("SAVE, LOAD, SETTINGS, QUIT")
            cmd = input("What do you do? ").upper()
            lbreak()
    while cmd == "TRAVEL" or cmd == "T":
      for location in range(len(avail_locs) - 1):
          print(end="(")
          print(avail_locs[location][:1],end="")
          print(end=")")
          print(avail_locs[location][1:], sep=', ', end=", ")
      print(end="(")
      print(avail_locs[-1][:1],end="")
      print(end=")")
      print(avail_locs[-1][1:])
      cmd = input("What do you do? ").upper()
      lbreak()
    while cmd == "ACT" or cmd == "A":
      if room_objs == []:
                print("Nothing here is interactable.")
                print("Try TRAVELling!")
      else:
        for Item in range(len(room_objs) - 1):
            print(end="(")
            print(room_objs[Item][:2], end="")
            print(end=")")
            print(room_objs[Item][2:], sep=', ', end=", ")
        print(end="(")
        print(room_objs[-1][:2], end="")
        print(end=")")
        print(room_objs[-1][2:])
      cmd = input("What do you do? ").upper()
      lbreak()
    if cmd != "ACT" and cmd != "A" and cmd != "T" and cmd != "TRAVEL":
      TIA = 1
    if cmd == "SETTINGS":
      textSettings()
    if cmd == "ADDGOLD":
      gold = int(input("Gold new total? "))
    if cmd == "SAVE":
        save(storyProg, gold, inventory)
    if cmd == "LOAD":
        storyProg, gold, inventory = load(storyProg, gold, inventory)
    if cmd == "QUIT":
        wrapp("Are you sure you would like to quit?")
        cmd = yesno(cmd)
        if cmd == "YES" or cmd == "Y":
            exit()
  return cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory

def addRemove(item, inventory, room_objs):
    inventory.append(item)
    room_objs.remove(item)

def talklist():
    wrapp("Here are your options: ")

def yesno(cmd):
    talklist()
    wrapp("(Y)ES, (N)O")
    cmd = input("What do you say? ").upper()
    return cmd

roomID = 0