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
    def __init__(self, shortDesc, longDesc, firstDesc):
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.firstDesc = firstDesc


class PermItem:
    """"Items that are permanent and can't be taken."""
    def __init__(self, shortDesc, longDesc, firstDesc):
        self.shortDesc = shortDesc
        self.longDesc = longDesc
        self.firstDesc = firstDesc

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
compose yourself.  Fuck..."""  # First
)

sand = PermItem(
'sand',  # short description
"Small grains of sand. It's everywhere and not very useful right now.",  # Long

"""Sand. Billions and billions of tiny granular material that humanity has used
to construct glass, computer chips, and double D breasts.  It's great, but you
don't need to concern yourself with double D's right now."""  # First
)

water = PermItem(
'sea water',  # Short
"It's sea water.",  # Long

"""You look at the dark sea water and step into the shallow water. The wet
sand seeps between your toes. It's rather soothing here."""  # First
)

# List of all the items to be put into the location object
beachPermItems = [bonfire, sand, water]
beachTkItems = []

# Location(short description, long description, first description, takable
# items, and permanent items)
beachLoc = Location("Shoreline",
"""You are on the beach facing the shoreline. Along the beach, there is a bright
bonfire to your left. You can see a small bungalow to the Southwest and a rock
wall to the Southeast.""",

"""You are on the beach facing the shoreline. Along the beach, there is a bright
bonfire to your left. You can see a small bungalow to the Southwest and a rock
wall to the Southeast.""",

beachTkItems, beachPermItems
)


# Outside bungalow

outBungalowPermItems = []
outBungalowTkItems = []

outBungalow = Location(
"In front of a bungalow.",

"""You are standing in front of an old dilapidated bungalow.""",

"""The thatch roof has caved in a bit, but it is still standing. The door is
open and barely hanging off of one hinge."""

)
##################################
### Item and Location Synonyms ###
##################################


# A dictionary of all objects in the game.  This will help with synonyms
obj_synonyms = {
    # objects that can be taken
    # 'stick': 0, 'sticks': 0, 'branch': 0, 'wood': 0, 'drift-wood': 0,
    # 'mosquito': 1, 'net': 1,
    # 'wrapped-stick': 2,
    # 'torch': 3,
    # 'lit-torch': 4,

    # permanent objects
    'bonfire': -1, 'fire': -1, 'flame': -1,
    # 'bed': -2, 'mattress': -2,
    # 'pillow': -3, 'cushion': -3,
    # 'rocks': -4, 'boulders': -4,
    'sand': -5,
    # 'counter': -6, 'table': -6,
    # 'stove': -7,
    # 'lard': -8, 'bucket': -8, 'container': -8, 'fat': -8, 'oil': -8, 'tub': -8,
    'water': -9, 'ocean': -9, 'sea': -9, 'salt': -9
}

obj_keys = {
    # objects that can be taken
    # 0: 'stick',
    # 1: 'net',
    # 2: 'wrapped-stick',
    # 3: 'torch',
    # 4: 'lit-torch',

    # perminant objects
    -1: bonfire,
    # -2: 'bed',
    # -3: 'pillow': -3,
    # -4: 'rocks': -4,
    -5: sand,
    # -6: 'counter'
    # -7: 'stove': -7,
    # -8: 'lard'
    -9: water
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
    [ 0, -1, -1,   3,  0,  0, -1, -1, -1, -1,  2, -1],  # 1, outBungalowLoc
    [-1, -1, -1,  -1, -1, -1, -1, -1, -1, -1, -1,  1],  # 2, inBungalowLoc
    [ 0, -1, -1,   1,  0,  0, -1, -1, -1, -1, -1, -1],  # 3, rockWallLoc
    [-1, -1, -1,  -1, -1, -1, -1, -1, -1, -1, -1,  3],  # 4, darkCaveLoc
]

# A This will help tie in the
# dungeon map values with the location objects during movement
dungeon_locs = [beachLoc,
                # outBungalowLoc,
                # inBungalowLoc,
                # rockWallLoc,
                # darkCaveLoc
]

# A list that stores all the areas that have been visited
visited = []

def describe_loc(loc):
    global visited
    if loc not in visited:
        print(loc.firstDesc + '\n')
        print("From here you can see ", end='')
        listLen = len(loc.permItems)
        for i in range(listLen-1):
            print(loc.permItems[i].shortDesc + ', ', end='')
        print('and '+loc.permItems[listLen-1].shortDesc+'.')
        visited.append(loc)
    else:
        print(loc.longDesc)

# List of inventory objects and if we seen it
inventory_list = []
seen_item = []

def describe_item(item):
    global seen_item
    if item not in seen_item:
        print(item.firstDesc + '\n')
        seen_item.append(item)
    else:
        print(item.longDesc)


# Function to add a takable item object to the inventory and remove it from
# location when a player decides to take an item.
def add_inven(item):
    curr = dungeon_locs(current_loc)
    if item not in inventory_list:
        inventory_list.append(item)
        if item in curr.tkItems:
            curr.tkItems.remove(item)

# Function to remove an item from the inventory and place it in the location
# when a player drops the item object
def remove_inven(item):
    curr = dungeon_locs(current_loc)
    if item not in curr.tkItems:
        curr.tkItems.append(item)
        if item in inventory_list:
            inventory_list.remove(item)

# Function to look up inventory
def inven(arg):
    print("You are holding on to: ")
    for i in len(inventory_list)-1:
        print(i.longDesc)

# Function to examine items and location
def examine(args):  # examine = look
    curr = dungeon_locs[current_loc]
    if not args:
        describe_loc(curr)  # first or long description
    else:
        if args[0] not in obj_synonyms:
            print("I don't know what that is.")
        else:
            # Check the player input with object synonym list to get its key
            # number
            objnum = obj_synonyms[args[0]]
            # Now take the key, and look up our official name for the item
            item = obj_keys[objnum]
            describe_item(item)
            # if item not in inventory_list and item not in curr.tkItems:
            #     print("I don't see that here.")
            # else:
            #     print(item.longDesc)

def move(direct):
    global current_section
    newsect = dungeon_map[current_section][direct]
    if newsect == -1:
        print("You can't go that way.")
        # elif newsect == SPECIALNUMBER:
        #special_move(direct)
    else:
        current_section = newsect
        describe_loc(newsect)


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
    # 'take': take, 'get': take, 'pick': take, 'hold': take,
    # 'drop': drop, 'throw': drop, 'toss': drop,
     'look': examine, 'l': examine, 'examine': examine, 'x': examine,
    # 'read': examine, 'r': examine, 'describe': examine,
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


HEADING =
"""You open your eyes and see a full moon above. It's dark out and you've been
laying on the beach for hours. Propping yourself up, your hands sink into the
soft warm sand."""




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
        reply = input('>').lower().split(';') or ['']
        first = True
        for i in reply:
            if not first:
                print('>')
            execprint(i)
            first = False
    if __name__ == '__main__':
        input('\n<')


if __name__ == '__main__':
    run_game()

