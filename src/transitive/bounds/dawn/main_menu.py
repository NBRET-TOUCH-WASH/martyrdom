#coding:utf-8

#modules
#import blessings.mainMenu_asciiArt as asciiArt
#import lib.colorPrint as colorPrint

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
class MainMenu:
    """ main menu for the game """

    def __init__(self, titleHeader):
        self.titleHeader = titleHeader
        self.credits = '\t' * 7 + "NBRET-TOUCH-WASH, 2022"

        self.sections = {0:"1 - Play!",1:"2 - About",2:"3 - Settings",3:"4 - Quit"}


    def print_menu(self):
        color_print(self.titleHeader, Fore.RED)
        color_print(self.credits, Fore.LIGHTMAGENTA_EX, '\n')

        print('\n'*2 + '\t'*5 + '='*50)
        for s in self.sections.values():
            color_print('\t'*7 + ' '*5 + '{}'.format(s), Fore.LIGHTRED_EX)
        print('\t'*5 + '='*50)


    def select_option(self):
        """ allows the player to select one of the options in the main menu's sections """

        try:
            userChoice = int(input("Please select one of the options above:\n> "))
        except ValueError:
            print("Invalid option number, please try again.")
            return -1

        if 1 <= userChoice <= 4:
            return userChoice
        else:
            print("Invalid option number, please try again.")
            return -1



#functions



#variables
"""
? used for testing purposes
mainMenu1 = MainMenu()
"""



#script

"""
? used for testing purposes
mainMenu1.print_menu()
mainMenu1.select_option()
"""
