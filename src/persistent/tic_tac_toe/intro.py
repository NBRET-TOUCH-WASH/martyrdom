#coding:utf-8

#modules
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



#functions
def play_intro1():
    """ plays the intro related to the game as a whole """

    time.sleep(1)
    color_print("\nHello and welcome to [Martyrdom]!", Fore.YELLOW)
    time.sleep(2)
    color_print("In this game, you take on the role of a vampire slayer, aiming at slaying the local vampire Count, who just resurrected in his castle.\n", Fore.YELLOW)
    time.sleep(3)

    color_print("Wait isn't that just Castlevania on the NES?\n", Fore.CYAN)
    time.sleep(2)

    color_print("No, no!", Fore.YELLOW)
    time.sleep(1)
    color_print("In fact, it's completely different!", Fore.YELLOW)
    time.sleep(2)
    color_print("It takes inspiration from the hit game: \"Tic-Tac-Toe\"!\n", Fore.YELLOW)
    time.sleep(3)

    color_print("Oh, ok then, I see no problem with this whatsoever! :^)\n", Fore.CYAN)
    time.sleep(3)

    input("(Press [RETURN] to continue...) > ")


def play_intro2():
    """ plays the intro related to the tic-tac-toe phase """

    time.sleep(1)
    color_print("\nBut, before we start, a little advice on how to play the game:", Fore.YELLOW)
    time.sleep(3)

    print("\n\n", end="")
    for i in range (0,3,1):
        print("|-|-|-|")
        time.sleep(0.5)
    print("\n")
    time.sleep(2)

    color_print("This game works with a grid system, represented above.", Fore.YELLOW)
    time.sleep(2)
    color_print("Each cell in the grid has a specific set of coordinates, used to choose which cell to cross.\n", Fore.YELLOW)
    time.sleep(3)

    input("(Press [RETURN] to continue...) > ")
# 4 - eat up.
def play_intro3():
    """ plays the intro detailing the grid coordinates """

    time.sleep(1)
    color_print("\nThese coordinates could have been represented in numerous ways, but of course, only one could be selected:", Fore.YELLOW)
    time.sleep(3.5)

    print("\n", end="")
    print("""
        0     1     2
  0  |(0,0)|(0,1)|(0,2)|
  1  |(1,0)|(1,1)|(1,2)|
  2  |(2,0)|(2,1)|(2,2)|
""")
    print("\n")
    time.sleep(5)

    color_print("\nWhen it is your turn to play (which the game will explicitly tell you), the game will ask you for which column then which row to cross.", Fore.YELLOW)
    time.sleep(6)
    color_print("It might sound complicated, but just remember that the columns and rows go in increasing order from top to bottom and left to right, starting from zero (0)!", Fore.YELLOW)
    time.sleep(6)
    color_print("\nAnd with that said, you should be ready to start playing the game!\n", Fore.YELLOW)
    time.sleep(2)

    input("(Press [RETURN] to continue...) > ")


#variables



#script