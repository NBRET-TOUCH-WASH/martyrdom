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
class SettingsSection():
    """ main menu's settings section """

    def __init__(self, settingsHeader):
        self.header = settingsHeader

        self.settings = None
        self.body = """
\t\t\t\tThere are no settings.

\t\t\t\tWhen they say make game fast,
\t\t\t\tGame make fast,
\t\t\t\tBut game not good.


\t~ based on Kirillian's "This is literally the worst. Game. Ever.", 2021
"""


    def print_settings_section(self):
        color_print(self.header, Fore.RED)
        print("")
        color_print(self.body + '\n\n', Fore.LIGHTYELLOW_EX)



#functions



#variables
#settings1 = SettingsSection()



#script
#settings1.print_settings_section()