from dialogue import *

chief = {
    "name": "Town Chief",
    "description": [
        "The Town Chief, an elderly man with a stoic face. His complexion is",
        "quite sagged and worn, much like his clothing: old robes designed with",
        "runic patterns and inspirations taken from animals. The Chief stands",
        "hunched, without a very large presence physically, however you can feel",
        " that he holds knowledge some cannot fathom."
    ],
    "intro": [
        "Greetings, greying one, what brings you to me today?"
    ],
    "dialogue":chiefDialogue
}

spirit = {
    "name": "spirit",
    "description": [
        "A statue stands in the center of the shrine, coated in algae and moss.",
        "You feel comforted just being around the statue, since you used to pray",
        "here with your family. "
    ],
    "intro": [
        "And so you return, after all these years. Is it advice you have come",
        "for? Perhaps a favour?"
    ],
    "dialogue":spiritDialogue
}

ancestorGhost = {
    "name": "Drakes",
    "description": [
        "A shaded figure, ragged and floating just above the ground coated by",
        "mist. It is wielding a sword, though it looks too physically weak to",
        "even wield it. It is wearing a black, torn cloak, and a helmet. It's",
        "eyes are red, and glow in the darkness of the resting place of your ",
        "family."
    ],
    "intro": [
        "Skarde... The place where your family rests is a fitting place to test",
        " your mettle. I am Drakes, the spirit of your ancestors. Prepare yourself..."
    ],
    "dialogue":ancestorGhostDialogue
}

jormungandr = {
    "name": "Jörmungandr",
    "description": [
        "The one you came to beat. The one thing standing in your way now. The",
        "beast is massive in size, towering over you and almost the mountains",
        "behind it. Only part of it breaks the surface of the lake. The serpent",
        "is white, and each of its scales shine with the brightness of the moon.",
        " It's face is scarred from battles with gods. You can only be scared in",
        " its presence."
    ],
    "intro": [
        "You, you think you can even so much as lay a scratch on me? Pathetic,"
        "you've come all this way just to die here, alone."
    ],
    "dialogue":jormungandrDialogue
}

daughter = {
    "name": "Frida",
    "description": [
        "Your daughter, fair haired with blue eyes. She is resting in her bed.",
        "Over the past few months she has become terminally sick with an illness",
        "that no one has been able to cure as of yet. It is up to you to do",
        "something."
    ],
    "intro": [
        "Father, will I get better?"
    ],
    "dialogue": daughterDialogue
}

innKeeper = {
    "name": "Inn Keeper",
    "description": [
        "The Innkeeper is a tall standing man, with brown hair and a full beard.",
        "You can tell he is of a nice disposition, and is generally kind,",
        "probably at a detriment to his business. He is wearing a white tunic and",
        " a brown leather apron. "
    ],
    "intro": [
        "Welcome, would you like a room?"
    ],
    "dialogue":innKeeperDialogue
}

priest = {
    "name": "Priest",
    "description": [
        "The priest is a fair haired lady, who stands shorter than you. She is",
        "wearing a black robe, and in general, her facial complexion is warming",
        "and kind. She stands by the altar, worshipping the gods of old. You feel",
        " as if you could talk to her at any time."
    ],
    "intro": [
        "Welcome to my sanctuary here. I am here to answer any questions. I also"
        "offer blessings."
    ],
    "dialogue":priestDialogue
}

NPCs = {
    "chief": chief,
    "spirit": spirit,
    "drakes": ancestorGhost,
    "jormungandr": jormungandr,
    "daughter": daughter,
    "inn keeper": innKeeper,
    "priest": priest
}
