#! /usr/bin/python3

# Small text adventure game

HEADING = """You're on a beach."""

current_section = 0

# A list of tuples containing the (Area description, short description)
sections = [
    (
        """You are on the beach facing the shoreline. Along the beach, there is a bright
bonfire to your left. You can see a small bungalow to the Southwest and a rock
wall to the Southeast.""", "Shoreline"),  # index 0
    (
        """In front of you is a small wooden bungalow. It might have been for tourists
at one point, but it looks like it has seen better days. To the North
is the shoreline and to the East is a rock wall.""",
        "Outside Bungalow"),  # index 1
    (
        """You are inside the bungalow. There is an old bed under a mosquito net to
your right and a small table on your left.""",
        "Inside Bungalow"),  # index 2
    (
        """A huge rock wall stands before you. It's much too steep to climb, but you see
an opening among the cracks large enough that you could fit through. You also,
spot a few sticks and rocks at the base of the wall.

You can see the shoreline to the North and a bungalow to the East.""",
        "Rock wall"),  # index 3
    (
        """You squeezed yourself through the small crack. That was oddly pleasurable.
It's pitch black inside and you can't see anything but the entrance""",
        "Dark cave")  # index 4

]


# A dictionary that converts the short name of a section to its index
sec = {}
for indexed in enumerate(sections):
    index = indexed[0]
    long_name = indexed[1][1]  # indexed[1][0] is the description
    short_name = ''
    for C in long_name:
        if C in ' /':  # convert spaces and slashes into dashes
            short_name += '-'
        elif C not in ".'":  # don't use periods and apostrophes
            short_name += C.lower()  # convert letters to lowercase
    sec[short_name] = index

# print(sec)

# A dictionary of all possible directional movements and their indexes
dirs = {'north': 0, 'n': 0, 'south': 1, 's': 1,
        'west': 2, 'w': 2, 'east': 3, 'e': 3,
        'northeast': 4, 'ne': 4, 'southeast': 5, 'se': 5,
        'northwest': 6, 'nw': 6, 'southwest': 7, 'sw': 7,
        'up': 8, 'u': 8, 'down': 9, 'd': 9,
        'in': 10, 'enter': 10, 'on': 10, 'out': 11, 'exit': 11, 'off': 11}

# A matrix of all the possible paths on the map
dungeon_map = [
    # n,  s,  e,  w,  ne, nw, se, sw, up, dn, in, out
    [-1, -1, -1, -1, -1, -1, 3, 1, -1, -1, -1, -1],  # 0, shoreline
    [0, -1, -1, 3, 0, 0, -1, -1, -1, -1, 2, -1],  # 1, outside-bungalow
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1],  # 2, inside-bungalow
    [0, -1, -1, 1, 0, 0, -1, -1, -1, -1, -1, -1],  # 3, rock-wall
    [-1, 99, -1, -1, -1, -1, -1, -1, -1, -1, 99, 3],  # 4, dark-cave
]

# A dictionary of objects and descriptions
obj = {
    # objects that can be taken
    'stick': 0, 'sticks': 0, 'branch': 0, 'wood': 0, 'drift-wood': 0,
    'mosquito': 1, 'net': 1,
    'wrapped-stick': 2,
    'torch': 3,
    'lit-torch': 4,

    'bonfire': -1, 'fire': -1, 'flame': -1,
    'bed': -2, 'mattress': -2,
    'pillow': -3, 'cushion': -3,
    'rocks': -4, 'boulders': -4,
    'sand': -5,
    'counter': -6, 'table': -6,
    'stove': -7,
    'lard': -8, 'bucket': -8, 'container': -8, 'fat': -8, 'oil': -8, 'tub': -8,
    'water': -9, 'ocean': -9, 'sea': -9, 'salt': -9,
}
# A tuple of objects that can be taken. (Search indication, short description)
tk_objs = [
    ("There is a wet stick here.", "A wet stick."),  # 0
    ("There is a mosquito net hanging over the bed.",
     "A piece of mosquito net"),  # 1
    ("There is the makeshift torch you constructed.",
     "A makeshift torch."),  # 3
    ("There is a flaming lit-torch", "A lit-torch")
]

tk_obj_desc = [
    "It's a wet wooden stick.  Its the only interactive phallic item in the "
    "game!",
    "It's good sized swath of the mosquito net you found in the bungalow.",
    "It's the wet stick you wrapped with the net. Kinda looks like a giant...",
    "It's a complete makeshift torch. This should stay lit for a while."
    "This is a torch and the tip is on FIRE! The symbolism reminds you of your "
    "college days.  Thank god for antibiotics."
]

perm_objs = [
    None,
    ("There is a bright bonfire by the shore.", "A bonfire."),  # -1
    ("There is a bed in the right corner.", "A bed."),  # -2
    ("There is a  pillow by the foot of the bed", "A pillow."),  # -3
    ("There are a few rocks scattered about", "Some rocks."),  # -4
    ("There is sand every where.", "Sand"),  # -5
    ("There is a kitchen counter to the left", "Kitchen counter."),  # -6
    ("There is a stove on the counter", "A stove."),  # -7
    ("There is a bucket of lard on the counter", "Bucket of lard."),  # -8
    ("There is sea water by the shoreline", "Sea water")  # -9
]
perm_obj_desc = [
    None,
    """As you approach, the flames from the bonfire gently flicker in the wind.
    Upon closer inspection, you notice it's fueled by melted plastic containers
    and old car tires.  It's no wonder huge plumes of black smoke billow into
    the moon-lit sky. It's eerily beautiful.

    Suddenly, the wind shifts and you
    get a lung full of the toxic fumes. Practically choking to death, you drop
    to the ground curl up into the fetal position and cough for a solid 5
    minutes. You Wipe the tears from your face, stand back up, and take a few
    minutes to compose yourself.""",

    """The bed has seen some better days. As you inspect the mattress, you
    notice it has taken on a yellow and brown hue.  There are a few few crusty
    looking spots.  It must have been a popular teenage hangout. You spot a
    pillow near the foot of the bed.""",

    """The pillow lies naked on the foot of the bed. It looks damp and covered
    with black mold.  Your nose begins to run just getting close to it.

    You begin to ponder what terrible atrocities the pillow's cover must have
    been subjected to. Did someone used it as a substitute for toilet paper?
    Maybe it became an improvised gag? Or a make-shift contraceptive?
    Where is it now?! You had to know! Well... sort of.""",

    """These are special rocks.  They look just like the ones back at home:
    smooth, round and would fit nicely in a sack.  Although, it's no time to
    be playing these rocks right now.  You can play with them when you get
    home.""",

    """Sand. Billions and billions of tiny granular material that
    humanity has used to construct glass, computer chips, and double D
    breasts.  It's great, but you don't need to concern yourself with double D's
    right now.""",

    """A kitchen counter. There is a stove embedded in the middle and a
    small bucket standing on its right.""",

    """The stove is slick with grease and studded with charred bits of meat.""",

    """The bucket is filled to the brim with lard. It has slowly bubbling over
    from the heat.  It looks to be a popular destination for insects looking to
    drown."""

    """You look at the dark sea water and step into the shallow water. The wet
    sand seeps between your toes. It's rather soothing here.""",
]

############################
# below needs work
############################

inventory = []
items = []
visited = []


def describe(section):
    "Give a long description if we have a negative room number."
    # This will cause room 0 to always have a long explanation.
    global visited
    print(sections[abs(section)][1])
    if section <= 0 or section not in visited:
        print(sections[abs(section)][0])
    if section not in visited:
        visited.append(section)
    #for i in items[abs(section)]:
     #   if i >= 0:
      #      print(tk_objs[i][0])
       # else:
        #    if isinstance(perm_objs[abs(i)], str):
         #       print(perm_obs[abs(i)])


def inven(args):
    print("You currently have: ")
    for i in inventory:
        print(tk_objs[i][1])


def take(args):
    if not args:
        print("You must specify an object.")
    else:
        if args[0] == "all":
            first_objs = list(items[current_section])
            gotsome = False
            for i in first_objs:
                if i >= 0:
                    gotsome = True
                    print("%s:" % tk_objs[i][1])
                    takeobj(i)
            if not gotsome:
                print("Nothing to take.")
        else:
            if not args[0] in obj:
                print("I don't know what that is.")
            else:
                takeobj(obj[args[0]])


def takeobj(x):
    global inventory, items
    if not x in items[current_section]:
        print("I do not see that here.")
    else:
        if x < 0:
            print("You cannot take that.")
        else:
            print("Taken.")
            items[current_section].remove(x)
            inventory.append(x)


def drop(args):
    global inventory, items
    if not args:
        print("You must specify an object.")
    else:
        if not args[0] in obj:
            print("I don't know what that is.")
        else:
            objnum = obj[args[0]]
            if not objnum in inventory:
                print("You don't have that.")
            else:
                print("Done.")
                inventory.remove(objnum)
                items[current_section].append(objnum)

# This command doesnt seem right...
def examine(args): # examine = look
    if not args:
        describe(-current_section) # long description
    else:
        if not args[0] in obj:
            print("I don't know what that is.")
        else:
            objnum = obj[args[0]]
            if not objnum in inventory and not objnum in items[current_section]:
                print("I don't see that here.")
            else:
                if objnum >= 0:
                    desc = tk_obj_desc[objnum]
                else:
                    desc = perm_obj_desc[abs(objnum)]
                if isinstance(desc, str):
                    print(desc)
                else:
                    print("I see nothing special about that.")


def move(direct):
    global current_section
    newsect = dungeon_map[current_section][direct]
    if newsect == -1:
        print("You can't go that way.")
        # elif newsect == SPECIALNUMBER:
        #special_move(direct)
    else:
        current_section = newsect
        describe(newsect)


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
    # 'in' is a delimeter, and cannot be used as a funcname without entailing invalid syntax
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
    'drop': drop, 'throw': drop, 'toss': drop,
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
# and so on with the rest of the functions

# This function deals with user input


def execprint(x):
    line = x.split()
    for c in ',:':
        line = c.join(line).split(
            c)  # Also, get rid of `c` that's been there first
    if line:
        if not line[0] in verblist:
            print("I don't understand that.")
        else:
            func = verblist[line[0]]
            args = line[1:]
            func(args)


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