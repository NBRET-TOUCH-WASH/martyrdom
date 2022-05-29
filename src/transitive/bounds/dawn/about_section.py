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
        self.credits = "\t\tNBRET-TOUCH-WASH"

        self.body = """
Hi! Welcome to Martyrdom!

This is a game I've created as part of the final NSI mini-project for the 2022 schoolyear.

I learned quite a bit of stuff while making it and experimented several new things with the console and the Python language.
I also ran into my fair share of issues during development, some of which I've found out how to patch or find a workaround for, some others I just couldn't.

There still are two bugs, although one technically is an exploit, both of which I won't fix, not because I don't have the required technical abilities to do so, but more because while this game started as a well-organized and planned project, it quickly turned into a nightmarish mess of spaghetti code (for any of the people looking into the source code, the first comment in the main file will set the tone), just look at how empty the changelog is... So if anyone wants to take a chance at cracking them open and fixing them, go ahead I guess... :P

I should also add that due to personal obligations (and thus time-restraint reasons) as well as a lack of OOP and abstract thinking abilities, this game isn't complete, or at least not as much as I wish it'd was.
I had to cut off a SIGNIFICANT part from the originally planned content, in addition to already removing one the game's planned section, judged redundant when put next to the rest of the game.
As such, the game ends in a suprisingly abrupt way after throwing many lore-relevant elements at the player, all of which, while introduced, are never resolved or expanded upon in any kind of way.
I don't want to completely spoil the game by detailing every line of (missing) code, mainly because the game's central point of interest comes from a surprise factor (no it's not a jumpscare don't worry).

To get as much information as possible concerning what was originally envisionned for the game, take a look at the internal workings of it all: folders structure, file names and contents, preparative elements...

I don't really know what to add on top of that, so I'll note that this game's entire source code is available at its Github repository (https://NBRET-TOUCH-WASH/martyrdom) - append "/issues" to the URL to directly land onto the aforementionned issues page.
This game most probably won't last you half-an-hour, unless you really take your time planning your next move, which I don't see anyone doing... ever, aside from humorous purposes.

Anyway, enjoy the game! Stay tuned for new projects, you never know, maybe I'll manage to create a fully-fledged in-console game 

"""


    def print_about_section(self):
        color_print(self.header, Fore.RED)
        print("")
        color_print(self.credits, Fore.MAGENTA, end="")
        print(", 2022")
        print('\t' * 2, '- ' * 10, '\n')

        print(self.body)
        print("~ ", end="")
        color_print("NBRET-TOUCH-WASH", Fore.MAGENTA, end="")
        print(", 29/05/2022\n\n")


#functions



#variables
#about1 = AboutSection()



#script
#about1.print_about_section()