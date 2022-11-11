from items import *
from enemies import *
from npcs import *

room_template = {
    "name": "Template",

    "description": [
        "blahblahbalh"
    ],

    "exits": {'a': 1,
              'b': 2,
              'c': 3

              },

    "items": ["item1"],

    "npcs": ["npc1"],

    "enemies": ["enemy1"],

    "visited": False,

    "story": "story lines",

    "fight_end": "fight_end ending story"
}

room_cabin = {
    "name": "Cabin",

    "description": [
        "A Safe place to rest. To the South there is a path into the woods."
    ],

    "exits": {
        "south": "Woodland Clearing"
    },

    "items": [],

    "npcs": [daughter],

    "enemies": [],

    "visited": True,

    "story": [
        "You are Skarde, father to one, widower to Sigrid.\n",
        "You live in a small cabin deep within the forest, covered by layers of",
        "trees and other such vegetation. You've lived here since you were a boy",
        "and as such have learned to survive this life of solitude. It has been",
        "a struggle for you, though you've made your way through life with both your",
        "trusty ax, and lethal saxe in hand, and enough grit to get by.\n",
        "Over the recent months, you've found yourself caring for your gravely",
        "ill daughter, Frida. Many men of healing, priests, druids, and even",
        "doctors have been to tried to cure her sickness, though none have",
        "succeeded.\n",
        "One dark night, your daughter's illness begins to worsen once more. You",
        "feel that there is nothing to do, but take matters into your own hands.",
        "You know the forest surrounding the cabin is riddled with dangers at",
        "night, however you must make the journey south to the nearest town."
    ],

    "fight_end": ""
}

room_clearing = {
    "name": "Woodland Clearing",

    "description": [
        "A small clearing in the woodland tundra. To the north is your cabin, and",
        "to the south you can see the distant lights of the town. To the east, a",
        "small trail leads to the graveyard of your ancestors, and to the west,",
        "the trail continues to an old shrine"
    ],

    "exits": {
        "north": "Cabin",
        "south": "Town Trail",
        "west": "Shrine Trail",
        "east": "Graveyard Trail"
    },

    "items": [],

    "npcs": [],

    "enemies": [enemy_wolf],

    "visited": False,

    "story": [
        "You begin to walk from your cabin home, trudging through ground laced",
        "with a delicate layer of snow. You've always lived in this tundra, so",
        "wading through mud disguised by snow is no problem for you. Night is",
        "falling however, and you know that you should never be travelling",
        "through the forest alone and at night.\n",
        "After a few more miles, you reach a clearing in the trees. You become",
        "aware of snapping twigs and crunching leaves around you getting louder",
        "and louder. You can tell something is hunting you. A howl from the trees",
        "that line the path sets your pulse racing as a wolf lopes into the",
        "clearing. You can see the distant lights of the town to the south behind",
        "the wolf"
    ],

    "fight_end": [
        "Covered in the wolf's blood, and weary from effort, you can finally look",
        "around the clearing. To the south, you can see the lights of the town,",
        "to the east is a small trail to your ancestor's graveyard, to the west,",
        "the trail continues to a small shrine you used to pray at."
    ]
}

room_shrine = {
    "name": "Shrine",

    "description": [
        "You approach a shrine to some unknown deity. The exit is to the East."
    ],

    "exits": {
        "east": "Shrine Trail"
    },

    "items": [],

    "npcs": [spirit ],

    "enemies": [enemy_spirit],

    "visited": False,

    "story": [
        "You arrive at the broken and worn down shrine, where nature has regained",
        "control of what was once a man-made display of devotion to a now",
        "forgotten god. The trail leads back east to the Clearing in the woods.",
    ],

    "fight_end": [
        "Drakes: You have done well, Skarde. Now you will choose whether you want to obtain the power of another life."
    ]
}

room_shrine_trail = {
    "name": "Shrine Trail",

    "description": [
        "This Trail leads to the shrine in the distance. The trail continues West",
        "to the shrine, and East to the clearing in the woods."
    ],

    "exits": {
        "west": "Shrine",
        "east": "Woodland Clearing"
    },

    "items": [],

    "npcs": [],

    "enemies": [],

    "visited": False,

    "story": "",

    "fight_end": ""
}

room_town_trail = {
    "name": "Town Trail",

    "description": [
        "Trail that leaves the woodland. You can see the lights of the town off",
        "in the distance to the south. The path continues north to the clearing."
    ],

    "exits": {
        "north": "Woodland Clearing",
        "south": "Northern Gates"
    },

    "items": [],

    "npcs": [],

    "enemies": [],

    "visited": False,

    "story": "",

    "fight_end": ""
}

room_town_north_gates = {
    "name": "Northern Gates",

    "description": [
        "You arrive at the Northern gates to the town"
    ],

    "exits": {
        "north": "Town Trail",
        "south": "Town Centre",
    },

    "items": [],

    "npcs": [],

    "enemies": [],

    "visited": False,

    "story": [
        "After a night's worth of a dangerous journey, you finally arrive at the",
        "the town. It's been a while since you've been around a lot of people at",
        "once.",
    ],

    "fight_end": ""
}

room_town_east_gates = {
    "name": "Eastern Gates",

    "description": [
        "You arrive at the town eastern gates"
    ],

    "exits": {
        "west": "Town Centre",
        "east": "Bandit Trail",
    },

    "items": [],

    "npcs": [],

    "enemies": [],

    "visited": False,

    "story": "",

    "fight_end": ""
}

room_town = {
    "name": "Town Centre",

    "description": [
        "You arrive in the centre of the town"
    ],

    "exits": {
        "hall": "Town Hall",
        "tavern": "Town Tavern",
        "church": "Town Church",
        "inn": "Town Inn",
        "north": "Northern Gates",
        "east": "Eastern Gates"
    },

    "items": [],

    "npcs": [],

    "enemies": [],

    "visited": False,

    "story": [
        "The town is small, almost a village, minuscule huts line the roads",
        "through the town, though you can pick out certain buildings just from",
        "how they look alone. You can see a tavern, relatively small so shouldn't",
        "get too busy; an inn, somewhere to rest; a small church, a fairly new",
        "construction that holds connection to the gods; and the largest building,",
        "the town hall, a place where you'd more than likely find the town chief.\n",
        "Morning has broken, and now people are out in the town, washing things,",
        "sharpening tools and weapons. It's oddly quiet for how many people are",
        "here. Maybe some of these townspeople know something about the illness",
        "your daughter has."
    ],

    "fight_end": ""
}

room_town_inn = {
    "name": "Town Inn",

    "description": [
        "You enter the Inn"
    ],

    "exits": {
        "west": "Town Centre"
    },

    "items": [],

    "npcs": [innKeeper],

    "enemies": [],

    "visited": False,

    "story": [
        "You're in the inn, you're sure that there will be at least one bed for",
        "you here. The exit is to the West."
    ],

    "fight_end": ""
}

room_town_tavern = {
    "name": "Town Tavern",

    "description": [
        "You enter the Tavern"
    ],

    "exits": {
        "east": "Town Centre"
    },

    "items": [],

    "npcs": [],

    "enemies": [],

    "visited": False,

    "story": [
        "You enter the tavern, nothing out of the ordinary here. A few drunken",
        "brawls, and drunken lovers, though what else do you expect? Gossip is",
        "rich around these places, and so is conversation. [try listening or",
        "talking to people]. Drink also flows, if that's what you really crave.",
        "The exit is to the East.",
    ],

    "fight_end": ""
}

room_town_hall = {
    "name": "Town Hall",

    "description": [
        "You arrive inside the beautiful ornate town hall"
    ],

    "exits": {
        "north": "Town Centre"
    },

    "items": [],

    "npcs": [chief],

    "enemies": [],

    "visited": False,

    "story": [
        "You stand before an elder, the chief of the town. He's not very",
        "intimidating though you can tell he is wise past beyond his years.",
        "The building is large compared to other sin the town, and the walls",
        "are lined with ceremonial swords, daggers and shields. This building is",
        "obviously filled with pride and story. The exit is to the North.",
    ],

    "fight_end": ""
}

room_town_church = {
    "name": "Town Church",

    "description": [
        "You enter an old norse place or prayer"
    ],

    "exits": {
        "south": "Town Centre"
    },

    "items": [],

    "npcs": [],

    "enemies": [],

    "visited": False,

    "story": [
        "You enter through the large doors of the church, taking in the",
        "architecture and glassware the likes of which you've never had the",
        "chance to see before. A woman stands before the altar, robed in black;",
        "It would appear she is the priest. The exit is to the South."
    ],

    "fight_end": ""
}

room_graveyard_trail = {
    "name": "Graveyard Trail",

    "description": [
        "This Trail leads to a desolate graveyard"
    ],

    "exits": {
        "west": "Woodland Clearing",
        "east": "Graveyard"
    },

    "items": [],

    "npcs": [],

    "enemies": [],

    "visited": False,

    "story": "",

    "fight_end": ""
}

room_graveyard = {
    "name": "Graveyard",

    "description": [
        "You enter a barren wasteland littered with stone covered graves"
    ],

    "exits": {
        "west": "Graveyard Trail",
        "south": "Bandit Graveyard trail"

    },

    "items": [],

    "npcs": [],

    "enemies": [enemy_ghost],

    "visited": False,

    "story": [
        "A thick mist covers the ground, and the rattling of metal fences",
        "and the whistling of the wind can only make the hairs on your neck stand",
        "on end. You navigate your way to the graves of your ancestors, looking",
        "down onto it."
    ],

    "fight_end": [
        "Ghost has been defeated!"
    ]
}

room_bandit_graveyard_trail = {
    "name": "Bandit Graveyard Trail",

    "description": [
        "This route connects the bandits hideout to the graveyard"
    ],

    "exits": {
        "north": "Graveyard",
        "south": "Bandit Hideout"
    },

    "items": [],

    "npcs": [],

    "enemies": [enemy_bandit],

    "visited": False,

    "story": [
        "You approach the hideout revealed to you by the town Chief.\n",
        "You can tell from a distance that it's not too large, and looks very",
        "makeshift. Its probably held up by rocks, logs cloth. Standing at the",
        "gate, you realise you're at the point of no return, will you continue to",
        "fight"
    ],

    "fight_end": ""
}

room_bandit_hideout = {
    "name": "Bandit Hideout",

    "description": [
        "You arrive at a bandit camp"
    ],

    "exits": {
        "north": "Bandit Graveyard Trail",
        "west": "Bandit Trail"
    },

    "items": [],

    "npcs": [],

    "enemies": [enemy_bandit_boss],

    "visited": False,

    "story": [
        "After slowly slogging through the mud, you reach the camp.",
        "You've never fought other people before, but now you're about",
        "to find out how good you are at it",
    ],

    "fight_end": ""
}

room_bandit_trail = {
    "name": "Bandit trail",

    "description": [
        "You are on a trail between the eastern gates and the bandit hideout"
    ],

    "exits": {
        "west": "Eastern Gates",
        "east": "Bandit Hideout",
    },

    "items": [],

    "npcs": [],

    "enemies": [enemy_bandit],

    "visited": False,

    "story": "",

    "fight_end": ""
}

room_temple_trail = {
    "name": "Temple Trail",

    "description": [
        "This trail takes you up to the temple from the graveyard"
    ],

    "exits": {
        "north": "Temple",
        "south": "Graveyard",
    },

    "items": [],

    "npcs": [],

    "enemies": [],

    "visited": False,

    "story": "",

    "fight_end": ""
}

room_temple = {
    "name": "Temple",

    "description": [
        "An old abandoned temple from long ago"
    ],

    "exits": {
        "north": "Temple Fight Room"
    },

    "items": [],

    "npcs": [],

    "enemies": [],

    "visited": False,

    "story": [
        """Through a long journey through a vicious snowstorm, you reach the point where the aurora was dancing over.""",
        """As you walk through the blistering cold, the snow trembles, eventually breaking and causing you to fall through down into a pit.""",
        """A few moments pass before you regain your consciousness.""",
        """You wake up in a small chamber of what seems to be a temple.""",
        """ You get up and begin to make your way through the temple to find an exit."""],

    "fight_end": ""
}

room_temple_fight_room = {
    "name": "Temple Fight Room",

    "description": [
        "A chamber further within the winding corridors of this morbid temple"
    ],

    "exits": {
        "north": "Temple Treasure Room",
        'south': "Temple Reward Room"
    },

    "items": [],

    "npcs": [],

    "enemies": [enemy_corpse],

    "visited": False,

    "story": [
        """Winding corridors and tight spaces line the entire temple, and many mummified bodies lay in spaces dug out in the walls, could these be buried heroes of old?""",
        """ Either way, you continue to delve into the ancient temple.""",
        """Suddenly, from behind you, you hear a creaking. In a temple so empty, how could there be so much noise?""",
        """ You turn and find that several of the mummified bodies have turned undead, and draw their weapons towards you."""
    ],

    "fight_end": ""
}

room_temple_treasure_room = {
    "name": "Temple Treasure Room",

    "description": ["A dimly lit chamber within the old temple"

                    ],

    "exits": {
        "north": "Lake",
        "south": "Temple Fight Room"
    },

    "items": [item_gram],

    "npcs": [],

    "enemies": [],

    "visited": False,

    "story": ["""Defeating the walking dead, you approach the final room that was left to enter.""",
              """ Inside, a shattered blade lay on the table.""",
              """ A blade so sharp even when so horridly destroyed that it could cut the very walls of the temple you stand in.""",
              """ This was the legendary blade, Gram."""],

    "fight_end": ""
}

room_lake = {
    "name": "Lake",

    "description": ["An ominous and imposing lake. The air feels other worldly"

    ],

    "exits": {
        "south": "Temple Treasure Room"
    },

    "items": [],

    "npcs": [jormungandr],

    "enemies": [enemy_jormungandr],

    "visited": False,

    "story": ["""A large expansive lake sits dormantly between the bases of some mountains in the distance.""",
              """A thick fog coats the surface of the water, making the contents of the depths go unseen.""",
              """ Though, you know what you are here to do, and so does the monster within the lake.""",
              """You spot a rowboat along the sides of the lake, and take it.""",
              """You row yourself out into the middle of the lake and call out to the serpent, beckoning it to a challenge.""",
              """Only the sounds of rumbling can be heard, quietly until it gets louder, and louder, and louder.""",
              """The serpent rears its head from inside the lake, hissing at you. It's Time to fight!"""],

    "fight_end": [
        "Wounded, the World Serpent screeches at you and flees back into its watery domain.",
        "Though you could not slay the beast, you had gotten what you came for. Battered and",
        "tired, you fall onto your knees in the tiny rowboat, victory is yours. Hopefully now",
        "your daughter can be cured.  You travel home, rowing back onto the shore.   It was a",
        "long and arduous journey, but you have seen it through. At home, your sick child",
        "lays in bed, now comatose. You take the scale of the serpent and crush it into a",
        "powder with the hilt of Gram, almost breaking the bowl you put it in. You give the",
        "medicine to your daughter and slowly, she begins to wake. You've cured your daughter,",
        "no matter how you chose to do so, you have succeeded in your task, congratulations."
    ]
}

rooms = {
    "Template": room_template,
    "Cabin": room_cabin,
    "Woodland Clearing": room_clearing,
    "Town Trail": room_town_trail,
    "Northern Gates": room_town_north_gates,
    "Eastern Gates": room_town_east_gates,
    "Town Centre": room_town,
    "Town Church": room_town_church,
    "Town Inn": room_town_inn,
    "Town Hall": room_town_hall,
    "Town Tavern": room_town_tavern,
    "Shrine Trail": room_shrine_trail,
    "Shrine": room_shrine,
    "Graveyard Trail": room_graveyard_trail,
    "Graveyard": room_graveyard,
    "Bandit Hideout": room_bandit_hideout,
    "Bandit Trail": room_bandit_trail,
    "Temple Trail": room_temple_trail,
    "Temple": room_temple,
    "Temple Treasure Room": room_temple_treasure_room,
    "Temple Fight Room": room_temple_fight_room,
    "Lake": room_lake

}
