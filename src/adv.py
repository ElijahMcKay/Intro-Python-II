from room import Room
from player import Player
from item import Item
# importing sys so we can use sys.exit() to have the program stop on press of "q"
import sys
# Declare all the rooms

item = {
    "ruby": Item("ruby", "A shimmering jewel glints by the light of your torch."),
    "note": Item("note", "It is to smudged to read."),
    "book": Item("Spelunking for Dummies", "A book detailing the basics of cave exploration.  It looks as if it has never been opened."),
    "torch": Item("torch", "Illuminates the cave making it easier to explore and find items.", ),
}


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.  There are torches on either side of the cave opening.", [item['torch'], item['ruby'], item['note']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# room['outside'].itemArr.append('test')
# print(type(room['overlook'].itemArr))
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Gandalf", room['outside']) # constructed with a name, current_room


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# declaring this outside of loop, so it won't reset every time the loop iterates
currRoom = player.current_room

while True:
    print(f"You are now in {currRoom.name}.  {currRoom.description}\nYou find the following items:")
    
    currRoom.showItems()
    # for i in player.current_room.itemArr:
    print("What would you like to do?")
    # print("n + Enter to move north\ne + Enter to move east\ns + Enter to move south\nw + Enter to move west")
    # capturing the input
    userInput = input()
    # logic for moving cardinal directions
    if(hasattr(currRoom, f"{userInput}_to")):
        currRoom = getattr(currRoom, f"{userInput}_to")
    else:
        print("That doesn't lead anywhere.")


    # handling the user inputs the game
    if userInput == "q":
        print("Come back now, ya hear!")
        sys.exit()
    elif 'get' in userInput:
        # slicing the item the user wants out of the string they insert
        actionItem = userInput.split()
        # print(actionItem)
        if actionItem[1] not in player.itemArr:
            player.getItem(actionItem[1])
            player.current_room.showItems()
            print(f"You have picked up the {actionItem[1]}")
            print(f"You now have the following items:")
            player.showItems()
    elif 'drop' in userInput:
        # slicing the item the user wants out of the string they insert
        actionItem = userInput.split()
        if actionItem[1] in player.itemArr:
            player.dropItem(actionItem[1])
            player.current_room.itemArr.append(actionItem[1])

