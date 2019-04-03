from EnJinn.comnd import lbreak, optlist, what, cmd, inventory, talkwhat, gold, textSpeedGLOBAL, textWidthGLOBAL, name, tutorialWhat, addRemove, talklist, yesno, textSettings, wrapp, shop, cashier, addInv, instaWrapp, vardef, wip

from EnJinn.comnd import textInit

import sys
settings = sys.argv

localSpeed = settings[1] 
localWidth = settings[2]

textInit(localSpeed, localWidth)

game = 1

storyProg = {}

varlist = ["caseyBug1","tutDone","roomID","backpackCheck","talkwizcheck","momGreet","bedroomIntro","lowerTownIntro","gertieGreet","wizToTabbs","tempTextStore","ladybugdiscuss","smithIntro","oldManIntroTreeside","presentCount","CHouseintro","LukeTalk","room7intro"]

storyProg = vardef(storyProg, varlist)

storyProg.update({"roomID":100})

prologue = 1
if prologue == 1:
    #Prologue text.
    wrapp("Welcome to Tabbs.")
    wrapp("This is a text-based adventure game.")
    wrapp("If you wish to learn more about how to play the game, please type HELP or H now. If you would like to edit display settings, type SETTINGS or S. Type anything but HELP, H, SETTINGS, or S to keep playing.")
    settingsSet = 0
    yeetBye = input(">").upper()
    if yeetBye == "HELP" or yeetBye == "H":
        wrapp("Type HELP once more to gain the assistance you so desire.")
        exit()
    if yeetBye == "SETTINGS" or yeetBye == "S":
        textSettings()
    wrapp("Good.")
    wrapp("You have chosen well.")
    wrapp("Player...")
    goodName = 0
    while goodName == 0:
        name = input("What is your name? ").capitalize()
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
            wrapp("You can't take tabbs's name...")
            wrapp("Pick something elssse.")
        if name == "Jai":
            wrapp("The true name.")
            #wrapp("Unfortunately, already taken...")
        if name == "":
            wrapp("Please, enter your name.")
        if name == "Luke":
            wrapp("Yeesh, this is awkward. Can I ask you to pick a different name?")
        if name != "Tabbs" and name != "Casey" and name != "Mom" and name != "Vimm" and name != "Dad" and name != "Gertrude" and name != "" and name != "Luke":
            goodName = 1
        lbreak()
    wrapp("Your name is " + name + ".")
    wrapp("Your best friend, Casey, is [     ].")
    wrapp("Now awaken, Chosen, and face your fate...")
    lbreak()
    wrapp("You wake up, rolling out of bed.")
    wrapp("Yawning, you stretch, making a bit of a silly noise as you do so.")
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
                    "From Casey's family, you got a hand drawn picture book of you and Casey being crime fighting superheroes, Casey with a sword and you with a shield."
                )
                wrapp(
                    "It's the best present you've ever recieved. You just wish you could have told Casey that in person."
                )
                wrapp(
                    "For now, her dad said he would pass along the message."
                )
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
            cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = tutorialWhat(cmd, avail_locs, inventory, room_objs, storyProg, gold,textSpeedGLOBAL, textWidthGLOBAL, name)

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
                "You think that your town is wonderful. Wellside is paved with cobble, connecting all three of the buildings to the small square at the well, where you had your birthday festival yesterday. There's also a path leading to the road."
            )
            wrapp(
                "And the Wellside buildings are always so energized! There's your house, of course, which is where you live. There's the blacksmith's home, which doubles as his workplace. He and his husband, the guard, sleep there. In his workshop, the blacksmith works day and night on new mechanical devices, like the one he gave you for your birthday, as well as old-fashioned swords and shields and the like. You've been there with your mom to pick up commissions, and it's always a fantastic experience. Then there's Gertrude's house, where she does her seamstress and tailor work, as well as magicking up fabric and tools when people need them. You've never been inside, but you're sure it's absolutely magical."
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
            wrapp("Gertrude is knitting.")
            wrapp(
                "You can hear the slight crackling of the furnace in the smithy behind you, as well as the occasional clang of tools."
            )
            wrapp("The guard is at his post.")
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
        if cmd == "WELL" or cmd == "WE" and storyProg["wizToTabbs"] == 0:
            wrapp("You look down the well.")
            wrapp("That's really deep!")
            wrapp(
                "Silently, you make the same wish you made yesterday, when you blew out your candles."
            )
            wrapp("You hope the wish reaches Casey.")
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
        room_objs = ["LOOKOUT", "GIANT TREE", ""]
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
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if cmd == "CASEY'S HOUSE" and storyProg[
                "oldManinCHouse"] == 1 or cmd == "C" and storyProg[
                    "oldManinCHouse"] == 1:
            storyProg.update({"roomID": 6})
            wrapp("You head into Casey's house.")
        if cmd == "OLD MAN'S HOUSE" or cmd == "O":
            wrapp("You try the door. Locked.")
            wrapp(
                "You're not really sure why you expected anything different.")
        if cmd == "WELLSIDE PATH" or cmd == "W":
            wrapp("You head back towards Wellside, watching your feet as you walk down the path.")
            storyProg["roomID"] = 3
    while storyProg["roomID"] == 6:  #Casey's house w/Monty encounter
        lbreak()
        wrapp("You are in Casey's house, in the main room of the lower floor.")
        avail_locs = ["OUTSIDE","UPSTAIRS"]
        room_objs = ["WORKSHOP","CASEY'S DAD"]
        if storyProg["oldManinCHouse"] == 1:
            wrapp("Casey's house is similar to yours, in that the lower floor is almost entirely comprised of one large room, containing the kitchen, entertainment space, and a table, but it's different in its approach to each aspect. Rather than the sparse, functional design your house sports, the design of Casey's house prepares for everything.")
            wrapp("The kitchen wall is lined with shelves and drawers filled with every ingredient you've heard of and more, plus tools and utensils for food and crafting alike. The countertops have several preperation stations where you and Casey labored over cakes, cookies, and arts and crafts.")
            wrapp("Casey often referred to this part of the kitchen as \"The Workshop,\" and aside from her dad occasionally complaining about wood shavings that found their way into the skillet drawer, it's overall a favorable layout for everyone.")
            wrapp("In addition to all of this, Casey's house has a second floor, the only house to have one in town, excluding your own, of course. This is supported by a wooden beam in the middle of the room, which you've accidentally sleepwalked into more times than you care to admit.")
            wrapp("The first thing you notice when you enter is Casey's dad sitting on a couch, listening to Old Man Monty talk. You're not good enough at reading faces to be sure, but Casey's dad could be holding back tears.")
            wrapp("The old man stops saying what he was going to say.")
            wrapp("\"Ah, " + name + ", you're here,\" he says. He turns to Casey's dad. \"I'm sorry, Luke, I'm going to have to cut this a little short. " + name  + ", please meet me outside. We, ah, have some things that need dicussing.\"")
            wrapp("Monty gets up, leaving Casey's dad sitting on the couch, staring at the old man's retreating figure.")
            wrapp("Luke sits there a moment longer, watching as the door closes, before turning to you slowly, and attempting to put on a happy face. He gives up halfway through the attempt.")
            wrapp("\"Casey's gone,\" he says. \"Thought you ought to know.\"")
            storyProg.update({"oldManinCHouse":0})
        else:
            wrapp("Casey's dad is sitting on the couch, looking somehow lost.")
        optlist()
        cmd, storyProg, textSpeedGLOBAL, textWidthGLOBAL, name, gold, inventory = what(
            cmd, avail_locs, inventory, room_objs, storyProg, gold,
            textSpeedGLOBAL, textWidthGLOBAL, name)
        if cmd == "CASEY'S DAD" and storyProg["LukeTalk"] == 0 or cmd == "CA" and storyProg["LukeTalk"] == 0: 
          wrapp("You ask Casey's dad what he meant by that.")
          wrapp("He blinks owlishly at you, taking you in your entirety in, before continuing. \"She wasn't in her room this morning,\" said Luke. \" I thought maybe she had somehow... I dunno. She was too sick to move yesterday, it doesn't make sense for her to have somehow snuck out to see you.\"")
          wrapp("Casey's dad sighs. \"And yet, she's not in her room.\"")
          wrapp("\"But don't let my brooding distract you, " + name + ". Was there anything you wanted to talk about?\"")
          convoTree = 1
          TalkOptions = ["CASEY", "MONTY", "ARE YOU OKAY", "NO"]
          talklist()
          cmd = talkwhat(cmd, TalkOptions)
          while convoTree == 1:
              if cmd == "CASEY" and "CASEY" in TalkOptions or cmd == "C" and "CASEY" in TalkOptions:
                 wrapp("\"I don't know, " + name + ", I really don't. She was in bed, still as sick as she was yesterday, when I finally dozed off in the chair. I open my eyes and it's six hours later, and she's gone.\"")
                 wrapp("He shakes his head and puts his head in his hands. \"God, if Isabella were here she'd know what to do.\" He looks like he's about to lament some more, but he starts, as if remembering your presence, and stops talking.")
                 TalkOptions.remove("CASEY")
                 cmd = "a"
              elif cmd == "MONTY" and "MONTY" in TalkOptions or cmd == "M" and "MONTY" in TalkOptions:
                 wrapp("\"Oh, the old man just wanted to ask me what I knew about... Casey's disappearance.\"")
                 wrapp("\"I told him all I knew, but the guy kept asking for more. Asking if I remembered the dream I had before I dozed off, what clothes Casey was wearing... he probably had the best intentions, but he... his delivery was not the most graceful.\"")
                 wrapp("\"Monty is a lot of things, but good at reassuring worried fathers he is not,\" says Casey's father with a small smile. It quickly fades.")
                 TalkOptions.remove("MONTY") 
                 cmd = "a"
              elif cmd == "ARE YOU OKAY" and "ARE YOU OKAY" in TalkOptions or cmd == "A" and "ARE YOU OKAY" in TalkOptions:
                wrapp("\"What? Yeah. Yeah, I am, " + name + ", why do you ask?\"") 
                tempOpts = ["WORRIED","NO REASON"]
                cmd = talkwhat(cmd, tempOpts)
                wrapp("\"Well, that's sweet of you, but I'm just fine. I'm honestly more worried about Casey.\"")
                TalkOptions.remove("ARE YOU OKAY")
                cmd = "a"
              elif cmd == "NO" or cmd == "N":
                  wrapp("\"That's okay,\" says Casey's dad. \"But if you hear anything about Casey, let me know.")
                  convoTree = 0
                  storyProg.update({"LukeTalk":1})
              else:
                  wrapp("Luke doesn't understand what you meant by that.")
                  talklist()
                  cmd = talkwhat(cmd, TalkOptions)
              if cmd == "a":
                  wrapp("\"Anything else you want to talk about?\"")
                  talklist()
                  cmd = talkwhat(cmd, TalkOptions)
        if cmd == "CASEY'S DAD" and storyProg["LukeTalk"] == 1 or cmd == "CA" and storyProg["LukeTalk"] == 1:
          wrapp("\"I'm sorry, " + name + ", I'm feeling a little emotionally drained right now. Can we talk again some other time?\"")
        if cmd == "O" or cmd == "OUTSIDE":
          wrapp("You make your way outside.")
          if storyProg["caseyBug1"] == 1:
              wrapp("As you open the door, you notice the ladybug from earlier fly into the house.")
              wrapp("You're not sure what to make of that.")
              storyProg.update({"caseyBug1":2})
          storyProg.update({"roomID":5})
        if cmd == "WO" or cmd == "WORKSHOP":
          wrapp("The workshop. Or as Casey calls it, The Workshop.")
          wrapp("This is the place you and Casey made countless arts and crafts. And pancakes.")
          wrapp("You're tempted to pull out some stuff and try to start making things, but Casey isn't here, and it's weird to even think about messing with The Workshop alone.")
        if cmd == "U" or cmd == "UPSTAIRS":
          wrapp("You make your way to Casey's room.")
          storyProg.update({"roomID":7})

    while storyProg["roomID"] == 7:
        lbreak()
        avail_locs = ["DOWNSTAIRS"]
        room_objs = ["SKETCHES","ART SUPPLIES","WINDOW"]
        wrapp("You are in Casey’s room.")
        if storyProg["room7intro"] == 0:
          wrapp("Casey’s room is similar to yours, in that it has a windowsill, a bed, and is littered with stuff. But it’s more... Casey, for lack of a better term. The walls have tons of sketches and doodles pinned onto them, of designs for heroes and stories that you and Casey planned out but never got around to finishing.")
          wrapp("In addition to Casey's ever-present art case, Casey’s floor has a few tools and brushes lying around, and some of them are sharp and potentially dangerous. You learned that the hard way once. Casey didn’t stop apologizing every time you saw her for nearly a week.")
          wrapp("Notably, Casey is not in her room as far as you can tell, which lines up with what her dad told you.")
        if storyProg["talkWizCheck"] != 2:
          wrapp("You briefly wonder what the old man wants you for.")
          storyProg.update({"room7intro":1})
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
          storyProg.update({"roomID":6})
        if cmd == "SK" or cmd == "SKETCHES":
          wrapp("You glance at the sketches of armor and people.")
          wrapp("You and Casey spent hours on these. Your drawings aren't as polished as hers, but it didn't matter to either of you, because just thinking of outfits and powers and settings was fun by itself.")
          wrapp("Having a finished product would just be icing on the cake. But cakes tasted just fine without icing, too!")
          wrapp("At one point in time, you began making sketches for a story featuring a shapeshifting demon, but you gave up on that idea. Too ambitious for you.")
          wrapp("Casey tried inventing this huge world full of politics and intrigue, beginning with the main character stopping an assassination, but she couldn't figure out what to name the main character and dropped the project altogether.")
          wrapp("You both came to the conclusion that writing was hard. The pair of you mostly stuck to visual storytelling instead.")
        if cmd == "ART SUPPLIES" or cmd == "AR":
            wrapp("You stare down the art supplies, and specifically, the small wooden case with the word \"ART\" painted on it.")
            wrapp("A gift to Casey from Gertrude and your mother, it's a variation on your backpack, using some of the same spellwork that Gertrude uses to create her fabrics. Rather than being enchanted to have infinite space for infinite items, it's enchanted to have infinite art supplies. All you or Casey need to do is think of what you want to create and the appropriate supply comes out!")
            wrapp("It doesn't, however, have an appropriate disposal method, and you and Casey both were too sentimental to throw out the supplies like regular garbage. So on the floor they stay, and so it shall be.")
            wrapp("You briefly consider taking it. But, no, it's Casey's, and you couldn't seriously entertain that thought for more than a second.")
        if cmd == "WINDOW" or cmd == "WI":
            wrapp("")
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
        TalkOptions = ["NO"]
        talklist()
        cmd = talkwhat(cmd, TalkOptions)
        while convoTree == 1:
            if cmd == "NO" or cmd == "N":
                wrapp("")
                convoTree = 0
            else:
                wrapp(" doesn't understand what you meant by that.")
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
