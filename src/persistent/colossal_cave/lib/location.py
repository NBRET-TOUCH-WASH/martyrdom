#coding:utf-8

#modules



#classes
class Location:
    """ class for locations, places, area, etc """

    def __init__(self, areaName, rooms, shortDesc, areaMood) -> None:
        #str
        self.areaName = areaName

        #dict
        self.rooms = rooms

        """
        WHYNOT: idk about this one since it's supposed to be a text-based segment.... :/
        #str (ascii map)
        self.areaMap = areaMap
        """

        #str
        self.shortDesc = shortDesc  #e.g. "A small snow-covered wood cabin."
        self.areaMood = areaMood    #e.g. "spooky" ; "serene" ; "cozy" ; "hellish"...



#functions



#variables
#$ DOC UNUSED IN THE FIRST TWO MINUTES LMAO
#? sample Location class variable:
# locationExampleMap = """
#  ___________     ___________
# |           |___|           |
# |     0      ___      1     |
# |           |   |           |
# \___________/   \___________/
# """
# locationExample = Location("Debug Area",{0:"Debug Room",1:"Debug closet"},locationExampleMap,"Debuggy")



#script