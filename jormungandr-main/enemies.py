enemy_wolf = {
    "name": "Wolf",
    "health": 30,
    "speed": 30,
    "evasion": 10,
    "abilities": {
        "scratch": {
            "damage": 5,
            "accuracy": 100
        },
        "bite": {
            "damage": 10,
            "accuracy": 90
        }
    }
}

enemy_bandit = {
    "name": "Bandit",
    "health": 65,
    "speed": 55,
    "evasion": 33,
    "abilities": {
        "strike": {
            "damage": 10,
            "accuracy": 90
        },
        "eviscerate": {
            "damage": 15,
            "accuracy": 75
        }
    }
}

enemy_bandit_boss = {
    "name": "Bandit Boss",
    "health": 100,
    "speed": 60,
    "evasion": 33,
    "abilities": {
        "strike": {
            "damage": 20,
            "accuracy": 60
        },
        "eviscerate": {
            "damage": 25,
            "accuracy": 75
        }
    }
}

# enemy_ranged_bandit = {
#     "name": "bandit",
#     "health": 35,
#     "speed": 45,
#     "evasion": 25,
#     "abilities": {
#         "scratch": {
#             "damage": 5,
#             "accuracy": 100
#         },
#         "bite": {
#             "damage": 10,
#             "accuracy": 90
#         }
#     }
# }

enemy_ghost = {
    "name": "ghost",
    "health": 20,
    "speed": 60,
    "evasion": 50,
    "abilities": {
        "curse": {
            "damage": 5,
            "accuracy": 90
        },
    }
}

enemy_corpse = {
    "name": "animated corpse",
    "health": 20,
    "speed": 60,
    "evasion": 50,
    "abilities": {
        "Limp Whack": {
            "damage": 10,
            "accuracy": 80
        },
    }
}

enemy_spirit = {
    "name": "spirit",
    "health": 20,
    "speed": 60,
    "evasion": 50,
    "abilities": {
        "Elders Judgement": {
            "damage": 10,
            "accuracy": 80
        },
    }
}


enemy_jormungandr = {
    "name": "jormungandr",
    "health": 250,
    "speed": 55,
    "evasion": 10,
    "abilities": {
        "acid_pool": {
            "damage": 5,
            "accuracy": 100
        },
        "acid_shot": {
            "damage": 10,
            "accuracy": 90
        },
        "tail_whip": {
            "damage": 15,
            "accuracy": 75
        }
    }
}

enemies = {
    "wolf": enemy_wolf,
    "bandit": enemy_bandit,
    "bandit boss": enemy_bandit_boss,
    # "ranged_bandit": enemy_ranged_bandit,
    "ghost": enemy_ghost,
    "jormungandr": enemy_jormungandr,
    "corpse": enemy_corpse,
    "spirit": enemy_spirit

}
