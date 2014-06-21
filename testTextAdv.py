#! /usr/bin/env python3

# Nicholas' tutorial doesn't use classes and objects.  It might make the game
# more difficult to scale. I'm going to see if I can improve upon his design a
# bit.  This is some experimental code that I am playing with.

from random import choice as randomchoice

#######################
####### Classes #######
#######################

class Location:
    """locations in the game"""
    def __init__(self, shortDesc, longDesc, firstDesc, tkItems, permItems):
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.firstDesc = firstDesc
        self.tkItems = tkItems
        self.permItems = permItems


class TkItem:
    """"Items you can take in the game."""
    def __init__(self, shortDesc, longDesc, firstDesc, takeDesc):
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.firstDesc = firstDesc
        self.takeDesc = takeDesc


class PermItem:
    """"Items that are permanent and can't be taken."""
    def __init__(self, shortDesc, longDesc, firstDesc, takeDesc):
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.firstDesc = firstDesc
        self.takeDesc = takeDesc

# class NPC:
#     """Non-player character. How should I do dialogue?"""
#     def __init__(self, shortDesc, longDesc, firstDesc, speech):
#         self.shortDesc = shortDesc
#         self.longDesc = longDesc
#         self.firstDesc = firstDesc
#         self.speech = speech


#########################################
####### Locations and their items #######
#########################################

# The Beach; Location 0

# Items that are found in the beach
bonfire = PermItem(
'a bonfire',  # Short

'A toxic bonfire complete with, plastic, tires and black smoke.',  # Long

"""As you approach, the flames from the bonfire gently flicker in the wind.
Upon closer inspection, you notice it's fueled by melted plastic containers
and old car tires.  It's no wonder huge plumes of black smoke billow into
the moon-lit sky. It's eerily beautiful.

As you wonder who decided to commit this environmental atrocity, the wind shifts
and you get a lung full of the toxic fumes. Practically choking to death, you
drop to the sand, curl into the fetal position and cough for a solid 5 minutes.
You wipe the tears from your face, stand back up, and take a few minutes to
compose yourself.  Fuck...""",  # First

"""WHAT? Are you crazy? I'll leave the bonfire where it is.""")

sand = PermItem(
'sand',  # short description
"Small grains of sand. It's everywhere.",  # Long

"""Sand. Billions and billions of tiny granular material that humanity has used
to construct glass, computer chips, and double D breasts.  It's great, but you
don't need to concern yourself with double D's right now.""",  # First

"""Sand is great, but you don't need any.""")

water = PermItem(
'sea water',  # Short
"It's sea water.",  # Long

"""You look at the dark sea water and step into the shallow water. The wet
sand seeps between your toes. It's rather soothing here.""",  # First

"""There is plenty of it. You can comeback here and enjoy it any time""")

# Lists of the items to be put into the beach location object
beachPermItems = [bonfire, sand, water]
beachTkItems = []

# Location(short description, long description, first description, takable
# items, and permanent items)
beachLoc = Location("Shoreline",
"""You are on the beach facing the shoreline. Along the beach, there is a bright
bonfire to your left. You can see a small bungalow to the Southwest and a cliff
side to the Southeast.""",

"""You are on the beach facing the shoreline. Along the beach, there is a bright
bonfire to your left. You can see a small bungalow to the Southwest and a cliff
side to the Southeast.""",

beachTkItems, beachPermItems)


# Outside bungalow # 2

outBungalowPermItems = []
outBungalowTkItems = []

outBungalowLoc = Location(
"In front of a bungalow.",

"""You are standing in front of an old dilapidated bungalow. The thatch roof has
caved in a bit, but it is still standing. Looks safe enough to enter. You see
the cliff side to the East and the beach to the North.""",

"""You are standing in front of an old dilapidated bungalow. The thatch roof has
caved in a bit, but it is still standing. The door is long gone. It looks safe
enough to enter. You see the beach to the North and a cliff side to the East.
""",

outBungalowTkItems, outBungalowPermItems)


# Inside the Bungalow #2
pillow = PermItem(
"a pillow",

"""The pillow lies naked on the foot of the bed. It looks damp and covered
with black mold.""",

"""The pillow lies naked on the foot of the bed. It looks damp and covered
with black mold.  Your nose begins to run just getting close to it.

You begin to ponder what terrible atrocities the pillow's cover must have
been subjected to. Did someone used it as a substitute for toilet paper?
Maybe it became an improvised gag? Or a make-shift contraceptive?
Where is it now?! You had to know! Well... sort of.""",

"""You might be allergic to black mold. I think we all are. Lets leave it
where it is.  Besides, after seeing that bed, who knows what fluids it has been
soaked in.""")

bed = PermItem(
"a bed",

"""The bed has seen some better days. As you inspect the mattress, you
notice it has taken on a yellow and brown hue.  There are a few few crusty
looking spots.  It must have been a popular teenage hangout. You spot a
pillow near the foot of the bed.""",

"""The bed has seen some better days. As you inspect the mattress, you
notice it has taken on a yellow and brown hue.  There are a few few crusty
looking spots.  It must have been a popular teenage hangout. You spot a
pillow near the foot of the bed.""",

"""...the crust...""")

counter = PermItem(
"a counter",

"""A greasy kitchen counter. There is a stove embedded in the middle and a
small bucket standing on its right.""",

"""It's a kitchen counter.  You notice it is slick to the touch. It also
has some signs of water damage. There is a stove embedded in the middle and a
small bucket standing on its right.""",

"""You'd probably need a small crane to lift this.""")

lard = PermItem(
"a bucket of lard",

"""The bucket is filled to the brim with lard. It has slowly bubbling over
from the heat.  It looks to be a popular destination for insects looking to
drown.""",

"""You spot a brown wooden bucket. It is overflowing with a thick, cream colored
liquid. Probably lard. It's bubbling over at the top.  Fruit-flies hover above
the substance, and can't seem to stop themselves from dying in it.""",

"""It's probably best left here. There is no handle, and it smells atrocious."""
)

stove = PermItem(
"a stove",

"""The stove is slick with grease and studded with charred bits of meat. You try
to turn it on, but there is no spark or any propane.""",

"""The stove is slick with grease and studded with charred bits of meat. You try
to turn it on, but there is no spark or any propane.""",

"""It's a part of the counter. It's also pretty useless.""")

net = TkItem(
"a mosquito net",

"""An old mosquito net.  DAMN they be lots of holes.""",

"""You see an old mosquito net hanging over the bed.  It's got a lot of holes
in it.""",

"""You rip some of the mosquito net down and shove it down your pants. For
safe-keeping.""")

inBungalowPermItems = [pillow, bed, counter, lard, stove]
inBungalowTkItems = [net]

inBungalowLoc = Location(
"inside the bungalow.",

"""You are inside the bungalow. There is an old bed to your right and a counter
on your left. You can see the exit behind you.""",

"""You are inside the bungalow. There is an old bed to your right and a counter
to your left.""",

inBungalowTkItems, inBungalowPermItems)


# Cliffside #3
rocks = PermItem(
"a pile of rocks",

"""They are just rocks. C'mon. I just put them here to bother you. I'm trying to
be clever and meta.""",

"""These rocks look just like the ones back at home: smooth, round and would fit
nicely in a sack.  Although, it's no time to be playing these rocks right now.
You can play with them when you get home.""",

"""You try to pick up a few rocks, but realize you already have a small pair
lying unused in your sack. You should probably use them first."""
)

opening = PermItem(
"a cave opening",

"""You might be able to fit in there, but its way too dark to see anything.""",

"""The opening is very small. You shout inside and hear an echo.  Must be a
cave of some sort. You think you could fit through the hole, but it's too risky
to be squeezing yourself through dark spots.""",

"""You can't take the opening, what the fuck?"""
)

stick = TkItem(
"a stick",

"""It's a fresh wooden stick.  Its the only interactive phallic item in the
game!""",

"""A huge gnarled stick. Looks like the optimal girth for your hands.""",

"""You reach down and pick up this gnarled stick.  Impressed with the
girth of this enormous stick, you strap it to your side by the band of your
tightie whities."""
)

cliffSideTkItems = [stick]
cliffSidePermItems = [rocks, opening]

cliffSideLoc = Location(
"a cliff side",

"""A huge cliff side stands before you. It's much too steep to climb, but you
see an opening among the cracks large enough that you could fit through.
You can see the shoreline to the North and a bungalow to the West.""",

"""A huge cliff side stands before you. It's much too steep to climb and seems
to extend all the way to the bungalow preventing you from going further South.

Although, you do see an small opening among the cracks. There are some rocks
laying at the base of the cliff.""",

cliffSideTkItems, cliffSidePermItems

)
darkCaveTkItems =[]
darkCavePermItems = []

darkCaveLoc = Location(
"a cave",

"""It looks like the cave is pretty deep.  But too bad the developer of this
game was too lazy to continue. Game Over.

You can quit by typing 'quit'""",

"""CONGRATULATIONS. You are got in the cave. You beat the game. Pat yourself on
the back.  Seriously, thanks for playing my first game. It was a demo so.. yeah.
It was a crappy, ending to a very crappy game. Sorry for wasting your time. I'll
go make a better one.

You can quit the game by typing 'quit'""",

darkCaveTkItems, darkCavePermItems
)

wrappedStick = TkItem(
"a wrapped-stick",

"""It's the gnarled stick you wrapped with the mosquito net.  It looks almost
like a torch. Although, it's not quite there. It would burn out pretty fast.""",

"""You wrap your stick with the mosquito net. Right on one tip. Kinda looks like
a giant... wrapped-stick""",

"""You already have it strapped to your loins."""
)

torch = TkItem(
"a torch",

"""It's a makeshift torch composed of a stick, mosquito net and lard.""",

"""You are special person. You made homemade torch out of mosquito net, and
stick. Then had good time double-dipping the tip in lard. This should burn
nicely.""",

"""You already have it. The lard from your homemade torch is soaking through
your boxers."""
)

litTorch = TkItem(
"a lit-torch",

"""Your torch is fucking on fire.""",

"""Congratulations, your torch is on fucking fire. Just like how your penis
feels when you wee.""",

"""You already have it. It's burning a hole in your jock strap."""
)

##########################################
### Item Indexes and Location Synonyms ###
#########################################


# A dictionary of all objects in the game.  This will help with synonyms
obj_synonyms = {
    # objects that can be taken
    'stick': 0, 'sticks': 0, 'branch': 0, 'wood': 0, 'drift-wood': 0,
    'mosquito': 1, 'net': 1,
    'wrapped-stick': 2, 'wrapped': 2,
    'torch': 3,
    'lit-torch': 4,

    # permanent objects
    'bonfire': -1, 'fire': -1, 'flame': -1,
    'bed': -2, 'mattress': -2,
    'pillow': -3, 'cushion': -3,
    'rocks': -4, 'rock':-4, 'boulders': -4,
    'sand': -5, 'grains': -5,
    'counter': -6, 'table': -6,
    'stove': -7, 'oven': -7,
    'lard': -8, 'bucket': -8, 'container': -8, 'fat': -8, 'oil': -8, 'tub': -8,
    'water': -9, 'ocean': -9, 'sea': -9, 'salt': -9,
    'opening': -10, 'cave': -10, 'crack': -10, 'cracks': -10, 'entrance': -10,
    'hole': -10
}

obj_keys = {
    # objects that can be taken
    0: stick,
    1: net,
    2: wrappedStick,
    3: torch,
    4: litTorch,

    # perminant objects
    -1: bonfire,
    -2: bed,
    -3: pillow,
    -4: rocks,
    -5: sand,
    -6: counter,
    -7: stove,
    -8: lard,
    -9: water,
    -10: opening
}


################################################
##### Movement, Map, Inventory and Actions #####
################################################


# A dictionary of all possible directional movements and their indexes
dirs = {'north': 0, 'n': 0, 'south': 1, 's': 1,
        'west': 2, 'w': 2, 'east': 3, 'e': 3,
        'northeast': 4, 'ne': 4, 'southeast': 5, 'se': 5,
        'northwest': 6, 'nw': 6, 'southwest': 7, 'sw': 7,
        'up': 8, 'u': 8, 'down': 9, 'd': 9,
        'in': 10, 'enter': 10, 'on': 10, 'out': 11, 'exit': 11, 'off': 11}


# A variable for current location, starts at the beach
current_loc = 0

# A list that stores all the areas that have been visited and lists
visited = []

# A matrix of all the possible paths on the map
dungeon_map = [
    # n,  s,  e,  w,  ne, nw, se, sw, up, dn, in, out
    [-1, -1, -1,  -1, -1, -1,  3,  1, -1, -1, -1, -1],  # 0, beachLoc
    [ 0, -1,  3,  -1,  0,  0, -1, -1, -1, -1,  2, -1],  # 1, outBungalowLoc
    [-1, -1, -1,  -1, -1, -1, -1, -1, -1, -1, -1,  1],  # 2, inBungalowLoc
    [ 0, -1, -1,   1,  0,  0, -1, -1, -1, -1, 400,-1],  # 3, cliffsideLoc
    [-1, -1, -1,  -1, -1, -1, -1, -1, -1, -1, -1,  3],  # 4, darkCaveLoc
]

# Certain areas require an item to access will use special_move function
special_locs = {400: litTorch}

# List of tuples of possible combinations of items
combinations = [
    (stick, net, wrappedStick),  # combining the stick and net = wrapped stick
    (wrappedStick, lard, torch),# etc
    (torch, bonfire, litTorch)]

# A This will help tie in the
# dungeon map values with the location objects during movement
dungeon_locs = [beachLoc, outBungalowLoc, inBungalowLoc, cliffSideLoc,
                darkCaveLoc]


# List of inventory objects and if we seen it
# I hear having global variables in games are a bad idea. How do we get around
# using them?
inventory_list = []
seen_item = []

# Controls what description should be given for the location
def describe_loc(locNum):
    global visited
    loc = dungeon_locs[locNum]
    # The first time we see an area, print first description. This is the more
    # interesting description
    if loc not in visited: 
        print(loc.firstDesc, end='')
        visited.append(loc)
        tkLen = len(loc.tkItems)
        # Print the takable items in the location. This way once the items are
        # in the player's hands, it dissapears from the location description. 
        # It could also add a description work if we added the drop command.
        if tkLen > 0:
            print(" You also see ", end='')
            if tkLen > 1:
                for i in range(tkLen-1):
                    print(loc.tkItems[i].shortDesc + ', ', end='')
            else:
                print(loc.tkItems[0].shortDesc + '.')
    else:
        # Once the area has been visited, use the simple description so the
        # player doesn't get annoyed
        print(loc.longDesc)

# Function to describe an item. Also changes the description whether or not if
# it is the first time the player has looked at the item.
def describe_item(itemObj):
    global seen_item
    if itemObj not in seen_item:
        print(itemObj.firstDesc + '\n')
        seen_item.append(itemObj)
    else:
        print(itemObj.longDesc)


# Function to examine items and location
def examine(args):  # examine = look
    if not args:
        describe_loc(current_loc)  # first or long description
    elif args[0] not in obj_synonyms:
        print("I don't know what that is. Likely, I don't understand you. See "
              "help for details.")
    else:
        curr = dungeon_locs[current_loc]
        # Check and see if the item object is in the inventory or location
        # Check the player input with object synonym list to get its key
        # number
        objnum = obj_synonyms[args[0]]
        # Now take the key, and look up the item object
        itemObj = obj_keys[objnum]
        if itemObj not in inventory_list and itemObj not in curr.tkItems and itemObj not in curr.permItems:
            print("I don't see that here.")
        else:
            describe_item(itemObj)

# Function to add a takable item object to the inventory and remove it from
# location when a player decides to take an item.
def add_inven(itemObj):
    global current_loc
    curr = dungeon_locs[current_loc]
    if itemObj not in inventory_list:
        inventory_list.append(itemObj)
        if itemObj in curr.tkItems:
            curr.tkItems.remove(itemObj)

# Function to remove an item from the inventory and place it in the location
# when a player drops the item object
def remove_inven(itemObj):
    global current_loc
    curr = dungeon_locs[current_loc]
    if itemObj not in curr.tkItems:
        curr.tkItems.append(itemObj)
        if itemObj in inventory_list:
            inventory_list.remove(itemObj)

# Function to look up inventory
def inven(args):
    global inventory_list
    print("You have: ")
    invLen = len(inventory_list)
    if invLen < 1:
        print("nothing between your legs ... err ... in your inventory.")
    else:
        for i in range(invLen):
            x = "{num}) ".format(num=i+1) + inventory_list[i].shortDesc
            print(x)
        print('All neatly tucked into your gorgeous white undies.')

# Function to take an object. When taking the item from a location, it needs to
# be added to the player inventory and removed from the location. It also 
# outputs a description.
def take(args):
    if not args:
        print("You must specify an object.")
    else:
        global inventory_list, current_loc
        invLen = len(inventory_list)
        currTk = dungeon_locs[current_loc].tkItems
        if args[0] == "all":
            if len(currTk) < 1: #if the tkItems list in the loc has no objects
                print("There is nothing to take")
            else:
                print("You shove ", end='')
                if invLen == 1:
                    add_inven(currTk[0])
                    print(currTk[0] + 'into your tights.')
                else:
                    # All this code for punctuation.... worth it?
                    for i in range(len(currTk)-1):
                        add_inven(currTk[i])
                        print(currTk[i].shortDesc + ', ', end='')
                    add_inven(currTk[0])
                    print(currTk[0] + 'into your tights.')

        else:
            if args[0] not in obj_synonyms:
                print("I don't know what that is. Are you smoking?")
            else:
                takeobj(args[0])

# If you take one by one...
def takeobj(arg):
    global inventory_list, current_loc
    curr = dungeon_locs[current_loc]
    itemKey = obj_synonyms[arg]
    itemObj = obj_keys[itemKey]
    if itemObj in inventory_list:
        print("You already have that item tucked snuggly against your balls you dunce!")
    elif itemObj not in curr.tkItems and itemObj not in curr.permItems:
        print("I don't see that here, man.")
    else:
        # if you take a permanent object print the take description but don't
        # modify the inventory
        if itemObj in curr.permItems:
            print(itemObj.takeDesc)
        else:
            print(itemObj.takeDesc)
            add_inven(itemObj)

# Combining items!
def combine(args):
    if len(args) < 3:
        print("You must specify two objects and join them with an 'and' or 'with'"
              " E.g. 'combine [item1] and [item2]'")
    else:
        if args[0] not in obj_synonyms:
            print("I don't know what {} is.".format(args[0]))
        elif args[2] not in obj_synonyms:
            print("I don't know what {} is.".format(args[0]))
        else:
            itemObj1 = obj_keys[obj_synonyms[args[0]]]
            itemObj2 = obj_keys[obj_synonyms[args[2]]]
            print("You try to combine {} and {}. ".format(
                itemObj1.shortDesc, itemObj2.shortDesc), end='')
            # now check the combinations list to see if the two args can combine
            # to give you a new item.
            comboCheck(itemObj1, itemObj2)


# Check if we can combine items. If both objects are part of the same tuple in
# the combination list, then add the 3rd item or the combined item into the
# players inventory and remove any items used up (only tkitems not perm items)
def comboCheck(itemObj1, itemObj2):
    global combinations, inventory_list
    for tup in combinations:
        if itemObj1 in tup and itemObj2 in tup:
            inventory_list.append(tup[2])
            if itemObj1 in inventory_list:
                inventory_list.remove(itemObj1)
            if itemObj2 in inventory_list:
                inventory_list.remove(itemObj2)
            print(tup[2].firstDesc)
            return
    randText = randomchoice(["That didn't work.", "It no work buddy",
                             "That was a stupid idea.", "HAHAHAHA, no."])
    print(randText)

# This is Nicholas' original code. If you wanted a drop command, it would be
# much like the take command. Add item to location, remove item from inventory
# and describe the item being dropped.
# def drop(args):
#     global inventory, items
#     if not args:
#         print("You must specify an object.")
#     else:
#         if not args[0] in obj:
#             print("I don't know what that is.")
#         else:
#             objnum = obj[args[0]]
#             if not objnum in inventory:
#                 print("You don't have that.")
#             else:
#                 print("Done.")
#                 inventory.remove(objnum)
#                 items[current_section].append(objnum)

# function used to direct play to new locations on dungeon map.
def move(direct):
    global current_loc
    # goes into our dungeon_map matrix, and pulls out value of where to go next
    newsect = dungeon_map[current_loc][direct]
    if newsect == -1:
        print("You can't go that way.")
    elif newsect > 99:
        # send this special value to decode function
        special_move(newsect)
    else:
        current_loc = newsect
        describe_loc(current_loc)

# Help deal with special locations. It decodes direction if condition is met
# in this case, if a specific item is in inventory.
def special_move(newsect):
    global inventory_list, special_locs, current_loc
    if special_locs[newsect] in inventory_list:
        newsect = int(newsect / 100)  # secret algorythm!
        current_loc = newsect
        describe_loc(current_loc)
    else:
        print("You can't go in there. Maybe you can find something to help.")


def north(args):
    move(0)


def south(args):
    move(1)


def east(args):
    move(2)


def west(args):
    move(3)


def northeast(args):
    move(4)


def northwest(args):
    move(5)


def southeast(args):
    move(6)


def southwest(args):
    move(7)


def up(args):
    move(8)


def down(args):
    move(9)


def _in(args):
    # 'in' is a delimeter, and cannot be used as a funcname without entailing
    # invalid syntax
    move(10)


def out(args):
    move(11)


def go(args):
    if not args:
        print("You must specify a direction.")
    else:
        if not args[0] in dirs:
            print("I don't understand where you want to go.")
        else:
            move(dirs[args[0]])

def execprint(x):
    line = x.split()
    for c in ',:':
        line = c.join(line).split(
            c)  # Also, get rid of `c` that's been there first
    if line:
        if line[0] not in verblist:
            print("I don't understand that.")
        else:
            func = verblist[line[0]]  # look for first word in verblist
            args = line[1:]  # What follows first word are arguments
            func(args) # use the arguments for the verb function


def _help(args):
    print(HELP)


def _quit(args):
    global playing
    playing = False
    print("Quiting the game. Thanks for playing. Say 'bye'")


verblist = {
    'take': take, 'get': take, 'pick': take, 'hold': take,
    # 'drop': drop, 'throw': drop, 'toss': drop,
    'look': examine, 'l': examine, 'examine': examine, 'x': examine,
    'read': examine, 'r': examine, 'describe': examine,
    'combine': combine, 'use': combine,
    # can't use 'd' because of going down
    'inventory': inven, 'i': inven, 'items': inven, #'die': die,
    'quit': _quit,
    'help': _help,
    # 'save': save, 'restore': restore,
    'go': go,
    'north': north, 'n': north, 'south': south, 's': south,
    'east': east, 'e': east, 'west': west, 'w': west,
    'northeast': northeast, 'ne': northeast, 'southeast': southeast,
    'se': southeast,
    'northwest': northwest, 'nw': northwest, 'southwest': southwest,
    'sw': southwest,
    'up': up, 'u': up, 'down': down, 'd': down, 'in': _in, 'out': out,
    'on': _in, 'off': out, 'enter': _in, 'exit': out,
}


HELP = """
Instructions: This is a pretty rudimentary text adventure game that is limited
in how it can interpret your input.

* Movement: To move to a different location on the map, simply type a one word
direction.
E.g. 'north', 'n', 'southeast', 'in', etc

* Actions: There are 3 primary actions you can perform. 1) 'look', 2)'take' and
3) combine.  For the first 2 simply type "[action] [item]". No need for any
prepositions.  For combining, you need to type
"combine [item1] with/and [item2]"

Inventory: Type "inventory" to see what you are carrying.

* If you would like to quit the game, type 'quit'
"""


HEADING =(
"""\n\nWelcome to my first text adventure. It's a small demo I created to learn
Python and user interactivity. Thanks for giving it a try. -Brian

*** Please type 'help' for instructions and 'quit' to exit the game. ***

You open your eyes and see half a moon looming above. It's dark. You must have
been laying on the beach for hours. You notice your your underwear is moist and
clingy... Propping yourself up onto your elbows, your arms sink into the soft 
white sand. You hear small waves wash upon the shore. As you focus your eyes at
the water, you see a trail of sand extending from between your feet and fade
into the clear water below.""")


#############################
######  Execute Game ########
#############################

playing = True

# Function to run the game
def run_game():
    print(HEADING)
    global playing

    while playing:
        reply = input('\n>').lower().split(';') or ['']
        first = True
        for i in reply:
            if not first:
                print('\n>')
            execprint(i)
            first = False
    if __name__ == '__main__':
        input('\n>')


if __name__ == '__main__':
    run_game()