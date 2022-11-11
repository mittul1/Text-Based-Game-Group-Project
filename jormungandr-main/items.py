item_ax = {
    "id": "ax",

    "name": "an Ax",

    "description": "A family heirloom, old, but sturdy and well used",

    "is_weapon": True,

    "damage": 30,

    "accuracy": 75
}

item_saxe = {
    "id": "saxe",

    "name": "a Saxe",

    "description": "A norse Sea-Axe, just a big knife really",

    "is_weapon": True,

    "damage": 15,

    "accuracy": 85
}

item_gram = {
    "id": "gram",

    "name": "Gram",

    "description": "The mythical serpent slayer",

    "is_weapon": True,

    "damage": 40,

    "accuracy": 80
}

items_list = {
    "ax": item_ax,
    "saxe": item_saxe,
    "gram": item_gram
}

weapons_list = {key: items_list[key] for key in items_list if items_list[key]["is_weapon"]}
