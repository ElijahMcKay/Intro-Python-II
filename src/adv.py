from room import Room
from player import Player
from item import Item
# importing sys so we can use sys.exit() to have the program stop on press of "q"
import sys
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.  There are torches on either side of the cave opening."),

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

# creating items
item = {
    "ruby": Item("ruby", "A shimmering jewel glints by the light of your torch."),
    "note": Item("note", "It is to smudged to read."),
    "book": Item("Spelunking for Dummies", "A book detailing the basics of cave exploration.  It looks as if it has never been opened."),
    "torch": Item("torch", "Illuminates the cave making it easier to explore and find items.", ),
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

# adding items to rooms
room['outside'].itemArr = [item['torch']]
room['foyer'].itemArr = [item['book']]
room['narrow'].itemArr = [item['note']]
room['overlook'].itemArr = [item['ruby']]

# room['outside'].itemArr.append('test')
# print(type(room['overlook'].itemArr))
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Gandalf", room['outside']) # constructed with a name, current_room, and empty itemArr attribute

currentRoom = player.current_room
roomItems = currentRoom.itemArr
player.itemArr = ['test', 'test', 'test']


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

# print(player)
while(currentRoom != 'treasure'):
    print(f"You are now in {currentRoom}.  {currentRoom.description}\nYou find the following items:")
    print(roomItems[0])
    
    print("What would you like to do?")
    # print("n + Enter to move north\ne + Enter to move east\ns + Enter to move south\nw + Enter to move west")
    # capturing the input
    userInput = input()

    # logic for moving cardinal directions
    if(hasattr(currentRoom, 'n_to') and userInput == 'n'):
        currentRoom = currentRoom.n_to
    elif(hasattr(currentRoom, 'e_to') and userInput == 'e'):
        currentRoom = currentRoom.e_to
    elif(hasattr(currentRoom, 's_to') and userInput == 's'):
        currentRoom = currentRoom.s_to
    elif(hasattr(currentRoom, 'w_to') and userInput == 'w'):
        currentRoom = currentRoom.w_to
    else:
        print("That doesn't lead anywhere.")


    # handling the user quitting the game
    if userInput == "q":
        print("Come back now, ya hear!")
        sys.exit()
