#coding:utf-8

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

#import lib.location as location



#classes rebirth
class Element:
    """ class for any and all elements """

    def __init__(self, name, shortDesc) -> None:
        self.name = name
        self.shortDesc = shortDesc



class Location(Element):
    """ class for locations/areas... """

    def __init__(self, name, shortDesc, areaMood, **rooms) -> None:
        super().__init__(name, shortDesc)

        self.areaMood = areaMood
        self.rooms = rooms

class Room(Element):
    """ class for specific rooms """

    def __init__(self, name, shortDesc, roomMood, roomObjects, roomActions) -> None:
        super().__init__(name, shortDesc)

        self.roomMood = roomMood

        self.roomObjects = roomObjects
        self.roomActions = roomActions



class Player(Element):
    """ class for the player """

    def __init__(self, name, shortDesc, playerMood, currentRoom, **inventory) -> None:
        super().__init__(name, shortDesc)

        self.playerMood = playerMood
        self.currentRoom = currentRoom
        self.inventory = inventory



#? unused for now as it serves no purposes other than that of the `Element` class
#class Item(Element):
#    """ class for items """
#
#    def __init__(self, name, shortDesc) -> None:
#        super().__init__(name, shortDesc)



#functions
def clear_console():
    """ clears the current console output """

    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



def play_colossal_cave():
    clear_console()
    time.sleep(1)
    print(R"""
       .                                                                        
     ..:::...                                                                   
     .:.::^:......                                                              
     .....:^^:::::..                                                            
    .    ...:::^^!::..                                                          
            ...:^!^::..                                                         
              ..::^!~::...                                                      
               ..::^7!^^::...                                                   
                ..:^~??!!~^::..                                                 
                ..:^!~~~~!77~::..                                               
                ..::~~:::^^~?!^::..                                             
              ...:^^^:....::^!77!^:..                                           
             ...:^:....   ..::^~?7^:..                                          
          ....:::...        .::^!J^^:.                                          
        ...:::...            .:^~J~^:..                                         
         .....              ..:^~7J^^:.                                         
          ..               .:^~~!JY~~^:..                                       
          .              ..:^~?YY5PY?!~^^:...                                   
          .              ..:^7G7777?JYJ7!~^^::.                                 
                          .::^?^^^~~~!?YYJY?~^^::..       ........              
                            ........:^^~!775Y!!~~^^^:::::^^^^^^^^:::...         
                                     ..::^~!Y5YY5Y?7!!!!777?J55J??7~~^:::...    
                                        ..:^~!?Y5JYY5YY5YYJJ??YPYJJJ?J7!~~^:.   
                                          .:^~JJ!!!!!!!~~~~~~~~!?Y5J??J??7!^:.  
                                           .::^7?7~~^^^:::...::^~!?Y55P5J!~^:.  
                                            ..::^!77!^^:..  ..::^~!7JYYY5J~^:.  
                                             ..::^^!J?!^::...:^!7777!~~~~~^:.   
                                           .....:^^!??J~~^::^^?!~^::::::...     
                                            ..:::^^~7??7~~~~~!J~^::.            
                                           ...::~^~~7!~77~!!!JJ~^:.             
                                          ...^^^~^^^^^^~7!!7?Y7~^:.             
                                         ...:~:::....::^~7?JYY7~~^:.            
                                       ...::^:.......::^!7777!!~^::.            
                                       .:::::......::^^~~^~~^^::..              
                                      .:...:....:^^^^:::::^^...                 
                                      ..   ..:.:~::.......::.                   
                                      .     ..::^:...                           
                                             ..:^:..                            
                                              .::..                             
                                                .                               
""")
    time.sleep(0.25)

    clear_console()
    time.sleep(2)
    print("When you open your eyes for what feels like the first time in about seven months, you notice you've been transported somewhere.")
    time.sleep(4)
    print("It is dark, rainy and stormy, making out the shape of the things before you is hard.")
    time.sleep(3)
    print("\nAfter a few seconds of effort, you start to combine the few elements your brain can properly process:")
    time.sleep(4)
    print("A door, ", end="")
    time.sleep(1)
    print("windows, ", end="")
    time.sleep(1)
    print("a roof...")
    time.sleep(2)
    print("\nYou realize you're standing before a house, the lightnings' glow rapidly printing its image on your retina.")
    time.sleep(4)
    print("Ahead of you is a path to enter said house ; behind you, a road, crossing your path left to right from the edges of a street that seemingly stretches into infinity.\n")
    time.sleep(6)

    while True:
        userInput = input("What will you do?\n> ")



#variables
#! debug
#debugOffice = Room("Debug Office","Offices for debugging.","Debuggier",["DEBUG MUG","DEBUG TABLE"],["FLIP TABLE","DRINK MUG"])
#debugDpt = Location("Debug Dpt.","Debug Department","Debuggy",{debugOffice:0,"DEBUG CORRIDOR":1})


#script
play_colossal_cave()