from gameparser import normalise_input


def daughterDialogue():
    branch = -1
    while True:
        branch = branch + 1
        playerInput = input("Say: ")
        playerInput = normalise_input(playerInput)
        if branch == 0:
            if playerInput == ["yes"]:
                print(
                    "Frida" + ": " + "Are you going to help me then? No one else can. Are you going to leave to find a way to help?")

            elif playerInput == ["no"]:
                print("Your daughter just cries")
                raise KeyboardInterrupt

            else:
                break

        elif branch == 1:
            if playerInput == ["yes"]:
                print("Frida" + ": " + "I'll be okay until you come back. Be safe")
                break

            elif playerInput == ["no"]:
                print("Frida" + ": " + "But why?")
                print("Your daughter just cries")
                raise KeyboardInterrupt

            else:
                break


def priestDialogue():
    playerInput = input("Say: ")
    playerInput = normalise_input(playerInput)

    if "blessing" in playerInput:
        print("Priest: " + "Here, be blessed and go forth in the name of the gods. May you be guided by Odin's wisdom.")

    elif "illness" in playerInput:
        print(
            "Priest: " + "An illness? I'm afraid I cannot heal anyone physically, only spiritually. You should ask the Town Chief, he knows a lot about medicine.")

    else:
        print("Priest: " + "I'm afraid I cannot help you with something outside of spirituality and the gods.")


def spiritDialogue():
    branch = -1
    while True:
        branch = branch + 1
        playerInput = input("Say: ")
        playerInput = normalise_input(playerInput)
        if branch == 0:
            if "illness" in playerInput:
                print(
                    "Shrine God: " + "So your daughter is sick, and no one can cure her? Then you must go and claim a scale from the fabled World Serpent to cure her yourself.")

            elif "advice" in playerInput:
                print(
                    "Shrine God: " + "I will guide you through your battles, only if you devote yourself to me. You will gain immense power, only for a terrible price.")

            else:
                break

        elif branch == 1:
            if "yes" in playerInput:
                print(
                    "Shrine God: " + "Good, then I hope you will be a good disciple. Now go, go find the beastly snake and claim what is yours.")
                break
            elif "no" in playerInput:
                print("Shrine God: " + "You insult me, even after I offer you my blessing? Never return here.")
                break


def innKeeperDialogue():
    playerInput = input("Say: ")
    playerInput = normalise_input(playerInput)

    if playerInput == ["yes"]:
        print(
            "Inn Keeper: " + "Then there's plenty, I can offer you this one right here.")

    elif playerInput == ["no"]:
        print("Inn Keeper: " + "I'm sorry, but there's no other services we offer, have a nice day.")


def jormungandrDialogue():
    playerInput = input("Say: ")
    playerInput = normalise_input(playerInput)

    if "yes" in playerInput:
        print("Jörmungandr: " + "Such bravado, such confidence. Prepare to die.")

    elif "no" in playerInput:
        print("Jörmungandr: " + "Being modest will not save you here, Skarde.")


def chiefDialogue():
    branch = -1
    while True:
        branch = branch + 1
        playerInput = input("Say: ")
        playerInput = normalise_input(playerInput)
        if branch == 0:
            if "illness" in playerInput:
                print(
                    "Chief" + ": " + "Ah, I see. An incurable illness? Well, then you must take a scale from the deadly Jörmungandr to fix your daughter")

            else:
                print("Chief: " + "Then I give you my blessing, may the gods guide you.")
                break

        elif branch == 1:
            if "how" and "scale" in playerInput:
                print(
                    "Chief:" + ": " + "You can take a scale with this blade, a treasure of this town. To earn this favour, you will have to help us first. There's a camp of outlaws not far from here, they terrorise this town, see them dead and you can have this dagger.")

            elif "what" and "do" in playerInput:
                print("Chief" + ": " + "Perhaps you should think about how you can take a scale from this beast.")
                branch = branch + 1

            else:
                break

        elif branch == 2:
            if "kill" and "chief" in playerInput:
                print("Chief: " + "What? No, you cannot be doing this! Someone, anyone, help! Help!")
                break

            elif "ok" in playerInput:
                print("Chief: " + "Good, then I will be seeing you when you return successful.")
                break

            elif "no" in playerInput:
                print("Chief: " + "Then I'm afraid I can offer you no more help.")
                break

            else:
                break

        elif branch == 3:
            if "how" in playerInput:
                print("Chief: " +"You can take a scale with this blade, a treasure of this town. To earn this favour, you will have to help us first. There's a camp of outlaws not far from here, they terrorise this town, see them dead and you can have this dagger.")
                branch = branch - 2
            else:
                break

def ancestorGhostDialogue():
    pass


if __name__ == "__main__":
    chiefDialogue()
