#!/usr/bin/python3
import os
import pickle
import random

import map
from map import rooms as default_rooms
from player import player as default_player
from items import items_list, weapons_list
from gameparser import normalise_input
from enemies import enemies
from npcs import NPCs

global rooms
global player


def display_text(text):
    for line in text:
        print("\033[0m" + line)


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item."""

    # print the list of items if there are items in the room
    items = room["items"]
    if items:
        print(f"\nThere is: ")
        for item in items:
            print("  " + item['name'])


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global player
    exits = player["current_room"]["exits"]
    if direction in exits:
        if player["current_room"]["enemies"]:
            enemy = player["current_room"]["enemies"][0]
            if enemy['health'] > 0:
                print(f"\033[0mThe {enemy['name']} blocks your way. Looks like you\'ll have to fight your way out")
                return
        player["current_room"] = rooms[player["current_room"]["exits"][direction]]
        if not player["current_room"]["visited"] and player["current_room"]["story"]:
            display_text(player["current_room"]["story"])
            player["current_room"]["visited"] = True
        else:
            execute_look()
    else:
        print("\033[0mYou cannot go there.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    global player
    for item in player["current_room"]["items"]:
        if item["id"] == item_id:
            player["inventory"].append(item)
            player["current_room"]["items"].remove(item)
            print(f"\033[0mTook {item_id}.")
            return

    print("\033[0mYou cannot take that.")


def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    global player
    for item in player["inventory"]:
        if item["id"] == item_id:
            player["current_room"]["items"].append(item)
            player["inventory"].remove(item)
            print(f"\033[0mDropped {item_id}.")

            return

    print("\033[0mYou cannot drop that.")


def execute_look():
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this)."""

    global player
    # Display room description
    display_text(player["current_room"]["description"])
    print_room_items(player["current_room"])


def execute_examine(item_id):
    """Displays the description of an item"""

    global player
    for item in player["inventory"] + player["current_room"]["items"]:
        if item["id"] == item_id:
            print("\033[0m" + item["description"])
            return

    print(f"\033[0mYou can\'t see any {item_id} here")


def execute_view_inventory():
    """Displays all the items in the player's inventory in an aesthetic
    list under the header 'You Have:'"""
    if player["inventory"]:
        print("\033[0mYou have:")
        for item in player["inventory"]:
            print("  " + item["name"])
    else:
        print("\033[0mYou don't have anything in your inventory")


def execute_fight(action, enemy_id, weapon_id):
    """This function takes the player"s intended action, enemy_id and
    weapon_id and calculates any changes to health based on the stats
    of the weapon, player and enemy. Then one character attacks another,
    they have the chance to miss. If they don't miss, the other player
    has a chance to dodge the successful attack. If the dodge fails then
    changes to health are calculated. The player attacks first, and if
    the enemy didn't die after the player's action, the enemy attacks."""

    global player
    global enemies

    # define variables for fight
    enemy = enemies[enemy_id]
    weapon = weapons_list[weapon_id]

    # Calculate whether the player manages to hit the enemy and display appropriate message
    if random.randint(0, 100) <= weapon["accuracy"]:
        if random.randint(0, 100) <= player["evasion"]:
            print(f"\033[0mYou try to {action} the {enemy_id} with your {weapon_id}, but they dodge.")
        else:
            enemy["health"] -= weapon["damage"]
            if enemy["health"] < 1:
                print(
                    f"\033[0mYou fatally wound the {enemy_id} with your {weapon_id}.",
                    f"You watch the light leave the their eyes.\n")
            else:
                print(
                    f"\033[0mYou {action} the {enemy_id} with your {weapon_id}",
                    f"leaving them on {enemy['health']} health.")
    else:
        print(f"\033[0mYou try to {action} the {enemy_id} with your {weapon_id}, but you miss.")

    # check the enemy is still alive and so can attack the player back
    if enemy["health"] > 0:
        # Pick a random ability
        ability_name = random.choice(list(enemy["abilities"].keys()))
        ability = enemy["abilities"][ability_name]

        # Calculate whether the enemy manages to hit the player and display appropriate message
        if random.randint(0, 100) <= ability["accuracy"]:
            if random.randint(0, 100) <= player["evasion"]:
                print(f"The {enemy_id} tries to {ability_name} you, but you dodge.")
            else:
                # TODO change to more readable messages scratchs -> scratches
                player["health"] -= ability["damage"]
                if player["health"] < 1:
                    print(f"The {enemy_id} {ability_name}s you, and you perish from your wounds.")
                else:
                    print(f"The {enemy_id} {ability_name}s you leaving you on {player['health']} health.")
        else:
            print(f"The {enemy_id} tries to {ability_name} you, but misses.")

    # if the player survived print the end of fight story
    if player["health"] > 0 and enemy['health'] < 1:
        enemies.pop(enemy_id)
        for npc in NPCs:
            if npc == enemy_id:
                NPCs.pop(enemy_id)
                break
        display_text(player["current_room"]["fight_end"])


def execute_help():
    """Displays all the available commands"""
    print(
        "\033[0mEXAMINE/X <ITEM>",
        "TAKE <ITEM>",
        "DROP <ITEM>\n",
        "GO <DIRECTION>",
        "LOOK/L",
        "HELP/COMMANDS",
        "ATTACK <NPC/ENEMY> WITH <WEAPON/ITEM>",
        sep="\n"
    )


def execute_listen():
    """displays a message and modifies the map's story of the player is in an
    area that allows for listening"""
    if player["current_room"]["name"] == "Town Tavern":
        display_text([
            "You overhear some townspeople discussing the town elder's vast knowledge",
            "of ailments. Perhaps you should visit him to learn more about your",
            "daughter's illness."
        ])
        addition = [
            "You've heard that people respect this man a lot, and come to him for",
            "guidance, hopefully you can do the same."
        ]
        story = rooms["Hall"]["story"]
        rooms["Hall"]["story"] = story[:1] + addition + story[1:]
    else:
        print("\033[0mThere's nothing to hear here.")


def execute_speak(NPCname):
    """Initiates dialogue between player and NPC. Starts by printing the description of the NPC"""
    print("\033[0m" + NPCs[NPCname]["name"] + ":")
    display_text(NPCs[NPCname]["description"])
    display_text(NPCs[NPCname]["intro"])
    NPCs[NPCname]["dialogue"]()


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """

    if len(command) == 0:
        print("\033[0mThis makes no sense.")
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("\033[0mGo where?")

    elif command[0] in ["n", "s", "e", "w"]:
        dirs = {"n": "north", "s": "south", "e": "east", "w": "west"}
        execute_go(dirs[command[0]])

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("\033[0mTake what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("\033[0mDrop what?")

    elif command[0] in ["examine", "x"]:
        if len(command) > 1:
            execute_examine(command[1])
        else:
            print("\033[0mExamine what?")

    elif command[0] in ["look", "l"]:
        execute_look()

    elif command[0] == "inventory":
        execute_view_inventory()

    elif command[0] == "listen":
        execute_listen()

    elif command[0] in ["hit", "stab", "wound", "fight", "attack", "strike", "chop", "kill"]:
        if len(command) == 1:
            print(f"\033[0m{command[0]} what with what?")

        # if the command is partially complete
        elif len(command) == 2:
            if command[1] not in enemies:
                print(f"\033[0mI don't understand '{command[1]}'")
            elif enemies[command[1]] not in player["current_room"]["enemies"]:
                print(f"\033[0mTheres no {command[1]} here to {command[0]}.")
            else:
                print(f"\033[0m{command[0]} the {command[1]} with what?")

        # if the command is complete
        elif len(command) == 3:
            if command[1] not in enemies:
                print(f"\033[0mWhats a {command[1]}?")
            elif enemies[command[1]] not in player["current_room"]["enemies"]:
                print(f"\033[0mThere's no {command[1]} to {command[0]} here.")
            elif command[2] not in items_list:
                print(f"\033[0mI don't understand {command[2]}.")
            elif command[2] not in weapons_list:
                print(f"\033[0mYou can't fight with {items_list[command[2]]['name']}.")
            elif weapons_list[command[2]] not in player['inventory']:
                print(f"\033[0mYou don't have {weapons_list[command[2]]['name']}.")
            else:
                execute_fight(*command)
        else:
            print(f"\033[0m{command[0]} what with what?")

    elif command[0] in ["help", "commands"]:
        execute_help()

    elif command[0] == "save":
        save_game()
        print("\033[0mSave successful.")

    elif command[0] in ["talk", "speak"]:
        if len(command) == 1:
            print(f"\033[0m{command[0]} with who?")
        elif command[1] in NPCs and NPCs[command[1]] in player["current_room"]["npcs"]:
            execute_speak(command[1])
        else:
            print(f"\033[0m{command[0]} with who?")

    else:
        print("\033[0mThis makes no sense.")


def save_game():
    """Pickle game objects and save them to a text file"""
    global player
    global rooms

    f_name = input("\033[0mEnter the full name of the file to save to\n\n\033[94m> ")
    save_data = [player, rooms]

    with open(f_name, "wb") as file:
        pickle.dump(save_data, file)


def load_game():
    """Loads the game data from a save file using object serialisation"""
    global player
    global rooms

    f_name = input("\033[0mEnter the full name of the save file to load\n\033[94m> ")

    with open(f_name, "rb") as file:
        save_data = pickle.load(file)

    return save_data[0], save_data[1]


def display_game_menu():
    """Displays the main game menu to the user, of whether they want to start
    a new game or load a pre-saved game."""
    global player
    global rooms

    print('\033[1mJörmungandr\033[0m')
    print("1. new game")
    print("2. load save file")
    choice = input("\n\033[94m> ")

    if choice == "1":
        player = default_player
        rooms = default_rooms

        # Display the introduction to the jormungandr storyline
        display_text(rooms["Cabin"]["story"])

    elif choice == "2":
        player, rooms = load_game()


def open_temple_path():
    if map.room_town_hall["visited"] and map.room_graveyard["visited"] and map.room_shrine["visited"]:
        rooms["Graveyard"]["exits"]["north"] = 'Temple Trail'


# This is the entry point of our programz
def main():
    # clear the commandline and enable ansi coloring
    os.system("cls")
    os.system("color")

    # global game state variables
    global player
    global rooms

    # Display game menu
    display_game_menu()

    # Main game loop

    while True:
        # Read and normalise player's input
        user_input = input("\n\033[94m> ")
        command = normalise_input(user_input)
        open_temple_path()

        # Execute the player's command
        execute_command(command)

        if NPCs["jormungandr"] not in rooms["Lake"]["npcs"]:
            print("Congratulations for completing the game!")
            break


if __name__ == "__main__":
    main()
