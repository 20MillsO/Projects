# Import Required Modules
from time import sleep
import random

# Useful Information for Programmer
"WEAPONS: 'Sword of Flames', 'Bow of the Wind', 'Shadow Dagger'"
"ARMOUR: 'Dragon Scale Armour', 'Mystic Robes', 'Stealth Cloak'"
"POTIONS: 'Healing Potion', 'Magic Elixir', 'Strength Brew'"
"TOOLS: 'Grappling Hook', 'Lockpicking Kit', 'Magic Compass'"
"ARTIFACTS: 'Amulet of Protection', 'Ring of Invisibility', 'Crystal of Teleportation'"
"MISCELLANEOUS: 'Map of the Realm', 'Bag of Holding', 'Journal'"

# Lists
weapons = ["Sword of Flames", "Bow of the Wind", "Shadow Dagger"]
armour = ["Dragon Scale Armour", "Mystic Robes", "Stealth Cloak"]
potions = ["Healing Potion", "Magic Elixir", "Strength Brew"]
tools = ["Grappling Hook", "Lockpicking Kit", "Magic Compass"]
artifacts = ["Amulet of Protection", "Ring of Invisibility", "Crystal of Teleportion"]
miscellaneous = ["Map of the Realm", "Bag of Holding", "Journal"]

# Configuration
simulateLoading = False

# Loading Program
def loadProgram():
    print("Program now loading...")
    sleep(5)
    print("Program loaded successfully!\n")
    sleep(1)
    mainMenu()

# Main Menu
def mainMenu():
    global menuChoice
    print("MAIN MENU:")
    print("1. Start Story")
    print("2. Admin Menu\n")
    menuChoice = int(input("> "))
    mainMenu_Handler()

# Admin Menu
def adminMenu():
    global adminChoice
    print("\n")
    print("=========================")
    print("      HERO'S ARSENAL     ")
    print("       ADMIN MENU        ")
    print("=========================")
    print("1. View Inventory Options")
    print("2. Add Item to Inventory Options")
    print("3. Remove Item from Inventory Options")
    print("4. Exit Admin Menu")
    adminChoice = int(input("> "))
    adminHandler()

# Admin Menu Handler
def adminHandler():
    global adminChoice
    if adminChoice == 1:
        print("\n")
        print("WEAPONS:", weapons)
        print("ARMOUR:", armour)
        print("POTIONS:", potions)
        print("TOOLS:", tools)
        print("ARTIFACTS", artifacts)
        print("MISCELLANEOUS:", miscellaneous)
    elif adminChoice == 2:
        global addListChoice
        print("SELECT LIST TO MODIFY:")
        print("1. WEAPONS:", weapons)
        print("2. ARMOUR:", armour)
        print("3. POTIONS:", potions)
        print("4. TOOLS:", tools)
        print("5. ARTIFACTS", artifacts)
        print("6. MISCELLANEOUS:", miscellaneous, "\n")
        addListChoice = int(input("> "))
        addListChoiceHandler()
    elif adminChoice == 3:
        global removeListChoice
        print("SELECT LIST TO MODIFY:")
        print("1. WEAPONS:", weapons)
        print("2. ARMOUR:", armour)
        print("3. POTIONS:", potions)
        print("4. TOOLS:", tools)
        print("5. ARTIFACTS", artifacts)
        print("6. MISCELLANEOUS:", miscellaneous, "\n")
        removeListChoice = int(input("> "))
        removeListChoiceHandler()
    elif adminChoice == 4:
        print("\n")
        mainMenu()
    else:
        print("Error Code 01: Invalid argument entered.")
        adminMenu()

# addListChoice Handler
def addListChoiceHandler():
    global addListChoice
    if addListChoice == 1:
        addItem = input("ENTER ITEM TO BE ADDED TO 'WEAPONS' LIST: ")
        weapons.append(addItem)
        print(addItem, "HAS BEEN ADDED TO THE 'WEAPONS' LIST SUCCESSFULLY")
        adminMenu()
    elif addListChoice == 2:
        addItem = input("ENTER ITEM TO BE ADDED TO 'ARMOUR' LIST: ")
        weapons.append(addItem)
        print(addItem, "HAS BEEN ADDED TO THE 'ARMOUR' LIST SUCCESSFULLY")
        adminMenu()
    elif addListChoice == 3:
        addItem = input("ENTER ITEM TO BE ADDED TO 'POTIONS' LIST: ")
        weapons.append(addItem)
        print(addItem, "HAS BEEN ADDED TO THE 'POTIONS' LIST SUCCESSFULLY")
    elif addListChoice == 4:
        addItem = input("ENTER ITEM TO BE ADDED TO 'TOOLS' LIST: ")
        weapons.append(addItem)
        print(addItem, "HAS BEEN ADDED TO THE 'TOOLS' LIST SUCCESSFULLY")
    elif addListChoice == 5:
        addItem = input("ENTER ITEM TO BE ADDED TO 'ARTIFACTS' LIST: ")
        weapons.append(addItem)
        print(addItem, "HAS BEEN ADDED TO THE 'ARTIFACTS' LIST SUCCESSFULLY")
    elif addListChoice == 6:
        addItem = input("ENTER ITEM TO BE ADDED TO 'MISCELLANEOUS' LIST: ")
        weapons.append(addItem)
        print(addItem, "HAS BEEN ADDED TO THE 'MISCELLANEOUS' LIST SUCCESSFULLY")

# removeListChoice Handler
def removeListChoiceHandler():
    global removeListChoice
    if removeListChoice == 1:
        addItem = input("ENTER ITEM TO BE REMOVED TO 'WEAPONS' LIST: ")
        weapons.pop(addItem)
        print(addItem, "HAS BEEN REMOVED TO THE 'WEAPONS' LIST SUCCESSFULLY")
        adminMenu()
    elif removeListChoice == 2:
        addItem = input("ENTER ITEM TO BE REMOVED TO 'ARMOUR' LIST: ")
        weapons.pop(addItem)
        print(addItem, "HAS BEEN REMOVED TO THE 'ARMOUR' LIST SUCCESSFULLY")
        adminMenu()
    elif removeListChoice == 3:
        addItem = input("ENTER ITEM TO BE REMOVED TO 'POTIONS' LIST: ")
        weapons.pop(addItem)
        print(addItem, "HAS BEEN REMOVED TO THE 'POTIONS' LIST SUCCESSFULLY")
    elif removeListChoice == 4:
        addItem = input("ENTER ITEM TO BE REMOVED TO 'TOOLS' LIST: ")
        weapons.pop(addItem)
        print(addItem, "HAS BEEN REMOVED TO THE 'TOOLS' LIST SUCCESSFULLY")
    elif removeListChoice == 5:
        addItem = input("ENTER ITEM TO BE REMOVED TO 'ARTIFACTS' LIST: ")
        weapons.pop(addItem)
        print(addItem, "HAS BEEN REMOVED TO THE 'ARTIFACTS' LIST SUCCESSFULLY")
    elif removeListChoice == 6:
        addItem = input("ENTER ITEM TO BE REMOVED TO 'MISCELLANEOUS' LIST: ")
        weapons.pop(addItem)
        print(addItem, "HAS BEEN REMOVED TO THE 'MISCELLANEOUS' LIST SUCCESSFULLY")

# Introduction
def introduction():
    global isCandidate
    print("Welcome to 'The Hero's Hidden Arsenal'.")
    sleep(1)
    print("You'll be drawn into a world where every item holds a secret, and every secret holds a power.")
    sleep(5)
    print("As the hero, you'll uncover the mysteries of your hidden arsenal, facing challenges and foes that test your courage and wit.")
    sleep(6)
    print("With each discovery, the stakes will grow higher, and the true purpose of your journey will become clear.")
    sleep(5)
    print("Will you unlock the ultimate power or fall to the shadows that seek to claim it?\n")
    sleep(5)
    isCandidate = input("Are you the person we're looking for? (Y/N) ")
    isCandidate_Handler()

# isCandidate Handler
def isCandidate_Handler():
    global isCandidate
    if isCandidate == "Y":
        print("=========================\n        THE PROLOGUE     \n=========================\n")
        print("In a world where magic and technology coexist, the balance between light and darkness is maintained by the ancient Guardians.")
        sleep(6)
        print("However, a cataclysmic event known as the Shattering has disrupted this balance, plunging the world into chaos.")
        sleep(5)
        print("The hero, a young and unassuming individual named Arin, discovers they are the last descendant of the Guardians, destined to restore harmony.\n")
        sleep(6)
        startStory()
    elif isCandidate == "N":
        print("Turn away from the shadows that beckon you.")
        sleep(3)
        print("The world will remain in darkness, its cries for a saviour unanswered.")
        sleep(4)
        print("Perhaps another time, another place, you will find the strength to face your destiny.")
        sleep(4)
        quit()

# Start Story
def startStory():
    item =

# Chapter 1
def chapterOne():
        print("=========================\n        CHAPTER ONE      \n=========================\n")
        sleep(1)
        print("
        

# Main Menu Handler
def mainMenu_Handler():
    global menuChoice
    if menuChoice == 1:
        introduction()
    elif menuChoice == 2:
        adminMenu()
    else:
        print("Error Code 01: Invalid choice")
        mainMenu()

# Check whether to simulate loading
if simulateLoading == True:
    loadProgram()
elif simulateLoading == False:
    mainMenu()
else:
    print("Error Code 01: Invalid choice")
