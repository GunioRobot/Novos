from sys import exit

def conclusion():
    print "You are looking at the huge stone slab that stands between you and your initiation as a Warrior of the Novos."
    bomb_planted = False
    fuse_lit = False

    while True:

        next = raw_input("> ")

        if "plant" in next and "bomb" in next:
            print "The bomb has been planted."
            bomb_planted = True
        elif "light" in next and "fuse" in next and not bomb_planted:
            dead("You light the bomb while still holding it in your hands and blow yourself up.")
        elif "light" in next and "fuse" in next and bomb_planted:
            print "You light the fuse and take a step back. The bomb explodes."
            print "Through the debris and smoke, you see the elders and warriors of the Novos."
            win("They cheer as you emerge triumphant, one of them.")
        else:
            print "You're so close."


def torches():
    print "There are three unlit torches numbered 1 through 3 in the middle of the room."
    print "A fourth torch, lit, hangs off the wall next to you."
    print "There is a door on the far side of the room."
    torch_grabbed = False
    torch_one = False
    torch_two = False
    torch_three = False

    while not torch_grabbed:
        next = raw_input("> ")

        if next == "take torch":
            print "You grab the torch from the wall."
            torch_grabbed = True
        elif next == "open door":
            print "The door won't budge."
        else:
            print "You might want to start by taking the torch off the wall."

    while not torch_two:
        next = raw_input("> ")

        if "light" in next and "three" in next and not torch_three:
            print "You successfully light the torch."
            torch_three = True
        elif "light" in next and "three" in next and torch_three:
            print "It's already lit."
        elif "light" in next and "two" in next and not torch_one:
            print "The torch won't stay lit for more than a few seconds."
        elif "light" in next and "two" in next and torch_one:
            print "You successfully light the torch."
            print "The door suddenly opens."
            torch_two = True
        elif "light" in next and "1" in next or "one" in next and not torch_three:
            print "The torch won't stay lit for more than a few seconds."
        elif "light" in next and "1" in next or "one" in next and torch_three:
            print "You successfully light the torch."
            torch_one = True
        else:
            print "Maybe you should try lighting the torches."

    print "You proceed through the door and find yourself in the room you started in. Only now you have a bomb and a lit torch."
    conclusion()

def bomb():
    print "The only thing in this room is a bomb is sitting on a table."

    next = raw_input("> ")

    if "take" in next and "bomb" in next:
        print "You have picked up the bomb. You proceed to the next room."
        torches()
    else:
        print "Come on man."
        bomb()

def elites():
    print "KABOOM! Debris flies past you as a hole opens up in the far wall."
    print "A band of gnolls armed with rapiers comes dashing in. They look trained."
    enemies = ["first", "second", "third"]
    for i in enemies:
        print "The %s gnoll steps forward and taunts you." % i
        initiated = False
        parried = False
        gnoll_death = False

        while not gnoll_death:
            next = raw_input("> ")

            if "attack" in next and not parried:
                print "The gnoll parries your blow and takes a swing."
                initiated = True
            elif "attack" in next and parried:
                print "You thrust your rapier into the gnoll, driving it between his eyes. He falls to the ground as you withdraw your sword."
                gnoll_death = True
            elif "parry" in next and not initiated:
                print "The gnoll stays focused."
            elif "parry" in next and initiated:
                print "You successfully parry the gnoll's strike."
                parried = True
            else:
                dead("In one swift and graceful motion, the gnoll imaples your throat with his rapier.")

    print "Beyond the hole in the wall, you see another room. Would you like to save your progress? (y/n)"

    next = raw_input("> ")

    if next == "y":
        print "Yeah... alright... the game's saved now..."
        bomb()
    elif next == "n":
        print "I was only asking to be polite."
        bomb()
    else:
        dead("One of the gnolls opens his eyes and jolts up and sends his rapier careening through your groin.")

def dardon():
    print "Brace yourself adventurer. You have entered a dardon's lair!"
    print "It will take more than pure strength to fell this beast."
    print "The dardon lets out a deafening roar as it stamps its feet."
    print "The beast lowers its head and makes a charge right for you!"
    dardon_hp = range(0,5)
    exposed = False
    for i in dardon_hp:

        next = raw_input("> ")

        if "attack" in next and not exposed:
            dead("You attempt to attack dardon's massive skull with your rapier. The blade snaps immediately, as does every bone in your body.")
        elif next == "dodge" and not exposed:
            print "You dodge the beast's charge! He exposes his fleshy backside!"
            exposed = True
        elif "attack" in next and exposed:
            print "You pierce the beast with your rapier. He lets out a hideous shriek and turns around. He's charging again!"
            exposed = False
        elif next == "dodge" and exposed:
            dead("Unsatisfied with your successful dodge you perform another, giving dardon time to turn around and charge you again. His massive skull crushes every bone in your body.")
        else:
            dead("As you bumble about, the beast collides into you. His massive skull crushes every bone in your body.")
    next = raw_input("> ")

    if "attack" in next:
        print "You pierce the beast with your rapier. Letting out one last pathetic roar, he collapses."
        elites()
    else:
        dead("The dardon spins around wildly, knocking your head clean off.")

def henchmen():
    print "A goblin and bugbear stand behind him, somewhat unsure of themselves."
    enemies = ["troll", "goblin", "bugbear"]

    for i in enemies:
        print "The %s steps forward and looks around nervously." % i

        next = raw_input("> ")

        if next == "attack %s" % i:
            print "The %s's lifeless body falls to the ground." % i
        else:
            dead("The %s collects himself, takes a mighty swing and caves your head in." % i)
    print "Beyond the pile of your foes' pathetic corpses, you see a door."

    next = raw_input("> ")

    if next == "open door":
        print "You enter the next room."
        dardon()
    else:
        print "You reconsider and enter the next room instead."
        dardon()


def armory():
    print "This room is an armory."
    print "To your left is a rack of weapons and to your right is a rack of armor."
    print "There is a door in front of you."
    armed = False
    armored = False

    while True:
        next = raw_input("> ")

        if "take" in next and "weapon" in next and not armed:
            print "You take a rapier from the rack and equip it."
            armed = True
        elif "take" in next and "weapon" in next and armed:
            print "One per customer."
        elif "take" in next and "armor" in next and not armored:
            print "You don a fine suit of armor."
            armored = True
        elif "take" in next and "armor" in next and armored:
            print "One per customer."
        elif "open" in next and "door" in next and not armed and not armored:
            dead("As you open the door, a troll on the other side swings his hammer and crushes your face.")
        elif next == "open door" and armed and armored:
            print "As you open the door, a troll on the other side swings his hammer and connects with your face. The blow glances off your fancy helmet."
            henchmen()
        else:
            print "Maybe you should do something logical instead."

def immolation():
    print "You stand before a straight, narrow hallway."
    print "There is a pressure plate a few steps ahead."
    print "Some of the bricks in the wall are coming loose."
    brick_taken = False
    brick_thrown = False

    while True:
        next = raw_input("> ")

        if next == "take brick" and not brick_taken:
            print "You pry a brick loose from the wall."
            brick_taken = True
        elif next == "take brick" and brick_taken:
            dead("You attempt to take another brick but stumble onto the pressure plate. A stream of flames erupts and immolates you.")
        elif next == "throw brick" and brick_taken:
            print "The brick lands on the pressure plate. A stream of flame erupts over the brick. A door opens at the end of the hallway."
            brick_thrown = True
        elif next == "throw brick" and not brick_taken:
            dead("You tumble over yourself and land on the pressure plate. A stream of flame erupts and immolates you. Try taking a brick first.")
        elif "walk" in next or "door" in next and brick_thrown:
            print "You walk down the hallway and enter the next room."
            armory()
        elif "walk" in next or "door" in next or "pressure" in next or "plate" in next and not brick_thrown:
            dead("You mosey on down the hallway and step on the pressure plate. A stream of flame erupts and immolates you.")
        else:
            print "You look around nervously."

def vine_pit():
    print "You walk through the door and stand before a spiked pit."
    print "A vine hangs down from the ceiling in front of you."

    next = raw_input("> ")

    if "swing" in next or "vine" in next:
        print "You take hold of the vine and swing across the pit."
        immolation()
    else:
        dead("You slip and fall into the pit. Needles impale your body from head to toe.")

def entrance():
    print "You walk through the door into a small chamber."
    print "There are doors to your left and right."
    while True:
        next = raw_input("> ")

        if "left" in next:
            print "The door won't budge."
        elif "right" in next:
            vine_pit()
        else:
            print "You're losing the game."

def intro():
    """Introduction to the game."""
    print """You enter the Cavern of Rhama. An enormous stone slab falls from the ceiling behind you and shuts you in. If you manage to navigate this treacherous place, you will join the ranks of the mighty Novos warriors. If not, you will surely find great company in the other corpses that litter the cavern floors. The only way to go is a door in front of you.

    Proceed? (y/n)"""

    next = raw_input("> ")

    if next == "y":
        entrance()
    elif next == "n":
        print "Be seeing you..."
        exit(0)
    else:
        dead("If you can't follow simple instructions, the Novos will find someone who can.")

def dead(why):
    print why, "Better luck next time."
    exit(0)

def win(why):
    print why
    exit(0)

intro()
