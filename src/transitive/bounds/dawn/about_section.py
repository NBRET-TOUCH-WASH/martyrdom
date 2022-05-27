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
class AboutSection:
    """ main menu's about section """

    def __init__(self, aboutHeader):
        self.header = aboutHeader
        self.credits = "\t\tNBRET-TOUCH-WASH, 2022"

        self.body = """
Hello and wlecome to Martyrdom!


This is a "small" game I've put together as the final NSI mini-project of this year.
It was a lot of effort, I learned quite a bit of stuff while making it and I'm happy of the trajectory it's taking so far (the game isn't finished as I'm writing this)!


Anyway, I hope you have fun playing this thing, just a little piece of advice before starting:
\t\t\t~ In this game, looks are deceiving... ~


Enjoy!
"""


    def print_about_section(self):
        color_print(self.header, Fore.RED)
        print("")
        print(self.credits)
        print('\t' * 2, '- ' * 10, '\n\n')

        print(self.body)


#functions



#variables
#about1 = AboutSection()



#script
#about1.print_about_section()