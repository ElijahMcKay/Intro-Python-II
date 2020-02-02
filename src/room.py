# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    # base class for rooms
    def __init__(self, name, description, itemArr):
        self.name = name
        self.description = description
        self.itemArr = itemArr

    def __str__(self):
        return f"{self.itemArr}"
