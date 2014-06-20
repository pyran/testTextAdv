# Nicholas' tutorial doesn't use classes and objects.  It might make the game
# more difficult to scale. I'm going to see if I can improve upon his design a
# bit.  This is some experimental code that I am playing with.

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

"""WHAT? Are you crazy? I'll leave the bonfire where it is."""
)

sand = PermItem(
'sand',  # short description
"Small grains of sand. It's everywhere.",  # Long

"""Sand. Billions and billions of tiny granular material that humanity has used
to construct glass, computer chips, and double D breasts.  It's great, but you
don't need to concern yourself with double D's right now.""",  # First

"""Sand is great, but you don't need any."""
)

water = PermItem(
'sea water',  # Short
"It's sea water.",  # Long

"""You look at the dark sea water and step into the shallow water. The wet
sand seeps between your toes. It's rather soothing here.""",  # First

"""There is plenty of it. You can comeback here and enjoy it any time"""

)

# List of all the items to be put into the location object
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

beachTkItems, beachPermItems
)


# Outside bungalow

outBungalowPermItems = []
outBungalowTkItems = []

outBungalowLoc = Location(
"In front of a bungalow.",

"""You are standing in front of an old dilapidated bungalow. The thatch roof has
caved in a bit, but it is still standing. The door is open and barely hanging
off of one hinge. Looks safe enough to enter. You see the beach to the North
and a rock wall to the East.""",

"""You are standing in front of an old dilapidated bungalow. The thatch roof has
caved in a bit, but it is still standing. The door is open and barely hanging
off of one hinge. Looks safe enough to enter.""",

outBungalowTkItems, outBungalowPermItems
)

# Inside the Bungalow

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
soaked in."""
)

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

"""...the crust..."""
)

counter = PermItem(
"a counter",

"""A greasy kitchen counter. There is a stove embedded in the middle and a
small bucket standing on its right.""",

"""It's a kitchen counter.  You notice it is slick to the touch. It also
has some signs of water damage. There is a stove embedded in the middle and a
small bucket standing on its right.""",

"""You'd probably need a small crane to lift this."""
)

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

"""It's a part of the counter. It's also pretty useless."""
)

net = TkItem(
"a mosquito net",

"""An old mosquito net.  DAMN they be lots of holes.""",

"""You see an old mosquito net hanging over the bed.  It's got a lot of holes
in it.""",

"""You rip some of the mosquito net down and shove it down your pants. For
safe-keeping."""
)

inBungalowPermItems = [pillow, bed, counter, lard, stove]
inBungalowTkItems = [net]

inBungalowLoc = Location(
"inside the bungalow.",

"""You are inside the bungalow. There is an old bed under a mosquito net to
your right and a small table on your left. You can see the exit behind you.""",

"""You are inside the bungalow. There is an old bed under a mosquito net to
your right and a small table on your left.""",

inBungalowTkItems, inBungalowPermItems
)

# Rock wall

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

"""Sweet cave bro.""",

"""You can't take a cave entrance, what the fuck?"""
)

stick = TkItem(
"a stick",

"""It's a fresh wooden stick.  Its the only interactive phallic item in the
game!""",

"""A huge gnarled stick. Looks like the optimal girth for your hands.""",

"""You reach down and pick up this gnarled stick.  Still impressed with the
girth of this enormous stick, you strap it to your side by the band of your
tightie whities."""
)

cliffSideTkItems = [stick]
cliffSidePermItems = [rocks, opening]

cliffSideLoc = Location(
"A cliff side",

"""A huge cliff side stands before you. It's much too steep to climb, but you
see an opening among the cracks large enough that you could fit through.
You can see the shoreline to the North and a bungalow to the East.""",

"""A huge cliff side stands before you. It's much too steep to climb. It's
likely an artificial wall the developer put up to stop you from going farther
south.

Although, you do see an opening among the cracks large enough that you
could fit through.""",

cliffSideTkItems, cliffSidePermItems

)

darkCaveLoc = Location(
"A cave",

"""You are in a cave. CONGRATULATIONS. You beat the game. Pat yourself on the"
back.  Seriously, thanks for playing my first game. It was crappy, now I should
go make a better one.""",

"""You are in a cave. CONGRATULATIONS. You beat the game. Pat yourself on the"
back.  Seriously, thanks for playing my first game. It was crappy, now I should
go make a better one.""",

None, None
)

wrappedStick = TkItem(
"a wrapped stick",

"""It's the gnarled stick you wrapped with the mosquito net. Kinda looks like a
giant...""",

"""It's the gnarled stick you wrapped with the mosquito net on one tip. Kinda
looks like a giant...""",

"""You already have it strapped to your loins."""
)

torch = TkItem(
"a torch",

"""It's a makeshift torch composed of a stick, mosquito net and lard.""",

"""It's the product of your genius! A homemade torch made of mosquito net, and
a stick.  Then the tip was double-dipped in lard. This should stay lit for a
while.""",

"""You already have it. The lard from your homemade torch is soaking through
your boxers."""
)

litTorch = TkItem(
"a lit torch",

"""Your torch is fucking on fire.""",

"""Your torch is fucking on fire. Just like your penis when you pee.""",

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
    'wrapped-stick': 2, 'wrapped':2,
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
    'opening': -10, 'cave': -10, 'crack': -10, 'entrance':-10
}

obj_keys = {
    # objects that can be taken
    0: stick,
    1: net,
    # 2: wrappedStick,
    # 3: torch,
    # 4: lit-torch,

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

# A matrix of all the possible paths on the map
dungeon_map = [
    # n,  s,  e,  w,  ne, nw, se, sw, up, dn, in, out
    [-1, -1, -1,  -1, -1, -1,  3,  1, -1, -1, -1, -1],  # 0, beachLoc
    [ 0, -1,  3,  -1,  0,  0, -1, -1, -1, -1,  2, -1],  # 1, outBungalowLoc
    [-1, -1, -1,  -1, -1, -1, -1, -1, -1, -1, -1,  1],  # 2, inBungalowLoc
    [ 0, -1, -1,   1,  0,  0, -1, -1, -1, -1, -2, -1],  # 3, cliffside
    [-1, -1, -1,  -1, -1, -1, -1, -1, -1, -1, -1,  3],  # 4, darkCaveLoc
]

# A This will help tie in the
# dungeon map values with the location objects during movement
dungeon_locs = [beachLoc, outBungalowLoc, inBungalowLoc, cliffSideLoc,
                darkCaveLoc]

# A list that stores all the areas that have been visited
visited = []

def describe_loc(locNum):
    global visited
    loc = dungeon_locs[locNum]
    if loc not in visited:
        print(loc.firstDesc, end='')
        visited.append(loc)
        tkLen = len(loc.tkItems)
        if tkLen > 0:
            print(" You also see ", end='')
            if tkLen > 1:
                for i in range(tkLen-1):
                    print(loc.tkItems[i].shortDesc + ', ', end='')
            else:
                print(loc.tkItems[0].shortDesc + '.')
    else:
        print(loc.longDesc)

# List of inventory objects and if we seen it
inventory_list = [net, stick]
seen_item = []

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
    else:
        # Check the player input with object synonym list to get its key
        # number
        objnum = obj_synonyms[args[0]]
        # Now take the key, and look up the item object
        itemObj = obj_keys[objnum]
        curr = dungeon_locs[current_loc]
        # Check and see if the item object is in the inventory or location
        if args[0] not in obj_synonyms:
            print("I don't know what that is.")
        elif itemObj not in inventory_list and itemObj not in curr.tkItems and itemObj not in curr.permItems:
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
#def combine(arg1, arg2)


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

def move(direct):
    global current_loc
    newsect = dungeon_map[current_loc][direct]
    if newsect == -1:
        print("You can't go that way.")
    elif newsect == -2:
        if lit-torch not in inventory_list:
            print("It's too fucking dark. You shouldn't go in there.")
        else:
            newsect = dungeon_map[current_loc][4]
    else:
        current_loc = newsect
        describe_loc(current_loc)


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

verblist = {
    'take': take, 'get': take, 'pick': take, 'hold': take,
    # 'drop': drop, 'throw': drop, 'toss': drop,
    'look': examine, 'l': examine, 'examine': examine, 'x': examine,
    'read': examine, 'r': examine, 'describe': examine,
    # can't use 'd' because of going down
     'inventory': inven, 'i': inven, 'items': inven, #'die': die, 'quit': _quit,
    #'help': _help, 'save': save, 'restore': restore, 'go': go,
    'north': north, 'n': north, 'south': south, 's': south,
    'east': east, 'e': east, 'west': west, 'w': west,
    'northeast': northeast, 'ne': northeast, 'southeast': southeast,
    'se': southeast,
    'northwest': northwest, 'nw': northwest, 'southwest': southwest,
    'sw': southwest,
    'up': up, 'u': up, 'down': down, 'd': down, 'in': _in, 'out': out,
    'on': _in, 'off': out, 'enter': _in, 'exit': out,
}


HEADING =(
"""You open your eyes and see a full moon above. It's dark out and you've been
laying on the beach for hours. Propping yourself up, your hands sink into the
soft warm sand.""")




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
            func(args)

#############################
######  Execute Game ########

# Function to run the game
def run_game():
    print(HEADING)
    while True:
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

