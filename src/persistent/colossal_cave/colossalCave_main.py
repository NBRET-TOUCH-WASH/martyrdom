#coding:utf-8



"""
[X] ============================================================ [X]
 |                                                                |
 |                ABANDONNED TO THE MISTS OF TIME!                |
 |                                                                |
[X] ============================================================ [X]
"""



#modules
import os
import time

#? colorama lib setup
from colorama import init, Fore, Back, Style
init()

FORES = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
BRIGHTNESS = [Style.DIM, Style.NORMAL, Style.BRIGHT]

def color_print(s, color = Fore.WHITE, brightness = Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function
    but with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)



#classes
class Element:
    """ base unit for in-game objects """

    def __init__(self, name, details) -> None:
        self.name = name
        #? description used when the object is looked at by the player
        self.details = details



class Player(Element):
    """ class for the player """

    def __init__(self, name, details, currentLoc) -> None:
        super().__init__(name, details)

        #Room class
        self.currentLoc = currentLoc

        #list
        #§ TBA
        #self.inventory = inventory


    def analyze_input(self, playerInput):
        """ analyzes the player's input and selects a corresponding action """

        if "GO" in playerInput:
            playerInput = playerInput.split()
            for w in range(0,len(playerInput)-1,1):
                if playerInput[w] == "GO" and playerInput[w+1] == "TO":
                    self.go_to(self.currentLoc,playerInput[w+2])


    def go_to(self, currentLoc, destination):
        """ allows the player to move from one room to another """

        if destination in currentLoc.neighborRooms:
            currentLoc = destination
        else:
            pass

        return currentLoc

    def look_at(self):
        """ allows the player to look at specific elements, offering more details """
        pass

    def get_item(self):
        """ allows the player to get a specific item """
        pass 



class Room(Element):
    """ class for all places the player can go to """

    def __init__(self, name, details, *neighborRooms) -> None:
        super().__init__(name, details)

        self.neighborRooms = neighborRooms

        #self.roomItems = roomItems
        #self.roomActions = roomActions



#functions



#variables
testRoom1 = Room("Room1",
                "first room",
                ("room2"))

testRoom2 = Room("Room2",
                "second room",
                ("room1"))

player1 = Player("Avery Doe","Average player.","room1")



#script
playerInput = input("What to do?\n> ").upper()
player1.analyze_input(playerInput)
input()