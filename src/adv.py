from room import Room
from player import Player
from item import Item
# importing sys so we can use sys.exit() to have the program stop on press of "q"
import sys
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Gandalf", room['outside']) # constructed with a name and current_room attribute

# print(player.current_room) # gives me a name "Gandalf, and a current_room: "Outside Cave Entrance" attribute
# print("room outside", room['outside'])
# creating variables for common
currentRoom = player.current_room
# roomDescription = currentRoom.description

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
    print(f"You are now in {currentRoom}.  {currentRoom.description}\nWhat would you like to do?")
    # print("n + Enter to move north\ne + Enter to move east\ns + Enter to move south\nw + Enter to move west")
    # capturing the input
    userInput = input()

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


# playing around with how I'm going to allow the user to quit the program
# quit = input()

# if quit == "q":
#     print("Come back now, ya hear!")
#     sys.exit()
# else:
#     print('kept going')