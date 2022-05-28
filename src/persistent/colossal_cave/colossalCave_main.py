#coding:utf-8

#modules
#import lib.location as location



#classes
class Element:
    """ class for any and all interactible elements """

    def __init__(self, name, shortDesc) -> None:
        #str
        self.name = name
        self.shortDesc = shortDesc #e.g. "A small yellowed out lamp." ; "A large snow-covered wood cabin"...


class Player(Element):
    """ class for the player, mainly used when the player interacts with themselves """

    def __init__(self, name, shortDesc, currentLocation, inventory, playerMood) -> None:
        super().__init__(name, shortDesc)

        #str ~ Location.name
        self.currentLocation = currentLocation

        #dict
        self.inventory = inventory      #e.g. "A pen", "A hat", "A key", "A crowbar"...

        #str
        self.mood = playerMood          #e.g. "Distressed" ; "Relieved" ; "Terrified" ; "Joyful"...


class Location(Element):
    """ class for locations, places, area, etc """

    def __init__(self, name, shortDesc, rooms, areaMood) -> None:
        super().__init__(name, shortDesc)

        #dict
        self.rooms = rooms
        """
            #WHYNOT: idk about this one since it's supposed to be a text-based segment.... :/
            self.areaMap = areaMap #ascii map
        """

        #str
        self.areaMood = areaMood #e.g. "spooky" ; "serene" ; "cozy" ; "hellish"...

class Room(Location):
    """ class for specific rooms inside of Locations """

    def __init__(self, name, shortDesc, rooms, areaMood, roomObjects, roomActions) -> None:
        #? the `rooms` parameter will be a single-entry dict
        super().__init__(name, shortDesc, rooms, areaMood)

        #dict
        self.objects = roomObjects      #e.g. "A lamp", "A key", "A window"...
        self.roomActions = roomActions  #e.g. "Open window", "Get key", "Read book"...


#? unused for now as it serves no purposes other than that of the `Element` class
#class Item(Element):
#    """ class for items """
#
#    def __init__(self, name, shortDesc) -> None:
#        super().__init__(name, shortDesc)



#functions
def play_colossal_cave():
    pass



#variables



#script