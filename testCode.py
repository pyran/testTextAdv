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
'Bonfire.',  # Short

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
'Sand.',  # short description
"Small grains of sand. It's everywhere and not very useful right now.",  # Long

"""Sand. Billions and billions of tiny granular material that humanity has used
to construct glass, computer chips, and double D breasts.  It's great, but you
don't need to concern yourself with double D's right now."""  # First
)

water = PermItem(
'Sea water.',  # Short
"It's sea water.",  # Long

"""You look at the dark sea water and step into the shallow water. The wet
sand seeps between your toes. It's rather soothing here."""  # First
)

beachPermItems = [bonfire, sand, water]

beach = Location("Shoreline",
"""You are on the beach facing the shoreline. Along the beach, there is a bright
bonfire to your left. You can see a small bungalow to the Southwest and a rock
wall to the Southeast.""",

"""You open your eyes and see a full moon above. It's dark out and you've been
laying on the beach for hours. Propping yourself up, your hands sink into the
soft warm sand..""",

None,

beachPermItems
)

print(beach.firstDesc + '\n')
print(beach.permItems[0].firstDesc + '\n')

for num, obj in enumerate(beachPermItems):
    print(num,obj.shortDesc)