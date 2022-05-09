from EnJinn.comnd import lbreak, optlist, what, cmd, inventory, talkwhat, gold, textSpeedGLOBAL, textWidthGLOBAL, name, tutorialWhat, addRemove, talklist, yesno, textSettings, wrapp, shop, cashier, addInv, instaWrapp, vardef, wip

import string

from EnJinn.comnd import textInit

import sys
settings = sys.argv

localSpeed = settings[1]
localWidth = settings[2]

textInit(localSpeed, localWidth)

import json

skipProlg = 0

game = 1

storyProg = {}

varlist = [
    "caseyBug1", "tutDone", "roomID", "backpackCheck", "talkwizcheck",
    "momGreet", "bedroomIntro", "lowerTownIntro", "gertieGreet", "wizToTabbs",
    "tempTextStore", "ladybugdiscuss", "smithIntro", "oldManIntroTreeside",
    "presentCount", "CHouseintro", "LukeTalk", "room7intro", "oldManinCHouse",
    "wellIntro", "age", "tabbsChambIntro"
]

storyProg = vardef(storyProg, varlist)

storyProg.update({"roomID": 100})

goodName = 1

prologue = 1
if prologue == 1:
    #Prologue text.
    wrapp("Welcome to Tabbs.")
    wrapp("This is a text-based adventure game.")
    wrapp(
        "If you wish to learn more about how to play the game, please type HELP or H now. If you have a save file already stored, type LOAD to get into the game instantly. If you would like to edit display settings, type SETTINGS or S. Type anything but HELP, H, LOAD, SETTINGS, or S to keep playing."
    )
    settingsSet = 0
    yeetBye = input(">").upper()
    if yeetBye == "HELP" or yeetBye == "H":
        wrapp("Type HELP once more to gain the assistance you so desire.")
        exit()
    elif yeetBye == "SETTINGS" or yeetBye == "S":
        textSettings()
        goodName = 0
        wrapp("Your settings are in order?")
        wrapp("Very good, player...")
        wrapp("Very organized.")
        wrapp("Player...")
    elif yeetBye == "LOAD":
        print("Loading...")
        with open('data.txt') as json_file:
            saveFileContent = json.load(json_file)
            storyProg, gold, inventory = saveFileContent
        print("Load complete!")
        skipProlg = 1
        name = storyProg["name"]
    elif yeetBye == "CUSTLOAD":
        print("Copy/paste your save file below:")
        custfile = input()
        saveFileContent = json.loads(custfile)
        storyProg, gold, inventory = saveFileContent
        skipProlg = 1
        name = storyProg["name"]
    else:
        goodName = 0
        wrapp("Good.")
        wrapp("You have chosen well.")
        wrapp("Player...")
    while goodName == 0:
        name = input("What is your name? ")
        name = string.capwords(name)
        if name == "Casey":
            wrapp(
                "Sorry! But, uh, that's kinda my name! Kinda in-use here! So, um, if you could pick another one?"
            )
        if name == "Mom":
            wrapp(
                "Sweetie, it's nice that you love me that much but I'm not ready to be a grandmother."
            )
            wrapp("Can you pick a different name, for my sake?")
        if name == "Vimm":
            wrapp(
                "For the sake of the timestream, I cannot allow you to have this name."
            )
            wrapp("Pick a different one.")
        if name == "Gertrude":
            wrapp(
                "You wanna take my name? Come and fight me for it! I may be old, but I'm not incapable!"
            )
            wrapp(
                "...Ah, I'm just messing with you. If you really feel strongly about keeping it, you can."
            )
            wrapp(
                "Do you want to share a name with me, kiddo? Just type YES or NO, I can wait. "
            )
            answ = input("What do you say? ").upper()
            if answ == "YES" or answ == "Y":
                wrapp(
                    "Well, remember, if this gets confusing, it's entirely your fault, Gertrude Junior!"
                )
                name = "Gertrude Jr."
                goodName = 1
            else:
                wrapp("Thought so. Pick a different one, then, okay?")
        if name == "Dad":
            instaWrapp(" File \"Tabbs.py\", line ERROR")
            instaWrapp("   ERROR.ERROR(ERROR)")
            instaWrapp(
                "NameError: Cannot select this name. Do not select this name.")
            instaWrapp("Returning to game selection...")
            exit()
        if name == "Tabbs":
            wrapp("Silly...")
            wrapp("You can't take Tabbs's name...")
            wrapp("Pick something elssse.")
        if name == "Jai":
            wrapp("The true name.")
            #wrapp("Unfortunately, already taken...")
        if name == "":
            wrapp("Please, enter your name.")
        if name == "Luke":
            wrapp(
                "Yeesh, this is awkward. Can I ask you to pick a different name?"
            )
        if name == "Def":
            wrapp("...?")
            wrapp("SERIOUSLY?")
            wrapp("CHOOSE ANOTHER NAME.")
        if name == "Monty":
            wrapp("...Hah! You want to take my name! That's funny! That's...")
            wrapp("...you're serious, aren't you?")
            wrapp(
                "Okay, um. I have to tell you that you can't take my name. Pick another."
            )
        if name == "Sebestos":
            wrapp("...weird choice, but okay.")
        if name != "Tabbs" and name != "Casey" and name != "Mom" and name != "Vimm" and name != "Dad" and name != "Gertrude" and name != "" and name != "Luke" and name != "Monty" and name != "Def":
            goodName = 1
        lbreak()
    if skipProlg == 0:
        wrapp("Your name is " + name + ".")
        wrapp("Your best friend, Casey, is [     ].")
        wrapp("Now awaken, Chosen, and face your fate...")
        lbreak()
        wrapp("You wake up, rolling out of bed.")
        wrapp(
            "Yawning, you stretch, making a bit of a silly noise as you do so."
        )
        wrapp("Yesterday was your twelfth birthday!")
        wrapp(
            "You were a little disappointed Casey wasn't able to show up to the celebrations, though."
        )
        wrapp(
            "You take stock of your surroundings as the last remnants of sleep leave your eyes."
        )
storyProg.update({"name": name})

while game == 1:
    while storyProg["roomID"] == 100:
        lbreak()
        avail_locs = ["DOWNSTAIRS"]
        room_objs = ["BED", "PRESENTS", "WINDOW"]
        wrapp("You are in your bedroom.")
        if storyProg["bedroomIntro"] == 0:
            wrapp(
                "Your bedroom is filled with unwrapped presents from your birthday yesterday, with one from nearly everyone in town. Some of the presents glow from obvious enchantment, others whirr, the mechanical parts making a pleasant buzz that had lulled you to sleep last night. A few of them just look nice."
            )
            wrapp(
                "Hanging on the wall is a wooden sword, firmly bolted into the plaster. Your dad gave that to you when you were six, before he had to leave."
            )
            storyProg.update({"bedroomIntro": 1})
        wrapp("Behind you is your bed, warm and comfy.")
        wrapp("Your window is to your side.")
        if storyProg["caseyBug1"] == 0:
            wrapp("Wandering around on the windowsill is a small ladybug.")
            room_objs.append("LADYBUG")
        if storyProg["caseyBug1"] == 1:
            wrapp("The ladybug is no longer in your room.")
            room_objs.append("SILL")
        if "BACKPACK" not in inventory:
            cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = tutorialWhat(
                cmd, avail_locs, inventory, room_objs, storyProg, gold,
                textSpeedGLOBAL, textWidthGLOBAL, name)
        else:
            optlist()
            cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
                cmd, avail_locs, inventory, room_objs, storyProg, gold,
                textSpeedGLOBAL, textWidthGLOBAL, name)

        if cmd == "LADYBUG" and storyProg[
                "caseyBug1"] == 0 or cmd == "LA" and storyProg[
                    "caseyBug1"] == 0:
            wrapp("You stare at the ladybug.")
            wrapp(
                "The ladybug, once it notices your staring, flies away through the window."
            )
            wrapp("The ladybug is free.")
            storyProg.update({"caseyBug1": 1})
        if cmd == "SILL" and storyProg[
                "caseyBug1"] == 1 or cmd == "SI" and storyProg[
                    "caseyBug1"] == 1:
            wrapp(
                "You look at the spot on the windowsill where the ladybug was."
            )
            wrapp("You feel an odd mix of sadness and elation.")
            wrapp("You hope the bug made it out okay.")
        elif cmd == "WINDOW" or cmd == "WI":
            wrapp(
                "You lean your head out the window and look out over town. From your vantage point, you have an overhead view of Wellside; you can see old Gertrude knitting, you can see the blacksmith chatting with his husband, and if you squint, you can make out Casey's house near Treeside."
            )
            wrapp(
                "Unfortunately, your view isn't good enough to make out many details of what's going on near Treeside; the fact that Treeside is on a hill means that your angle is bad."
            )
        elif cmd == "PRESENTS" or cmd == "PR":
            if storyProg["presentCount"] == 0:
                wrapp(
                    "You look at your presents. Five in total, one from nearly everyone in town!"
                )
            storyProg["presentCount"] = storyProg["presentCount"] + 1
            if storyProg["presentCount"] == 1:
                wrapp(
                    "From the blacksmith, you got a small mechanical dragonfly. It's been whirring softly all night, and the machinery acted like a lullaby when you went to bed. You think you might keep it on."
                )
            if storyProg["presentCount"] == 2:
                wrapp(
                    "From the guard, you got a helmet. It's too big for you, but he says that since his husband made it, it's guaranteed to fit someday. You weren't sure if that was a reference to the blacksmith's skill with magic or the size of your head."
                )
            if storyProg["presentCount"] == 3:
                wrapp(
                    "From Gertrude, you got a beautiful sweater. Genuinely one of the nicest pieces of clothing you own."
                )
                wrapp(
                    "Times like these you realize she isn't the town seamstress for nothing."
                )
            if storyProg["presentCount"] == 4:
                wrapp(
                    "From Casey's family, you got a hand drawn picture book of you and Casey being evil-smiting dragon slayers, Casey with a sword and you with a shield."
                )
                wrapp(
                    "It's the best present you've ever recieved. You just wish you could have told Casey that in person."
                )
                wrapp("For now, her dad said he would pass along the message.")
            if storyProg["presentCount"] == 6:
                wrapp(
                    "From mom, you got a sapphire orb, shimmering with power. Your mom had it enchanted so that if you snapped your fingers, it would glow blue. If you snapped again, it would shut off."
                )
                wrapp(
                    "So much more convenient than having to walk and manually turn the power on and off!"
                )
            if storyProg["presentCount"] == 5:
                wrapp(
                    "The old man didn't show up yesterday, so you didn't get anything from him."
                )
                wrapp(
                    "If you were being honest with yourself, you didn't expect to recieve anything."
                )
            if storyProg["presentCount"] == 7:
                wrapp(
                    "You stare at the presents again. Yup, they're all still there."
                )
                storyProg["presentCount"] = 6
            elif storyProg["presentCount"] < 6:
                wrapp("There are still more presents!")
        elif cmd == "BED" or cmd == "BE":
            wrapp("You glance at your bed longingly.")
            wrapp("But you still have a full day ahead of you!")
        elif cmd == "DOWNSTAIRS" or cmd == "D":
            wrapp("You walk downstairs into the family room.")
            if storyProg["tutDone"] == 0:
                storyProg.update({"roomID": 101})
            if storyProg["tutDone"] == 1:
                storyProg.update({"roomID": 2})
    while storyProg["roomID"] == 101:

        lbreak()
        avail_locs = ["UPSTAIRS", "OUTSIDE"]
        room_objs = ["MOM", "BACKPACK"]
        wrapp("You are downstairs in your home.")
        wrapp("Your mom is sitting at the kitchen table.")
        if storyProg["momGreet"] == 0:
            wrapp("She notices your approach.")
            wrapp("\"" + name + "! Good morning, sleepyhead!\"")
            storyProg.update({"momGreet": 1})
        else:
            wrapp("She has made herself some tea.")

        if "BACKPACK" not in inventory:
            cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = tutorialWhat(
                cmd, avail_locs, inventory, room_objs, storyProg, gold,
                textSpeedGLOBAL, textWidthGLOBAL, name)

        elif "BACKPACK" in inventory:
            optlist()
            room_objs.remove("BACKPACK")
            cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
                cmd, avail_locs, inventory, room_objs, storyProg, gold,
                textSpeedGLOBAL, textWidthGLOBAL, name)

        if cmd == "OUTSIDE" and "BACKPACK" not in inventory and storyProg[
                "backpackCheck"] == 0 or cmd == "O" and "BACKPACK" not in inventory and storyProg[
                    "backpackCheck"] == 0:
            wrapp("\"Wait!\" shouts your mom.")
            wrapp(
                "\"Sweetheart, you forgot your backpack. I'll feel better if you have it.\""
            )
            storyProg.update({"backpackCheck": 1})

        elif cmd == "OUTSIDE" and "BACKPACK" not in inventory and storyProg[
                "backpackCheck"] == 1 or cmd == "O" and "BACKPACK" not in inventory and storyProg[
                    "backpackCheck"] == 1:
            wrapp("\"Just pick up your backpack, okay " + name + "?\"")

        elif cmd == "MOM" and storyProg[
                "talkwizcheck"] == 1 or cmd == "MO" and storyProg[
                    "talkwizcheck"] == 1:
            wrapp("\"Remember, don't talk to the old man!\" says your mom.")
            if "BACKPACK" not in inventory:
                wrapp("\"And don't forget your backpack!\"")
            wrapp("\"Have a great day!\"")

        elif cmd == "MOM" and storyProg[
                "talkwizcheck"] == 0 or cmd == "MO" and storyProg[
                    "talkwizcheck"] == 0:
            wrapp("Your mom smiles at you.")
            wrapp(
                "\"Well, sweetie, I hope you know I let you sleep in,\" she says."
            )
            wrapp(
                "\"Don't expect this to be a frequent thing, though! I'm just being lenient because yesterday was your birthday.\""
            )
            wrapp("\"Anyway. Anything you wanted to talk about?\"")
            convoTree = 1
            TalkOptions = ["CASEY", "BACKPACK", "LADYBUG", "NO"]
            talklist()
            cmd = talkwhat(cmd, TalkOptions)
            while convoTree == 1:
                if cmd == "CASEY" and "CASEY" in TalkOptions or cmd == "C" and "CASEY" in TalkOptions:
                    wrapp("Your mother frowns.")
                    wrapp(
                        "\"Sweetheart, I know you're disappointed she couldn't come yesterday, but her dad said she was really sick!\""
                    )
                    wrapp(
                        "\"I haven't seen them yet today. They're probably still at home, that family wakes up late in general. Want me to pass on well-wishes?\""
                    )
                    cmd = yesno(cmd)
                    if cmd == "YES" or cmd == "Y":
                        wrapp("\"Alright, I'll do that.\"")
                    elif cmd == "NO" or cmd == "N":
                        wrapp(
                            "\"Oh! I'm sure, then, you'll do it in person!\"")
                    else:
                        wrapp(
                            "She looks at you for a second, before saying, \"I'll just do it myself, then. I'll probably see them later.\""
                        )
                    TalkOptions.remove("CASEY")
                    cmd = "a"
                elif cmd == "BACKPACK" and "BACKPACK" in TalkOptions or cmd == "B" and "BACKPACK" in TalkOptions:
                    wrapp(
                        "\"Thank you for reminding me! I meant to give you a snack for today, but it totally slipped my mind.\""
                    )
                    wrapp(
                        "Your mom gets up from the table, runs into the kitchen, and grabs a small pouch. She stuffs this into your backpack before sitting back down."
                    )
                    addInv(inventory, "MOM'S SANDWICH")
                    wrapp(
                        "\"Be careful with that backpack,\" she says. \"I don't want you to bring it home ripped again. One of these days the enchantments on it are flat out going to stop working, and everything you've ever put in there is just going to fly right out!\""
                    )
                    TalkOptions.remove("BACKPACK")
                    cmd = "a"
                elif cmd == "LADYBUG" and "LADYBUG" in TalkOptions or cmd == "L" and "LADYBUG" in TalkOptions:
                    wrapp("\"You saw a ladybug in your room?\" asks your mom.")
                    if storyProg["caseyBug1"] == 0:
                        wrapp(
                            "\"And it's still up there? You should actually go and see if you can get it to land on your hand. That's supposed to be good luck.\""
                        )
                        wrapp(
                            "Just as she says that, you notice the lazy flight of the ladybug coming down the stairs. It hovers right between you and your mom, bobbing up and down slightly in the air, flying a straight path right to the door."
                        )
                        wrapp("The ladybug is free.")
                        storyProg.update({"caseyBug1": 1})
                        wrapp(
                            "Your mom looks back at you. \"Well, I would have liked to have it land on my hand, but it doesn't look like that's possible anymore,\" she says with a wry smile."
                        )
                    elif storyProg["caseyBug1"] == 1:
                        wrapp(
                            "\"Oh, it's gone? That's a bit of a shame. I was going to tell you that if it lands on your hand it's good luck, but it doesn't look like that would have happened.\""
                        )
                    cmd = "a"
                    TalkOptions.remove("LADYBUG")
                elif cmd == "NO" or cmd == "N":
                    wrapp("\"That's alright!\"")
                    wrapp(
                        "Your mom seems to remember something. She hesitates before beginning, \"Oh, the old man wanted to speak to you."
                    )
                    wrapp(
                        "\"I don't know what he wanted. Frankly, I don't care to find out. "
                        + name + ", can you promise me something?\"")
                    cmd = yesno(cmd)
                    if cmd == "NO" or cmd == "N":
                        wrapp(
                            "\"Well, this is important, so I'm going to make you promise anyway.\""
                        )
                    wrapp(
                        "\"I don't want you going near him. Do that one thing for me. Please, for my sake and yours.\" Her tone is somber."
                    )
                    wrapp(
                        "She tries to smile, but you can tell she's worried, even as she says, \"Anyway, have a great day!\" as she waves you off."
                    )
                    convoTree = 0
                    storyProg.update({"talkwizcheck": 1})
                else:
                    wrapp(
                        "Your mom doesn't understand what you meant by that.")
                    talklist()
                    cmd = talkwhat(cmd, TalkOptions)
                if cmd == "a":
                    wrapp("\"Anything else you want to talk about?\"")
                    talklist()
                    cmd = talkwhat(cmd, TalkOptions)
        #End mom conversation tree

        elif cmd == "BACKPACK" and "BACKPACK" not in inventory or cmd == "BA" and "BACKPACK" not in inventory:
            wrapp("You put your dad's old enchanted bottomless bag on.")
            wrapp("A while ago, Gertrude had sewn straps onto it.")
            wrapp(
                "At the time, she had said: \"Put it on your back, and it's not quite a sack! It's a backpack!\""
            )
            wrapp("Gertrude is weird, but she sews a good backpack.")
            addRemove("BACKPACK", inventory, room_objs)

        elif cmd == "UPSTAIRS" or cmd == "U":
            wrapp("You climb back upstairs to your room.")
            storyProg.update({"roomID": 100})

        elif cmd == "OUTSIDE" and "BACKPACK" in inventory or cmd == "O" and "BACKPACK" in inventory:
            wrapp("You make your way outside, unlocking the door as you do.")
            if storyProg["caseyBug1"] == 0:
                wrapp(
                    "As you open the front door, the ladybug from your room darts out of the house, flying through the front door."
                )
                wrapp("The ladybug is free.")
                wrapp(
                    "You walk outside for real, following the general direction the ladybug flew."
                )
            storyProg.update({"roomID": 3})

    #The above were the prologue forms of the house rooms.
    #Below are the normal forms.

    while storyProg["roomID"] == 1:
        lbreak()

        avail_locs = ["DOWNSTAIRS"]
        room_objs = ["BED"]
        wrapp("You are in your bedroom.")
        wrapp("Behind you is your bed, warm and comfy.")
        wrapp("Your window is to your side.")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if cmd == "BED" or cmd == "BE":
            wrapp("You glance at your bed longingly.")
            wrapp("But you still have a full day ahead of you!")
        if cmd == "DOWNSTAIRS" or cmd == "D":
            wrapp("You walk downstairs into the family room.")
            storyProg.update({"roomID": 2})

    while storyProg["roomID"] == 2:
        lbreak()
        storyProg.update({"tutDone": 1})
        avail_locs = ["UPSTAIRS", "OUTSIDE"]
        room_objs = ["MOM"]
        wrapp("You are downstairs in your home.")
        wrapp("Your mom notices your approach.")
        wrapp("She is sitting at the kitchen table.")
        wrapp("\"" + name + "! Welcome back!\"")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)

        if cmd == "UPSTAIRS" or cmd == "U":
            wrapp("You climb back upstairs to your room.")
            storyProg.update({"roomID": 100})
        elif cmd == "OUTSIDE" or cmd == "O":
            wrapp("You make your way outside.")
            storyProg.update({"roomID": 3})
        elif cmd == "MOM" or cmd == "MO":
            wrapp("\"Hi, sweetheart!\" says your mom.")
            if "MOM'S SANDWICH" not in inventory:
                wrapp(
                    "She asks, \"Do you want a sandwich? I've got one right here.\""
                )
                wrapp(
                    "Before you can even raise a finger in protest, she shoves it into your ITEMS pouch."
                )
                addInv(inventory, "MOM'S SANDWICH")
            else:
                wrapp("\"I really hope you have a great day!\"")

    while storyProg["roomID"] == 3:
        lbreak()
        avail_locs = [
            "HOME", "SMITHY", "ROAD", "GERTRUDE'S HOUSE", "PATH TO TREESIDE"
        ]
        room_objs = ["GERTRUDE", "WELL"]
        if storyProg["oldManinCHouse"] == 3:
            avail_locs.append("WELL")
            room_objs.remove("WELL")
        wrapp("You are outside, in the half of town known as Wellside.")
        if storyProg["lowerTownIntro"] == 0:
            wrapp("The town center is fairly lively as you look upon it.")
            wrapp(
                "In the center of town is a well, the source of the town's water supply, as well as this half of town's name, Wellside."
            )
            wrapp(
                "Some visitors to your village have complained that your village is too small, and they wondered how anything got done in a town without a sprawling general store or a tavern or something, but you absolutely disagree with that sentiment."
            )
            wrapp(
                "You think that your town is wonderful. Wellside is paved with cobble, connecting all three of the cottages to the small square at the well, where you had your birthday festival yesterday. There's also a path leading to the road."
            )
            wrapp(
                "And the Wellside cottages are always so energized! There's your house, of course, which is where you live. There's the blacksmith's home, which doubles as his workplace. He and his husband, the guard, sleep there. In his workshop, the blacksmith works day and night on new mechanical devices, like the one he gave you for your birthday, as well as old-fashioned swords and shields and the like. You've been there with your mom to pick up commissions, and it's always a fantastic experience. Then there's Gertrude's house, where she does her seamstress and tailor work, as well as magicking up fabric and tools when people need them. You've never been inside, but you're sure it's absolutely magical."
            )
            wrapp(
                "You can also see the guard post, where the guard is... on guard."
            )
            wrapp(
                "Of course, you can see Casey's house and the old man's home up the hill in the upper half of town, which is called Treeside. Treeside is named for the larger-than-average tree that occupies most of the real estate there."
            )
            optlist()
            lolthisisneverused = input("What do you do? ")
            lbreak()
            wrapp(
                "Before you can move to do anything, though, Gertrude, who is sitting by the well knitting, jumps up and shouts at you in greeting."
            )
            if name == "Gertrude Jr.":
                wrapp(
                    "\"Gertie Junior! Little Gertie Junior! Get over here, I have to tell you something!\""
                )
            else:
                wrapp("\"" + name + "! Come over here!\"")
            wrapp(
                "She beckons you over to her, waving and grinning slightly madly."
            )
            storyProg.update({"lowerTownIntro": 1})
        elif storyProg["lowerTownIntro"] == 1:
            if storyProg["oldManinCHouse"] != 99 and storyProg[
                    "oldManinCHouse"] != 3:
                wrapp("Gertrude is knitting.")
                if storyProg["oldManinCHouse"] == 2 or storyProg[
                        "oldManinCHouse"] == 4:
                    wrapp("She is pointedly ignoring the old man.")
                elif storyProg["oldManinCHouse"] == 50:
                    wrapp("Monty turns to you.")
                    wrapp(
                        "\"" + name +
                        ",\" he says. \"The journey we're about to embark on may be long and difficult. We may encounter some terrible challenges, nearly unkillable monsters, or truly evil people. So I want you to prepare yourself by buying something for yourself from the shop in the smithy.\""
                    )
                    wrapp("He hands you 10 gold pieces, which you pocket.")
                    gold = 10
                    wrapp("\"" + name + ", purchase something wisely.\"")
                    wrapp(
                        "\"When you get back from the smithy, I'll give you a road pass, and we'll be on our way.\""
                    )
                    storyProg["oldManinCHouse"] = 4
            elif storyProg["oldManinCHouse"] == 99:
                wrapp(
                    "Gertrude has temporarily stopped her knitting, and is conversing with the old man. Their conversation stops when they see you."
                )
                wrapp(
                    "\"" + name +
                    ",\" says Monty. \"Come here.\" He steps away from Gertude. Gertrude side-eyes him, but says nothing, picking up her yarn and needles."
                )
                storyProg["oldManinCHouse"] = 2
            wrapp(
                "You can hear the slight crackling of the furnace in the smithy behind you, as well as the occasional clang of tools."
            )
            wrapp("The guard is at his post.")
        if storyProg["oldManinCHouse"] == 2 or storyProg["oldManinCHouse"] == 4:
            room_objs.append("OLD MAN")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if cmd == "G" or cmd == "GERTRUDE'S HOUSE":
            wrapp("The door to Gertrude's house is locked.")
            wrapp(
                "Out of the corner of your eye you notice that Gertrude sees you try the knob, but she says nothing."
            )
            wrapp(
                "You could swear you saw her smile slightly, but it was so fast you're not sure you didn't actually imagine it."
            )

        if cmd == "HOME" or cmd == "H":
            wrapp("You walk back into your home.")
            storyProg.update({"roomID": 2})
        if cmd == "SMITHY" or cmd == "S":
            wrapp(
                "You enter the smithy, feeling the slight increase of temperature as you pass the threshold."
            )
            storyProg.update({"roomID": 4})
        if cmd == "ROAD" and "ROAD PASS" not in inventory or cmd == "R" and "ROAD PASS" not in inventory:
            wrapp("You walk towards the road.")
            wrapp(
                "As you approach the guard's post, he asks, \"Do you have a pass to leave town?\""
            )
            wrapp(
                "When you shake your head, he smiles. \"Look, " + name +
                ", I wish I could let you out. But I think your mom would literally kill me, then bring me back to life somehow, then kill me again, just for letting you see the road.\""
            )
            wrapp(
                "He shrugs helplessly. \"But it's out of my hands, really. Sorry, "
                + name + ". Really, I am.\"")

        if cmd == "ROAD" and "ROAD PASS" in inventory and storyProg["oldManinCHouse"] == 5 or cmd == "R" and "ROAD PASS" in inventory and storyProg["oldManinCHouse"] == 5:
            wrapp("You walk towards the road. Monty follows.")
            wrapp(
                "As you approach the guard's post, he asks, \"Do you have a pass to leave town?\""
            )
            wrapp("As a matter of fact, you do. And you show the guard the road pass, waving it in front of you proudly.")
            wrapp("\"Woah, okay. You do have a road pass. Monty give this to you?\"")
            wrapp("You nod.") 
            wrapp("\"Alright, then, " + name + ", head on out. You've got Monty with you, so I trust you'll be okay.\"")
            wrapp("\"I shall return " + name + "safe and sound, I promise,\" says Monty. \"Tell " + name + "'s mother we're heading out. Shouldn't be too long.\"")
            wrapp("The ladybug on your hand flutters its wings slightly.")
            wrapp("\"Okay, then,\" says the guard. The road is now free for your perusal. See you soon!\"")
            wrapp("\"Thank you, Leon,\" says Monty. \"We'll be back before you know it.\"")
            print()
            lbreak()
            print()
            wrapp("Now would be a good time to save, as it will be your last opportunity to return to town for some time. To save, simply type SAVE at any time.")
            wrapp("Would you like to save?")
            cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
            wrapp("To leave town, simply type ROAD once more.")
            storyProg["oldManinCHouse"] = 6
            cmd = ""
        if cmd == "ROAD" and "ROAD PASS" in inventory and storyProg["oldManinCHouse"] == 6 or cmd == "R" and "ROAD PASS" in inventory and storyProg["oldManinCHouse"] == 6:
            wrapp("\"Well,\" says Monty. \"Let's get going.\"")
            wrapp("You follow Monty out of town, the ladybug having migrated to your shoulder. Tabbs peeks out at you from around Monty's cloak, but says nothing.")
            print()
            wrapp("END OF CHAPTER ONE")
            print()
            storyProg["roomID"] = 10
        if cmd == "WELL" and storyProg[
                "oldManinCHouse"] != 3 or cmd == "WE" and storyProg[
                    "oldManinCHouse"] != 3:
            wrapp("You look down the well.")
            wrapp("That's really deep!")
            wrapp(
                "Silently, you make the same wish you made yesterday, when you blew out your candles."
            )
            wrapp("You hope the wish reaches Casey.")
        if cmd == "OLD MAN" and "OLD MAN" in room_objs or cmd == "OL" and "OLD MAN" in room_objs:
            if storyProg["oldManinCHouse"] == 2:
                wrapp("\"" + name +
                      ", you asked to see where Tabbs lived, yes?\"")
                wrapp("You nod.")
                wrapp(
                    "He hesitates for a moment, glancing at Gertrude, but she doesn't react. Then he continues."
                )
                wrapp(
                    "\"She lives in here,\" he says, and for a second you think she's dead and he was going to point to his heart as a metaphor for a person's memory living on after death, but then he gestures towards the well."
                )
                wrapp(
                    "You look down the well. Notably, you don't see anyone, certainly nobody named Tabbs."
                )
                wrapp(
                    "The old man watches you lean over the edge and chuckles. \"She's deeper down,\" he says. \"There's a tunnel, and you have to climb a magic ladder on the way down. I'll activate it for you.\""
                )
                wrapp(
                    "The old man taps his staff against the side of the well and a small, blue spark comes out of the tip. It swirls about in the center of the well for a moment, before abruptly dropping. As it falls, it splits sparks off of itself, which attach to the wall of the well and grow to form glowing, blue handhelds."
                )
                wrapp(
                    "With practiced, smooth movement, the old man vaults himself over the edge of the wall and climbs down the glowing ladder."
                )
                wrapp("Halfway to the bottom, you hear the old man shout, \"" +
                      name + "! Are you coming down or what? \"")
                storyProg["oldManinCHouse"] = 3
            elif storyProg["oldManinCHouse"] == 4:
                wrapp("The old man turns around when you approach him.")
                wrapp("\"Well, " + name +
                      "? Have you gone to the smith yet?\"")
                if storyProg["smithIntro"] == 1:
                    wrapp("You honestly tell him yes.")
                    wrapp("\"Good!\" he says. \"Did you buy anything?\"")
                    if "RIDDLER'S FLASK" in inventory:
                        wrapp("You repeat your affirmation.")
                        wrapp("\"Wonderful!\" he says.")
                    else:
                        wrapp(
                            "\"...that's fine, I guess,\" says Monty. \"That you didn't buy anything. Shows confidence. Which you'll need.\""
                        )
                    wrapp(
                        "\"Anyway, I've made nearly all my preperations. So we can get going as soon as I...\""
                    )
                    wrapp(
                        "As he talks, you notice the ladybug from earlier flying around behind Monty. You zone out a little, staring straight at the ladybug. It flies in a lazy circle, wings beating hundreds of times every few seconds. The ladybug makes its way past the snake on Monty's neck, who lifts her head and sticks out her tongue briefly in its direction, but the ladybug doesn't fly close enough to Tabbs to truly be in danger."
                    )
                    wrapp(
                        "On instinct, you turn your palm up. If the ladybug landed on your hand, that was good luck, right?"
                    )
                    wrapp(
                        "The ladybug hovers above your palm for a moment before slowly lowering itself down. You don't move a muscle."
                    )
                    wrapp(
                        "You stare at the ladybug's carapace. Six black spots, exactly three on both sides. They each form a rough triangle, both ends pointing towards each other."
                    )
                    wrapp("The ladybug slowly begins crawling up your arm.")
                    wrapp(
                        "\"...so if we want to make it to Bashapt before sundown tomorrow, we're going to have to really start moving. "
                        + name + "? What do you think of that plan?\"")
                    wrapp(
                        "You blink, looking up at Monty. You nod, hoping the movement wouldn't disturb the ladybug."
                    )
                    wrapp("\"Perfect,\" he says. \"Here, " + name +
                          ". Take this road pass.\"")
                    addInv(inventory, "ROAD PASS")
                    wrapp("\"Let's go, " + name +
                          ". We're heading out to the road.\"")
                    storyProg["oldManinCHouse"] = 5
                    wrapp(
                        "You look back at your palm, but the ladybug is gone. You panic silently for a moment, worried that you've hurt the ladybug, until you feel a tickling near your ear."
                    )
                    wrapp(
                        "You crane your neck just enough to be able to see that the ladybug has landed on your shoulder."
                    )
                    wrapp("...huh. Okay.")
                else:
                    wrapp("You tell him no.")
                    wrapp("\"Well, you probably should do that,\" he says.")
                    wrapp(
                        "He then turns around and proceeds to ignore you, cracking open his spellbook."
                    )
            elif storyProg["oldManinCHouse"] == 5:
              wrapp("\"Go on, then,\" says Monty. \"Talk to the guard, he'll let us out.\"")
        if cmd == "WELL" and "WELL" in avail_locs or cmd == "W" and "WELL" in avail_locs:
            wrapp("Very, very carefully, you make your way down the well.")
            storyProg["roomID"] = 8
        if cmd == "PATH TO TREESIDE" or cmd == "P":
            wrapp("You clamber up the hilly path towards Treeside.")
            storyProg.update({"roomID": 5})
        if cmd == "GERTRUDE" and storyProg[
                "gertieGreet"] == 0 or cmd == "GE" and storyProg[
                    "gertieGreet"] == 0:
            wrapp(
                "\"Well, if it isn't " + name +
                "! How does it feel being twelve? Different? Unique? Are you suddenly, instantly, wiser and more mature?\""
            )
            wrapp(
                "She gives you a toothy grin. \"You probably feel mostly the same, right? Well, that's aging for you! One day you're twelve, you don't feel anything different, and before you know it you're the rich age of I-don't-even-remember!\""
            )
            if storyProg["oldManinCHouse"] != 2 or storyProg[
                    "oldManinCHouse"] != 4 or storyProg["oldManinCHouse"] != 3:
                wrapp(
                    "\"Oh! And I forgot to tell you, but the old man asked me to tell you to see him. He's near the lookout at Treeside, where he usually is.\""
                )
            wrapp("\"Well, birthday kid? Anything you wanted to talk about?\"")
            convoTree = 1
            TalkOptions = ["OLD MAN", "CASEY", "LADYBUG", "NO"]
            talklist()
            cmd = talkwhat(cmd, TalkOptions)
            while convoTree == 1:
                if cmd == "OLD MAN" and "OLD MAN" in TalkOptions or cmd == "O" and "OLD MAN" in TalkOptions:
                    if storyProg["oldManinCHouse"] == 2 or storyProg[
                            "oldManinCHouse"] == 4:
                        wrapp(
                            "\"...Monty and I go way back,\" she says after some hesitation, avoiding eye contact with him. \"But I won't bore you with the details. Long story short, we had a falling out before you were old enough to remember.\" She shakes her head. \"It's ancient history now.\""
                        )
                    elif storyProg["oldManinCHouse"] == 3:
                        wrapp(
                            "\"The crazy coot just jumped down a well, kid. I think that's all the information you really need about him.\""
                        )
                    else:
                        wrapp(
                            "\"The old man? Monty? Sorry, kid, but I don't really remember what he wanted you for.\""
                        )
                        wrapp(
                            "\"He did seem pretty antsy, though. If I were you I'd head over there ay-ess-ay-pee.\""
                        )
                    cmd = "a"
                    TalkOptions.remove("OLD MAN")
                    if storyProg["talkwizcheck"] == 1:
                        TalkOptions.append("MOM")
                    TalkOptions.remove("NO")
                    TalkOptions.append("NO")
                if cmd == "MOM" and "MOM" in TalkOptions or cmd == "M" and "MOM" in TalkOptions:
                    wrapp(
                        "Getrude looks surprised. \"Your mom really made you promise not to go near Monty? That's... I'm not even sure how to react to that, if I'm being honest, "
                        + name + ".\"")
                    wrapp(
                        "Gertrude strokes her chin. \"Now, if you were to ask me, which you did, what you should do... hmm... Well, look at it this way! You've known the old man since before you were born! He's been trustworthy all your life.\""
                    )
                    wrapp(
                        "\"In my opinion, your mom's probably a little overprotective. Seeing your kid turn twelve does that to a mom. Not that I know from experience.\""
                    )
                    TalkOptions.remove("MOM")
                    cmd = "a"
                if cmd == "CASEY" and "CASEY" in TalkOptions or cmd == "C" and "CASEY" in TalkOptions:
                    wrapp(
                        "Gertrude shrugs, her bony shoulders rising. \"Haven't seen her or her father today, yet. They're probably at home.\""
                    )
                    TalkOptions.remove("CASEY")
                    cmd = "a"
                if cmd == "LADYBUG" and "LADYBUG" in TalkOptions or cmd == "L" and "LADYBUG" in TalkOptions:
                    if storyProg["ladybugdiscuss"] == 0:
                        wrapp(
                            "\"You saw a ladybug?\" asks Gertrude, wide-eyed. \"That's... wow. I haven't seen a ladybug in decades. You must be really lucky!\""
                        )
                        cmd = "a"
                        storyProg.update({"ladybugdiscuss": 1})
                    else:
                        wrapp(
                            "\"What's the significance of the ladybug? Why are you asking me that? I'm just the town's old seamstress, I don't know anything about the symbolic importance of the ladybug.\""
                        )
                        cmd = "a"
                        TalkOptions.remove("LADYBUG")
                if cmd == "NO" or cmd == "N":
                    if "OLD MAN" in TalkOptions or "MOM" in TalkOptions or "LADYBUG" in TalkOptions or "CASEY" in TalkOptions:
                        wrapp(
                            "\"Oh, that's alright! I don't expect youngsters like yourself to want to talk to weird old women for long anyway.\""
                        )
                    else:
                        wrapp(
                            "\"Well, that's alright! Thanks for entertaining me, kiddo. Not a lot of youngsters talk to weird old women for long, so I'm glad you did.\""
                        )
                    if storyProg["oldManinCHouse"] == 2:
                        wrapp(
                            "\"I think Monty is looking a little anxious, though. Talk to him!\""
                        )
                    if storyProg["oldManinCHouse"] != 4 or storyProg[
                            "oldManinCHouse"] != 3 or storyProg[
                                "oldManinCHouse"] != 2:
                        wrapp(
                            "\"Remember, the old man's up the hill, near the lookout!\""
                        )
                    convoTree = 0
                    storyProg.update({"gertieGreet": 1})

                if cmd == "a":
                    wrapp("\"Anything else you want to talk about, kiddo?\"")
                    talklist()
                    cmd = talkwhat(cmd, TalkOptions)
                if cmd != "CASEY" and cmd != "MOM" and cmd != "OLD MAN" and cmd != "LADYBUG" and cmd != "NO" and cmd != "C" and cmd != "M" and cmd != "O" and cmd != "L" and cmd != "N" and cmd != "a":
                    wrapp(
                        "Gertrude doesn't understand what you meant by that.")
                    talklist()
                    cmd = talkwhat(cmd, TalkOptions)
        if cmd == "GERTRUDE" and storyProg[
                "gertieGreet"] == 1 or cmd == "GE" and storyProg[
                    "gertieGreet"] == 1:
            wrapp(
                "Gertrude shrugs apologetically. \"Sorry, kiddo, but if you're looking for more lore, you're not gonna find it with me. That's the old man's job!\""
            )
            if storyProg["oldManinCHouse"] == 2:
                wrapp(
                    "She glares very pointedly at the old man. He ignores her."
                )
            if "OLD MAN" in TalkOptions or "MOM" in TalkOptions or "LADYBUG" in TalkOptions or "CASEY" in TalkOptions:
                wrapp(
                    "She shakes her head. \"This is what happens when you don't talk to me as long as you possibly can, kid! The terrible feeling of missing out!\""
                )

    while storyProg["roomID"] == 4:
        lbreak()

        avail_locs = ["OUTSIDE", "LIVING QUARTERS"]
        room_objs = ["SHOP"]
        wrapp("You are in the smithy workshop.")
        if storyProg["smithIntro"] == 0:
            wrapp(
                "The smithy has two parts; the workshop, and the living quarters."
            )
            wrapp(
                "The workshop is littered with unfinished experiments; you notice the table littered with scrapped ideas for mechanical dragonflies, sword hilts, and what you think were supposed to be pieces of armor. Some of them glow faintly, a sign of the strengthening magic setting."
            )
            wrapp(
                "There is a large stone furnace with multiple layers, so that the blacksmith can put many projects in at once. You notice that two of three layers are currently in use."
            )
            wrapp(
                "Behind the workshop is a door leading to the living quarters that the blacksmith shares with the guard."
            )
            wrapp(
                "As he notices you enter, the smith, black-bearded and broad-shouldered, greets you jovially."
            )
            wrapp(
                "\"" + name +
                "! Good morning! How did you like my gift from yesterday? Did the dragonfly work as I hoped it did?\""
            )
            TalkOptions = ["LIKED IT", "DIDN'T USE IT"]
            talklist()
            cmd = talkwhat(cmd, TalkOptions)
            if cmd == "L" or cmd == "LIKED IT":
                wrapp(
                    "\"Glad to hear it! I put a lot of work into that little mechanical guy.\""
                )
            elif cmd == "D" or cmd == "DIDN'T USE IT":
                wrapp(
                    "\"Well, that's a bit of a shame, but there's always tomorrow.\""
                )
            else:
                wrapp("\"I'm... not entirely sure what you meant by that?\"")
            wrapp(
                "\"Anyway, kid, what are you doing here without your mom? You're lucky I'm taking a break right now, I could have been doing something dangerous.\""
            )
            TalkOptions = ["CURIOUS", "NOT SURE"]
            talklist()
            cmd = talkwhat(cmd, TalkOptions)
            if cmd == "C" or cmd == "CURIOUS":
                wrapp(
                    "The smith chuckles. \"Well, I could spend all day explaining how exactly I managed to create the dragonfly, mixing mechanical parts with an ambient magic crystal-based battery system, but I'm sure that would bore you. I'm guessing you secretly just want to see my shop?"
                )
            else:
                wrapp(
                    "The smith makes an exaggerated thinker pose. \"Well, what could possibly excite a child's imagination so much that they would be drawn to a smithy? Is it the pure joy of creation? Could it be the wonder of seeing brilliant new inventions as they're created? Or is it possibly the simple fact that I tend to shower you with gifts from my shop every time you come? It's the last one, isn't it?\""
                )
            cmd = yesno(cmd)
            if cmd == "Y" or cmd == "YES":
                wrapp("\"I knew it! I'll get it ready for you right now.\"")
            else:
                wrapp(
                    "\"Playing coy, are you?\" he asks. \"Well, I 'won't' get it for you,\" he says. Then he winks. Vigorously."
                )
            wrapp(
                "He ducks below a counter, and pops back up, holding a drawer with a variety of items as well as prices affixed to them."
            )
            wrapp("\"Well, " + name + "? What'll you have?\"")
            storyProg.update({"smithIntro": 1})
        elif storyProg["smithIntro"] == 1:
            wrapp(
                "The smith greets you, the shop spread glittering before you.")
            wrapp("\"What'll you have?\" he asks, grinning broadly.")

        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if cmd == "L" or cmd == "LIVING QUARTERS":
            wrapp(
                "As you approach the living quarters, a hairy arm stops you.")
            wrapp(
                "\"Woah, lil' buddy, that's kind of private,\" he says. \"I don't just waltz into your bedroom, do I?\""
            )
            wrapp(
                "Slightly shamefully, you make your way back to the front of the room."
            )
        if cmd == "O" or cmd == "OUTSIDE":
            wrapp("You make your way out of the smithy.")
            wrapp("\"Come back soon!\" shouts the smith, waving you out.")
            storyProg.update({"roomID": 3})
        if cmd == "SH" or cmd == "SHOP":
            wrapp("You glance at the shop.")
            shopping = 1
            rflask = {
                "itemName":
                "RIDDLER'S FLASK",
                "status":
                "5G",
                "itemDesc":
                "Filled with an unknown burbling, boiling liquid, it's used often in deserts like the mythical Sahara, at least according to the traveller who sold the flask to the smith. The smith did his own investigation, and found that the item was cursed to never relieve thirst while containing infinite liquid. Really only useful for looking nice."
            }
            msword = {
                "itemName":
                "MAGIC SWORD",
                "status":
                "100G",
                "itemDesc":
                "A magic sword. Useful for heroes and the adventuring type, but quite unwieldy. Made by the blacksmith on commission, but the commissioner never returned to pick up the sword. That's what happens to heroes..."
            }
            gamelon = {
                "itemName":
                "WAND OF GAMELON",
                "status":
                "75G",
                "itemDesc":
                "A magic wand from a far-off realm. Or so the Blacksmith claims. It glows a little, but you vaguely remember the guard complaining about his old lance being reused in a project."
            }
            catalog = [rflask, msword, gamelon]
            while shopping == 1:
                cmd = cashier(catalog, gold, cmd)
                if cmd == "R" or cmd == "RIDDLER'S FLASK":
                    gold = shop("RIDDLER'S FLASK", catalog, gold)
                if cmd == "M" or cmd == "MAGIC SWORD":
                    gold = shop("MAGIC SWORD", catalog, gold)
                if cmd == "W" or cmd == "WAND OF GAMELON":
                    gold = shop("WAND OF GAMELON", catalog, gold)
                if cmd == "QUIT" or cmd == "Q":
                    wrapp("\"Thanks much!\"")
                    shopping = 0
    while storyProg["roomID"] == 5:
        lbreak()

        avail_locs = ["CASEY'S HOUSE", "OLD MAN'S HOUSE", "WELLSIDE PATH"]
        room_objs = ["LOOKOUT", "GIANT TREE"]

        #wip()
        wrapp("You are in the half of town known as Treeside.")
        if storyProg["oldManIntroTreeside"] == 0:
            wrapp(
                "Treeside derives its name from the giant tree that occupies most of the space of this half of town. Its boughs are constantly covered in leaves; leaves that never turn any color but green. The tree is the biggest one you've ever seen in your life, and it's your town's main claim to fame. Casey told you the tree supposedly had a healing aura, but one time you scraped your knee while playing and then fell asleep in the shade but when you woke up it was still slightly pink, so you're not entirely sure Casey was right."
            )
            wrapp(
                "As you finally make your way into the main part of Treeside, the clearing between Casey's (to you) massive two-story house and the old man's house, you look for Old Man Monty."
            )
            if storyProg["talkwizcheck"] == 1:
                wrapp(
                    "You remember the promise that you made your mom, but you are curious as to where he is. So you can avoid him, of course."
                )
            wrapp(
                "Usually, he's sitting on the lookout or near the base of the tree, studying some arcane text or another, or working on the automatic supply summoners for the town."
            )
            wrapp(
                "As you look, you notice that he was at the base of the tree, at least judging by the fact that he left a small stack of tomes on the ground. You look around for him, only to see the door to Casey's house close."
            )
            storyProg.update({"oldManIntroTreeside": 1})
            storyProg.update({"oldManinCHouse": 1})
        else:
            wrapp(
                "The shade of the tree covers you, leaving you nice and cool.")
            wrapp("The old man's tomes are near the base of the tree.")
            if storyProg["oldManinCHouse"] == 1:
                wrapp(
                    "You remember seeing the old man enter Casey's house. Perhaps you should go after him."
                )
            if storyProg["oldManinCHouse"] == 0:
                wrapp(
                    "The old man is standing by his tomes, watching you, waiting for you to approach him. His grip on his staff is tight."
                )
        if storyProg["oldManinCHouse"] == 0:
            room_objs.append("OLD MAN")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if cmd == "CASEY'S HOUSE" and storyProg[
                "oldManinCHouse"] == 1 or cmd == "C" and storyProg[
                    "oldManinCHouse"] == 1:
            storyProg.update({"roomID": 6})
            wrapp("You head into Casey's house, following the old man inside.")
        if cmd == "CASEY'S HOUSE" and storyProg[
                "oldManinCHouse"] == 0 or cmd == "C" and storyProg[
                    "oldManinCHouse"] == 0:
            storyProg.update({"roomID": 6})
            wrapp("You head into Casey's house.")
        if cmd == "OLD MAN'S HOUSE" or cmd == "O":
            wrapp("You try the door. Locked.")
            wrapp(
                "You're not really sure why you expected anything different.")
        if cmd == "WELLSIDE PATH" or cmd == "W":
            wrapp(
                "You head back towards Wellside, watching your feet as you walk down the path."
            )
            storyProg["roomID"] = 3
        if cmd == "OLD MAN" and storyProg[
                "oldManinCHouse"] == 0 or cmd == "OL" and storyProg[
                    "oldManinCHouse"] == 0:
            wrapp("The old man smiles slightly as you approach him.")
            wrapp(
                "\"So!\" he says, a bit too loudly and chipper. \"It was your birthday yesterday, yes?\""
            )
            if storyProg["presentCount"] >= 6:
                wrapp(
                    "Considering that the old man didn't get you anything, you're a little surprised he remembered it was your birthday at all."
                )
            wrapp("You nod in response.")
            wrapp("\"Great! That's great. And you're twelve, yes?\"")
            wrapp("You nod again, hesitantly this time.")
            wrapp(
                "\"Cool, that's cool,\" he says. \"It actually was my birthday yesterday, too.\""
            )
            wrapp(
                "You ask him how old he is. Then you realize it's a rude question to ask."
            )
            wrapp("He laughs, and says, \"I'm 90 as of yesterday, " + name +
                  ". It's okay. I know I look much older.\"")
            wrapp(
                "You aren't sure what he means by that. Old man Monty, despite being hunched over with a thick white beard, never really seemed old to you. Well, he was old, you did literally call him 'the old man' in your head, maybe he was old as Gertrude, but he never seemed... feeble? Feeble."
            )
            wrapp("He looks good for 90, is what you conclude.")
            wrapp(
                "The old man stares at you as you contemplate this. Any humor he had gained from your question seems gone now. His countenance is exceptionally grave. You look up at him, and he speaks."
            )
            wrapp("\"I know what happened to Casey,\" he says.")
            TalkOptions = ["WHAT", "HOW"]
            talklist()
            cmd = talkwhat(cmd, TalkOptions)
            wrapp(
                "\"The what and how aren't important right now,\" he says. \"But I'll just say I have a friend who went through a similar experience to what she must be going through right now, and I'd like to introduce you to her.\""
            )
            wrapp(
                "You're floored for a moment. You don't even know how to respond."
            )
            wrapp("But then you ask...")
            TalkOptions = ["WHO"]
            talklist()
            cmd = talkwhat(cmd, TalkOptions)
            wrapp(
                "\"You haven't met her,\" says Monty. \"And I know that in a town with about half-a-dozen people that's hard to believe, but she's kept herself secret at my request.\""
            )
            wrapp("\"Her name is Tabbs.\"")
            wrapp(
                "You try to think back, remember if anyone ever said that name to you before, but you come up empty-handed."
            )
            wrapp("You ask the old man...")
            TalkOptions = ["WHERE"]
            talklist()
            cmd = talkwhat(cmd, TalkOptions)
            wrapp(
                "\"I'll take you to her,\" says the old man. \"Meet me outside the well.\""
            )
            wrapp(
                "The old man walks away, leaving you more worried than before you talked to him."
            )
            storyProg["oldManinCHouse"] = 99
        if cmd == "LOOKOUT" or cmd == "LO":
            wrapp(
                "The lookout post. You climb the tree briefly to see the view."
            )
            wrapp(
                "Looking out over the landscape, you see the sloped, rolling hills of your country of Sebestos. You can see fields further out, fields of flowers and wheat and meadows and lakes. And if you really squint, really try your hardest to make it out, that, or just use the telescope that you left on the lookout for this exact purpose, you can see the distant pillars of the capital city of Bashapt."
            )
            wrapp(
                "You've never been there, but you're more than curious. For now, though, you're content just imagining and looking at the hills and fields."
            )
            wrapp("You climb back down. Nature is amazing!")
        if cmd == "GIANT TREE" or cmd == "GI":
            wrapp("The town's giant tree.")
            wrapp(
                "Your mom used to tell you bedtime stories about how the tree had, in the past, been the home of a spirit of death. One time, the tree's spirit was disturbed by an evil wizard, and the spirit destroyed the wizard in retaliation."
            )
            wrapp(
                "The story didn't really help you go to sleep. A bit of an odd choice of story, in retrospect."
            )
    while storyProg["roomID"] == 6:  #Casey's house w/Monty encounter
        lbreak()
        wrapp("You are in Casey's house, in the main room of the lower floor.")
        avail_locs = ["OUTSIDE", "UPSTAIRS"]
        room_objs = ["WORKSHOP", "CASEY'S DAD"]
        if storyProg["oldManinCHouse"] == 1:
            wrapp(
                "Casey's house is similar to yours, in that the lower floor is almost entirely comprised of one large room, containing the kitchen, entertainment space, and a table, but it's different in its approach to each aspect. Rather than the sparse, functional design your house sports, the design of Casey's house prepares for everything."
            )
            wrapp(
                "The kitchen wall is lined with shelves and drawers filled with every ingredient you've heard of and more, plus tools and utensils for food and crafting alike. The countertops have several preperation stations where you and Casey labored over cakes, cookies, and arts and crafts."
            )
            wrapp(
                "Casey often referred to this part of the kitchen as \"The Workshop,\" and aside from her dad occasionally complaining about wood shavings that found their way into the skillet drawer, it's overall a favorable layout for everyone."
            )
            wrapp(
                "In addition to all of this, Casey's house has a second floor, the only house to have one in town, excluding your own, of course. This is supported by a wooden beam in the middle of the room, which you've accidentally sleepwalked into more times than you care to admit."
            )
            wrapp(
                "The first thing you notice when you enter is Casey's dad sitting on a couch, conversing with old man Monty. You're not good enough at reading faces to be sure, but Casey's dad could be holding back tears."
            )
            wrapp("They don't seem to have noticed you.")
            wrapp("You...")
            TalkOptions = ["EAVESDROP"]
            talklist()
            cmd = talkwhat(cmd, TalkOptions)
            wrapp(
                "From where you are, you can barely make out the pair's conversation. You tiptoe over just in time to catch old man Monty asking Luke a question.."
            )
            wrapp(
                "\"And you're sure she was in her bed before you fell asleep?\" he asks. \"Completely immobile from her illness?\""
            )
            wrapp(
                "Luke sighs deeply. \"I've told you everything, Monty. She was in bed, still as sick as she was yesterday, when I finally dozed off in the chair. I open my eyes and it's six hours later, and she's gone. That is all I know.\""
            )
            wrapp(
                "\"Was she in any distress? Did she report any strange dreams?\" Monty is looming over Luke. \"What was she wearing before she disappeared? Please, Luke, this is important!\""
            )
            wrapp(
                "Luke stands up suddenly, fury in his eyes. \"Alright, old man,that's enough. I don't know how in the hells you found out my daughter disappeared before I told anyone, but I don't like the direction these questions are going. If you're not going to help, get the hell out of my house.\"" 
            )
            wrapp(
                "Monty stands up too, indignantly, and almost says something before he notices you out of the corner of his eye."
            )
            wrapp(
                "The old man stops saying what he was going to say and turns to face you."
            )
            wrapp(
                "\"Ah, " + name +
                ", you're here,\" he says. He turns back to Casey's dad. \"I'm sorry, Luke, I'm going to have to cut this a little short. "
                + name +
                ", please meet me outside. We, ah, have some things that need dicussing.\""
            )
            wrapp(
                "Monty walks away, leaving Casey's dad to sit back down on the couch, staring at the old man's retreating figure."
            )
            wrapp(
                "Luke sits there a moment longer, watching as the door closes, before turning to you slowly, and attempting to put on a happy face. He gives up halfway through the attempt."
            )
            wrapp("\"Casey's gone,\" he says. \"Thought you ought to know.\"")
            storyProg.update({"oldManinCHouse": 0})
        else:
            wrapp("Casey's dad is sitting on the couch, looking somehow lost.")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if cmd == "CASEY'S DAD" and storyProg[
                "LukeTalk"] == 0 or cmd == "CA" and storyProg["LukeTalk"] == 0:
            wrapp("You ask Casey's dad what he meant by that.")
            wrapp(
                "He blinks owlishly at you, taking you in your entirety in, before continuing. \"She wasn't in her room this morning,\" said Luke. \" I thought maybe she had somehow... I dunno. She was too sick to move yesterday, it doesn't make sense for her to have somehow snuck out to see you.\""
            )
            wrapp("Casey's dad sighs. \"And yet, she's not in her room.\"")
            wrapp("\"But don't let my brooding distract you, " + name +
                  ". Was there anything you wanted to talk about?\"")
            convoTree = 1
            TalkOptions = ["CASEY", "MONTY", "ARE YOU OKAY", "NO"]
            talklist()
            cmd = talkwhat(cmd, TalkOptions)
            while convoTree == 1:
                if cmd == "CASEY" and "CASEY" in TalkOptions or cmd == "C" and "CASEY" in TalkOptions:
                    wrapp(
                        "\"I don't know, " + name +
                        ", I really don't. She was in bed, still as sick as she was yesterday, when I finally dozed off in the chair. I open my eyes and it's six hours later, and she's gone.\""
                    )
                    wrapp(
                        "He shakes his head and puts his head in his hands. \"God, if Isabella were here she'd know what to do.\" He looks like he's about to lament some more, but he starts, as if remembering your presence, and stops talking."
                    )
                    TalkOptions.remove("CASEY")
                    cmd = "a"
                elif cmd == "MONTY" and "MONTY" in TalkOptions or cmd == "M" and "MONTY" in TalkOptions:
                    wrapp(
                        "\"Oh, the old man just wanted to ask me what I knew about... Casey's disappearance.\""
                    )
                    wrapp(
                        "\"I told him all I knew, but the guy kept asking for more. Asking if I remembered the dream I had before I dozed off, what clothes Casey was wearing... he probably had the best intentions, but he... his delivery was not the most graceful.\""
                    )
                    wrapp(
                        "\"Monty is a lot of things, but good at reassuring worried fathers he is not,\" says Casey's father with a small smile. It quickly fades."
                    )
                    TalkOptions.remove("MONTY")
                    cmd = "a"
                elif cmd == "ARE YOU OKAY" and "ARE YOU OKAY" in TalkOptions or cmd == "A" and "ARE YOU OKAY" in TalkOptions:
                    wrapp("\"What? Yeah. Yeah, I am, " + name +
                          ", why do you ask?\"")
                    tempOpts = ["WORRIED", "NO REASON"]
                    cmd = talkwhat(cmd, tempOpts)
                    wrapp(
                        "\"Well, that's sweet of you, but I'm just fine. I'm honestly more worried about Casey.\""
                    )
                    TalkOptions.remove("ARE YOU OKAY")
                    cmd = "a"
                elif cmd == "NO" or cmd == "N":
                    wrapp(
                        "\"That's okay,\" says Casey's dad. \"But if you hear anything about Casey, let me know."
                    )
                    convoTree = 0
                    storyProg.update({"LukeTalk": 1})
                else:
                    wrapp("Luke doesn't understand what you meant by that.")
                    talklist()
                    cmd = talkwhat(cmd, TalkOptions)
                if cmd == "a":
                    wrapp("\"Anything else you want to talk about?\"")
                    talklist()
                    cmd = talkwhat(cmd, TalkOptions)
        if cmd == "CASEY'S DAD" and storyProg[
                "LukeTalk"] == 1 or cmd == "CA" and storyProg["LukeTalk"] == 1:
            wrapp(
                "\"I'm sorry, " + name +
                ", I'm feeling a little emotionally drained right now. Can we talk again some other time?\""
            )
        if cmd == "O" or cmd == "OUTSIDE":
            wrapp("You make your way outside.")
            if storyProg["caseyBug1"] == 1:
                wrapp(
                    "As you open the door, you notice the ladybug from earlier fly into the house."
                )
                wrapp("You're not sure what to make of that.")
                storyProg.update({"caseyBug1": 2})
            storyProg.update({"roomID": 5})
        if cmd == "WO" or cmd == "WORKSHOP":
            wrapp("The workshop. Or as Casey calls it, The Workshop.")
            wrapp(
                "This is the place you and Casey made countless arts and crafts. And pancakes."
            )
            wrapp(
                "You're tempted to pull out some stuff and try to start making things, but Casey isn't here, and it's weird to even think about messing with The Workshop alone."
            )
        if cmd == "U" or cmd == "UPSTAIRS":
            wrapp("You make your way to Casey's room.")
            storyProg.update({"roomID": 7})

    while storyProg["roomID"] == 7:
        lbreak()
        avail_locs = ["DOWNSTAIRS"]
        room_objs = ["SKETCHES", "ART SUPPLIES", "WINDOW"]
        wrapp("You are in Casey’s room.")
        if storyProg["room7intro"] == 0:
            wrapp(
                "Casey’s room is similar to yours, in that it has a windowsill, a bed, and is littered with stuff. But it’s more... Casey, for lack of a better term. The walls have tons of sketches and doodles pinned onto them, of designs for heroes and stories that you and Casey planned out but never got around to finishing."
            )
            wrapp(
                "In addition to Casey's ever-present art case, Casey’s floor has a few tools and brushes lying around, and some of them are sharp and potentially dangerous. You learned that the hard way once. Casey didn’t stop apologizing every time you saw her for nearly a week."
            )
            wrapp(
                "Notably, Casey is not in her room as far as you can tell, which lines up with what her dad told you."
            )
        if storyProg["talkwizcheck"] != 2:
            wrapp("You briefly wonder what the old man wants you for.")
            storyProg.update({"room7intro": 1})
        else:
            wrapp("You don’t see Casey anywhere.")
        if storyProg["caseyBug1"] == 2:
            wrapp("The ladybug from earlier is on Casey’s windowsill.")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if cmd == "D":
            wrapp("You head back downstairs.")
            storyProg.update({"roomID": 6})
        if cmd == "SK" or cmd == "SKETCHES":
            wrapp("You glance at the sketches of armor and people.")
            wrapp(
                "You and Casey spent hours on these. Your drawings aren't as polished as hers, but it didn't matter to either of you, because just thinking of outfits and powers and settings was fun by itself."
            )
            wrapp(
                "Having a finished product would just be icing on the cake. But cakes tasted just fine without icing, too!"
            )
            wrapp(
                "At one point in time, you began making sketches for a story featuring a shapeshifting demon, but you gave up on that idea. Too ambitious for you."
            )
            wrapp(
                "Casey tried inventing this huge world full of politics and intrigue, beginning with the main character stopping an assassination, but she couldn't figure out what to name the main character and dropped the project altogether."
            )
            wrapp(
                "You both came to the conclusion that writing was hard. The pair of you mostly stuck to visual storytelling instead."
            )
        if cmd == "ART SUPPLIES" or cmd == "AR":
            wrapp(
                "You stare down the art supplies, and specifically, the small wooden case with the word \"ART\" painted on it."
            )
            wrapp(
                "A gift to Casey from Gertrude and your mother, it's a variation on your backpack, using some of the same spellwork that Gertrude uses to create her fabrics. Rather than being enchanted to have infinite space for infinite items, it's enchanted to have infinite art supplies. All you or Casey need to do is think of what you want to create and the appropriate supply comes out!"
            )
            wrapp(
                "It doesn't, however, have an appropriate disposal method, and you and Casey both were too sentimental to throw out the supplies like regular garbage. So on the floor they stay, and so it shall be."
            )
            wrapp(
                "You briefly consider taking it. But, no, it's Casey's, and you can't seriously entertain that thought for more than a second."
            )
        if cmd == "WINDOW" or cmd == "WI":
            wrapp("Casey's bedroom window.")
            wrapp(
                "It allows her a good view of Wellside, as well as being useful for letting in air."
            )
            wrapp("It's open just a crack.")
            if storyProg["caseyBug1"] == 2:
                wrapp(
                    "You notice the ladybug from earlier is on the windowsill."
                )
                wrapp("Does this ladybug just like windowsills or something?")
                wrapp(
                    "You realize that you may have said that out loud once the ladybug flies away through the open window."
                )
                wrapp("The ladybug is free.")
                wrapp("...oops. You didn't mean to scare it.")
                storyProg.update({"caseyBug1": 3})

    while storyProg["roomID"] == 8:
        lbreak()

        # wip()
        avail_locs = ["SEWER"]
        room_objs = ["BUCKET"]
        wrapp(
            "You are at the bottom of the well, standing on a ledge surrounding the water."
        )
        wrapp(
            "Loosely hanging beside you is the bucket used for bringing water up."
        )
        if storyProg["wellIntro"] == 0:
            if storyProg["oldManinCHouse"] == 4:
                wrapp("Monty and Tabbs follow you out of Tabbs's chamber.")
                wrapp(
                    "\"We're going up,\" says Monty. He holds his staff into the air, and the same blue spark from earlier flies from the top. It hovers in midair for a moment before breaking off a smaller version of itself, forming the lowest rung of the ladder. As soon as that spark solidified into the electric blue ladder you had climbed down, the main spark rockets up the well, splitting itself off at appropriate intervals to form the rest of the ladder."
                )
                wrapp(
                    "You reach for the ladder before a thought occurs to you.")
                wrapp(
                    "You ask the old man how Tabbs was supposed to climb up the ladder without legs."
                )
                wrapp(
                    "He ponders this question for a moment. \"Well, that's actually--\""
                )
                wrapp(
                    "Tabbs interrupts him. \"Tabbs can... ssssshift back into smaller Tabbssss,\" she says. \"Not painful... but Tabbs doesn't like the feeling of being ssssso sssssmall...\""
                )
                wrapp(
                    "Monty looks at her, startled. \"You can do that? You would do that?\""
                )
                wrapp(
                    "Tabbs looks at her hands. \"Only temporary,\" she says, \"can grow again... but ssstill unpleasant. But if Tabbs can leave the well...\""
                )
                wrapp(
                    "Tabbs closes her eyes. As you watch, her arms melt away into her body, her hair vanishing before your eyes. Within only moments, where Tabbs stood was a giant snake with no semblance of humanity in its appearance at all. Then it begins to shrink."
                )
                wrapp(
                    "By the time you've finished processing what you just witnessed, Monty's already picked up the smaller form of Tabbs, who slithered around his neck."
                )
                wrapp(
                    "\"Well, are you ready?\" he asks the snake. She nods. Then Monty turns to you. \"Jai, lead the way.\""
                )
                storyProg["oldManinCHouse"] = 50
                storyProg["wellIntro"] = 2
                avail_locs.append("LADDER")
            else:
                wrapp("The well is... damp. Musty. Cold.")
                wrapp(
                    "You shiver at the atmosphere. Was this really where Monty's friend lived?"
                )
                wrapp(
                    "Monty glances at you. \"" + name +
                    ",\" he says. \"Follow me, we're going deeper into a tunnel. Tabbs resides down there.\""
                )
                wrapp(
                    "He walks away on the sewer ledge, leaving a trail of lingering blue sparks with each footstep."
                )
                wrapp("The ladder disappears as he does so.")
                storyProg["wellIntro"] = 1
        elif storyProg["wellIntro"] == 2:
            wrapp("Monty and Tabbs are waiting for you to climb up.")
            avail_locs.append("LADDER")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if cmd == "BU" or cmd == "BUCKET":
            wrapp(
                "A bucket. Used for bringing water up and down from the underground river, the one you're standing precariously close to."
            )
            wrapp("It's connected to the upper areas via a pulley system.")
        if cmd == "LADDER" and "LADDER" in avail_locs or cmd == "L" and "LADDER" in avail_locs:
            wrapp(
                "You climb up the ladder. Monty, with Tabbs wrapped around his neck, follow shortly behind you."
            )
            wrapp("The two of you climb over the edge of the well.")
            storyProg["roomID"] = 3
        if cmd == "S" or cmd == "SE":
            if storyProg["oldManinCHouse"] == 3:
                wrapp(
                    "You follow Monty's blue footprints and head deeper into the sewer."
                )
                wrapp(
                    "You turn the corner and see Monty standing outside an archway, staring inside. You begin to make your way to it, but right before you enter the next room, Monty stops you, holding a hand out to block your entrance."
                )
                wrapp(
                    "\"You are about to meet with Tabbs,\" he warns you. \"And despite everything I said about her being true, she is my friend, I have to be completely honest. She is not all there.\""
                )
                wrapp(
                    "Monty turns around to face you. His countenance is tight, mouth set in a grim line as he speaks. \"Years ago, she was afflicted by a curse that severely distorted her physical being. This was eventually partially undone, but her mental state never recovered.\""
                )
                wrapp("You swallow.")
                wrapp(
                    "\"I believe your friend Casey underwent a similar curse. But the rest is Tabbs's story to tell.\""
                )
                wrapp(
                    "You try and peer into the doorway beyond. It seems pitch-black, but you can hear something moving."
                )
                wrapp(
                    "The unspoken question is clear to both you and Monty. \"I'll tell you the details later,\" he says. \"For now, just promise me one thing.\""
                )
                wrapp("You nod uncertainly.")
                wrapp(
                    "\"Tabbs will ask you your age. From this moment on, you are eighteen years old or older. Do you hear me? How old are you?\""
                )
                convoTree = 1
                while convoTree == 1:
                    try:
                        storyProg["age"] = int(input("Enter a number. "))
                    except ValueError:
                        storyProg["age"] = 0
                    if storyProg["age"] >= 18:
                        wrapp(
                            "Monty sighs in relief. \"Good. Good! Just say that number and everything should be all right.\""
                        )
                        wrapp("He steps aside, and you enter the chamber.")
                        wrapp(
                            "As you step inside, you hear Monty say a whispered \"Good luck.\""
                        )
                        convoTree = 0
                        storyProg["roomID"] = 9
                    else:
                        wrapp(
                            "\"" + name +
                            ", I'm serious. What do you say if Tabbs asks you your age?\""
                        )
                else:
                    wrapp("You look into the darkness of the sewer.")
                    wrapp(
                        "It's too dark to see without the old man leading the way..."
                    )
                    wrapp("You decide not to risk it.")
    while storyProg["roomID"] == 9:
        lbreak()

        avail_locs = ["WELL"]
        room_objs = ["SKELETONS", "TABBS", "MONTY"]

        wrapp("You are in Tabbs's chamber.")
        if storyProg["tabbsChambIntro"] == 0:
            wrapp(
                "At first, you don't see any living person. The room is nearly pitch black, with the only light coming from Monty's glowing footprints. Any tiny rays of light that managed to come from the open well far away didn't make it past a few feet into the room."
            )
            wrapp(
                "This limited light, however, allows you to see that the floor is littered with animal bones."
            )
            wrapp(
                "You just about avoid stepping on a tiny ribcage when you glimpse movement in front of you."
            )
            wrapp("You...")
            TalkOptions = ["CALL OUT", "DO NOTHING"]
            talklist()
            cmd = talkwhat(cmd, TalkOptions)
            if cmd == "C" or cmd == "CALL OUT":
                wrapp("You call out to Tabbs.")
            else:
                wrapp(
                    "You are suddenly aware of how heavy your breath is. Was it the climb down the ladder that made your heart start pounding?"
                )
            wrapp(
                "Perhaps in reaction to the noise you made, the movement you weren't even 100% sure was there suddenly stops. Then it starts again. A ray of light glints off what you realize are scales, moving closer and closer to you."
            )
            wrapp(
                "You take a step back. The creature, whatever it is, seems to be massive, as it feels like the whole room is coming to life. You look back at Monty, but he nods at you. What's that supposed to mean!?"
            )
            wrapp(
                "Before you have a chance to back out, you hear a hissing noise come from deeper within the chamber. It resolves into a parched, cracked voice."
            )
            wrapp("\"Chosen...\" it whispers. \"Chosen... how old iss you?\"")
            storyProg["tabbsChambIntro"] = 1
            convoTree = 1
            while convoTree == 1:
                try:
                    storyProg["age"] = int(input("Enter a number. "))
                except ValueError:
                    storyProg["age"] = 0
                wrapp(
                    "Tabbs, for that is who was talking, comes out of the darkness, and you can finally see her face and most of her upper body."
                )
                if storyProg["age"] >= 18:
                    wrapp(
                        "Her clothes are tattered, figure gaunt. Tabbs is smiling, but it's not the smile of a healthy woman. In fact, the word you'd use was slightly deranged."
                    )
                    wrapp(
                        "\"Yessss...\" she whispers, almost reverently. \"Chosen... come to Tabbs.\""
                    )
                    wrapp(
                        "She shudders, and you can see something like pleasure run down her spine. You follow it down to her lower body, which is slowly moving into visibility, only to startle when you realize her lower body is that of a giant snake."
                    )
                    wrapp(
                        "This couldn't be real. This was too fantastical to believe. You were going on an adventure, with snake women calling you the \"Chosen,\" and Casey wasn't here with you."
                    )
                    wrapp("...was something like what happened to Casey?")
                    wrapp(
                        "Tabbs continues, oblivious to your introspection. \"I've waited "
                        + str(78 + storyProg["age"]) +
                        " years for thisss...\"")
                    convoTree = 0
                    storyProg["oldManinCHouse"] = 9
                else:
                    wrapp(
                        "Her clothes are tattered, figure gaunt. Tabbs is frowning, but it's not the frown of a healthy woman. In fact, the word you'd use was slightly deranged. She's showing too many teeth for you to feel comfortable."
                    )
                    wrapp(
                        "\"Chosen...\" she says, almost a whisper. \"Are you... not yet of age?\" Her voice seems to contain infinite sadness, dry though it may be."
                    )
                    convoTree = 0
            wrapp(
                "Just then, Monty runs through the gateway. \"The Chosen was joking with that!\" he said, waving his staff to create light. Tabbs recoils slightly at the bright blue orb that suddenly flickers into existence at the top of Monty's staff, but she clearly knows who he is. \"It was a joke! The Chosen is actually bona-fide eighteen-plus years old!\""
            )
            if storyProg["age"] >= 18:
                wrapp(
                    "Tabbs cocks her head at Monty. \"The Chosen said as much...\" she utters. \"Was it a joke?\""
                )
                wrapp(
                    "Monty backtracks immediately. \"No! It absolutely was not a joke! I'm sorry, I was just confused momentarily!\""
                )
                wrapp(
                    "He glances at you, as if not sure whether he's supposed to be grateful or angry that you followed his intructions. You're not sure whether or not to be grateful that he tried to help or angry he had so little faith in you."
                )
            else:
                wrapp(
                    "Tabbs instantly relaxes. \"Chosen...\" she says, looking at you. \"A funny joke, yessss... but one that scared Tabbs. Next time just ssssay the truth.\""
                )
                wrapp(
                    "She smiles at you. You have the feeling that Tabbs hadn't smiled in a very long time; it looks alien on her face. And her teeth are... sharp."
                )
            wrapp(
                "Monty takes a deep breath. \"Well,\" he says. \"Can we get down to business?\""
            )
            TalkOptions = ["BUSINESS"]
            talklist()
            cmd = talkwhat(cmd, TalkOptions)
            wrapp(
                "\"Businesssss?\" repeats Tabbs. She looks at Monty with wide eyes. \"Tabbs hasn't done business since... nearly a century ago...\" Her voice trails off into a mumble."
            )
            wrapp(
                "Monty shifts his stance, and leans on his staff. \"I mean business, Tabbs. The prophecy. The Chosen's best friend disappeared a few years ago, and now that we've fulfilled the age requirement of the prophecy we were hoping to begin saving her.\""
            )
            wrapp(
                "You don't have time to contemplate why Monty lied because Tabbs slithers towards the back of the room, faster than you expected from a half-snake."
            )
            wrapp(
                "You hear her rifling through some things, until suddenly the sound of papers shuffling stops. Tabbs turns around towards you, her long tail trailing behind her. In her hands is an ancient-looking piece of parchment, damaged by both the passage of time and slight scorching."
            )
            wrapp(
                "\"The Prophecy,\" states Tabbs, clutching the parchment to her chest. \"It is finally time, Chosen... time to save the one you losssst...\""
            )
            wrapp(
                "Monty turns away from Tabbs to face you. \"" + name +
                ",\" he says. \"This prophecy should answer nearly every question you have.\" He turns back to Tabbs, and taps the bottom of his staff on the floor of the chamber. The animal bones rattle slightly, and you feel some kind of magical energy rush through you as it fills the room."
            )
            wrapp(
                "You turn to Tabbs. She's looking at the parchment, expression neutral. Then she passes it to Monty, who gravely accepts it."
            )
            wrapp("Monty looks at you. \"" + name +
                  ", are you ready to hear the prophecy?\"")
            cmd = yesno(cmd)
            if cmd == "N" or cmd == "NO":
                wrapp(
                    "Tabbs hisses. \"Chosen...\" she says. \"You have come here from so far... you must face your fate. Read the prophecy.\""
                )
            wrapp(
                "Monty nods, clearing his throat. You feel another pulse of magical energy as he does so."
            )
            wrapp("Finally, Monty opens his mouth, and begins to read.")
            lbreak()
            wrapp("THE PROPHECY")
            wrapp("As Time will tell, the story goes,")
            wrapp("A curse befalls the living, those")
            wrapp("who Dedicate their lives to Good,")
            wrapp("Who fought the Evil where it stood.")
            print()
            wrapp("A town is picked, a darkness wrought")
            wrapp("A pair of heroes, not for nought")
            wrapp("A Change befalls the hero’s friend")
            wrapp("Potentially, they meet their end.")
            print()
            wrapp("If that be the case, head to the Capital,")
            wrapp("The Elder beside you, you won’t need a map at all.")
            wrapp("Friends by your side, the Evil fought off,")
            wrapp("The curse’s destruction... ")
            print()
            wrapp(
                "Monty's voice trails off. His finger goes past the scorch marks on the page to a lower part of the parchment."
            )
            wrapp("He continues...")
            print()
            wrapp("...but heed this warning, hesitate,")
            wrapp("Before the hero's one and eight")
            wrapp("The curse cannot be touched, don’t try")
            wrapp("Else all of man will Sleep")
            wrapp("For all of Time.")
            print()
            wrapp("You have been warned.")
            lbreak()
            wrapp(
                "Monty hands the parchment back to Tabbs. She slowly slithers away, putting the prophecy back where it was."
            )
            wrapp(
                "Finally, Monty lifts his staff, looking weary with the effort. \"So you see, now, don't you, "
                + name +
                "? The curse, the same one that took Tabbs from me the first time, it's hitting Casey now.\" "
            )
            wrapp(
                "\"To me, the next steps are clear,\" he says. \"I'm obviously the Elder the prophecy refers to, and you're the hero, and Casey's the hero's friend. Thus, we must go to the capital city of Bashapt.\""
            )
            wrapp(
                "\"I'll give you the copy of the prophecy I just made,\" he says. He reaches into his robe and pulls out a piece of parchment that looks identical to the one you just saw Tabbs put away."
            )
            addInv(inventory, "PROPHECY")
            wrapp(
                "He nods. \"We'll head out right away,\" he says. \"There is no time to waste if we want to break the curse and save Casey. Tabbs, you'll come too.\""
            )
            wrapp(
                "Tabbs perks up. \"Tabbs isss... going out?\" she asks, hope brimming in her eyes. \"Tabbs is practiced with being... sssstealthy!\""
            )
            wrapp(
                "Monty averts his eyes slightly but says, \"Yes, Tabbs. But do keep yourself out of sight. We'll get going in a minute.\""
            )
        else:
            wrapp(
                "Monty is making some preparations for the journey, flipping through a portable tome he brought with him and occasionally muttering something."
            )
            wrapp("Tabbs looks impatient to get out of her chamber.")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if cmd == "WELL" or cmd == "W":
            wrapp("You head out of Tabbs's chamber.")
            wrapp(
                "Monty follows you out, and Tabbs slithers towards the exit behind him."
            )
            storyProg["roomID"] = 8
            storyProg["oldManinCHouse"] = 4
        if cmd == "TABBS" or cmd == "TA":
            wrapp("You move to Tabbs.")
            wrapp(
                "From the waist up, Tabbs looks to be about your mom's age. Maybe younger. The only reason you aren't sure is because she looks... ragged. Her face has monstrous edges to it, like her teeth and the shape of her eyes. Her fingernails are long and sharp."
            )
            wrapp(
                "This makes sense when you look at her from the waist down. Instead of legs, Tabbs's entire lower body is that of a giant snake. You don't know enough about snakes to say which species. Maybe an anaconda or a python."
            )
            wrapp(
                "In her excitement to be ready to leave, she doesn't seem to notice your staring. When was the last time she left her sewer?"
            )
        if cmd == "MONTY" or cmd == "MO":
            if storyProg["oldManinCHouse"] != 999:
                wrapp("Monty stops flipping through his book for a moment.")
                wrapp("\"Ah, " + name +
                      ", what is it? Do you have any more questions for me?\"")
                convoTree = 1
                TalkOptions = ["CASEY", "TABBS", "NO"]
                talklist()
                cmd = talkwhat(cmd, TalkOptions)
                while convoTree == 1:
                    if cmd == "NO" or cmd == "N":
                        wrapp(
                            "\"Sure, " + name +
                            ". If you have any questions absolutely feel free to ask, but I want to be on our way to the Capital sooner rather than later.\""
                        )
                        convoTree = 0
                        storyProg["oldManinCHouse"] = 999
                    elif cmd == "CASEY" and "CASEY" in TalkOptions or cmd == "C" and "CASEY" in TalkOptions:
                        wrapp(
                            "\"What exactly happened to Casey... I don't know the exact details.\""
                        )
                        wrapp(
                            "\"But when I was...\" He lowers his voice. \"your age, my best friend disappeared from her home after a day of intense physical sickness. Six years later, when I turned eighteen, I found her, but the curse had been on her for so long, we were never able to turn her fully human again.\""
                        )
                        wrapp(
                            "\"That's why I want to save Casey sooner rather than later, you understand? I don't know what she's been trapped as, but better to save her now than have her be...\" He glances at Tabbs. \"Less than human.\""
                        )
                        cmd == "a"
                        TalkOptions.remove("CASEY")
                    elif cmd == "TABBS" and "TABBS" in TalkOptions or cmd == "T" and "TABBS" in TalkOptions:
                        cmd == "a"
                        TalkOptions.remove("TABBS")
                    else:
                        wrapp(
                            "Monty doesn't understand what you meant by that.")
                        talklist()
                        cmd = talkwhat(cmd, TalkOptions)
                    if cmd == "a":
                        wrapp("\"Anything else you want to talk about?\"")
                        talklist()
                        cmd = talkwhat(cmd, TalkOptions)
        if cmd == "SKELETONS" or cmd == "SK":
            wrapp("The floor is littered with animal skeletons.")
            wrapp("All of them are dry to the bone.")

    while storyProg["roomID"] == 10:
        lbreak()

        wip()

        avail_locs = []
        room_objs = []

        wrapp("You are on the journey to Jorts.")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)





    while storyProg["roomID"] == 1000:
        lbreak()

        wip()

        avail_locs = []
        room_objs = []

        wrapp("")

        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)

        cmd = yesno(cmd)

        convoTree = 1
        TalkOptions = ["NO", "EXAMPLE"]
        talklist()
        cmd = talkwhat(cmd, TalkOptions)
        while convoTree == 1:
            if cmd == "NO" or cmd == "N":
                wrapp("")
                convoTree = 0
            elif cmd == "EXAMPLE" and "EXAMPLE" in TalkOptions or cmd == "E" and "EXAMPLE" in TalkOptions:
                wrapp("")
                cmd == "a"
                TalkOptions.remove("EXAMPLE")
            else:
                wrapp("[CHARACTER] doesn't understand what you meant by that.")
                talklist()
                cmd = talkwhat(cmd, TalkOptions)
            if cmd == "a":
                wrapp("\"Anything else you want to talk about?\"")
                talklist()
                cmd = talkwhat(cmd, TalkOptions)

        if cmd == "SH" or cmd == "SHOP":
            wrapp("You glance at the shop.")
            shopping = 1
            iOne = {
                "itemName": "Item One",
                "status": "5G",
                "itemDesc": "Type the description of the first item here!"
            }
            iTwo = {
                "itemName": "Item Two",
                "status": "10G",
                "itemDesc": "Type the description of the second item here!"
            }
            iThree = {
                "itemName": "Item Three",
                "status": "15G",
                "itemDesc": "Type the description of the third item here!"
            }
            catalog = [iOne, iTwo, iThree]
            while shopping == 1:
                cmd = cashier(catalog, gold, cmd)
                if cmd == "R" or cmd == "RIDDLER'S FLASK":
                    gold = shop("RIDDLER'S FLASK", catalog, gold)
                if cmd == "M" or cmd == "MAGIC SWORD":
                    gold = shop("MAGIC SWORD", catalog, gold)
                if cmd == "W" or cmd == "WAND OF GAMELON":
                    gold = shop("WAND OF GAMELON", catalog, gold)
                if cmd == "QUIT" or cmd == "Q":
                    wrapp("\"Thanks much!\"")
                    shopping = 0
#Note to self:
#THIS IS EXAMPLE CODE YOU BLITHERING IDIOT DON'T TRY AND EDIT IT
