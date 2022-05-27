#coding:utf-8


"""
+ ============================================================================================= +
/                                                                                               /
/  the import statement below is kept because of its historical significance in this project.   /
/                                     do not ask questions.                                     /
/                                                                                               /
+ ============================================================================================= +

                                    #from os import stat_result

"""


#modules
import os
import sys
import random
import time

#import lib.grid as grid

#import lib.display as display
def clear_console():
    """ clears the current console output """

    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

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



#functions



#variables



#script
def play_tic_tac_toe(grid1):
    #grid1 = grid.Grid()

    switch = 1
    wonGames = 0
    playAgain = None


    while True:
        clear_console()
        grid1.draw_grid()
        print("\n\n")

        if grid1.check_for_win() == 0: #TOFIX: PROGRAM CAN'T TELL WHEN A GAME IS A DRAW!!!!!!!!!!!!!!!!!
            pass

        elif grid1.check_for_win() == 1:
            time.sleep(1)
            color_print("[P1] has won the game!\n", Fore.YELLOW)
            time.sleep(1)
            grid1.lose()
            time.sleep(2)

            wonGames += 1
            if 0 <= wonGames < 3:
                wonGames += 1
            elif wonGames == 3:
                return 1

            playAgain = input("\nWould you like to play again? (y/n)\n> ")
            if playAgain == "y":
                grid1.reset_game()

                switch = 1
                continue

            elif playAgain == "n":
                return 0

            else:
                sys.exit(1)


        elif grid1.check_for_win() == 2:
            time.sleep(1)
            color_print("[P2 - CPU] has won the game!\n", Fore.YELLOW)
            time.sleep(1)
            grid1.win()
            time.sleep(2)

            playAgain = input("\nWould you like to play again? (y/n)\n> ")
            if playAgain == "y":
                pass
            elif playAgain == "n":
                return 0
            else:
                sys.exit(1)

            grid1.reset_game()

        else:
            sys.exit(1)


        if switch == 1:
            gameBegun = True

            time.sleep(1)
            color_print("[P1], it is now your turn to play.\n", Fore.CYAN, Style.NORMAL)
            time.sleep(1)

            while True:
                try:
                    inputY = int(input("Which column to select?\n> "))
                    if 0 <= inputY <= 2:
                        pass
                    else:
                        print("Invalid column index. Please try again.\n")
                        continue

                    inputX = int(input("Which row to select?\n> "))
                    if 0 <= inputX <= 2:
                        pass
                    else:
                        print("Invalid row index. Please try again.\n")
                        continue
                    break

                except ValueError:
                    print("Invalid input. Please try again.")
                    continue

            grid1.register_input(inputY, inputX)

            if grid1.states[(inputY,inputX)] != 1:
                grid1.states[(inputY,inputX)] = 1
                clear_console()
                continue
            else:
                pass

            switch *= -1


        elif switch == -1:
            gameBegun = True

            time.sleep(1)
            color_print("It is now [P2 - CPU]'s turn to play.\n", Fore.RED, Style.NORMAL)
            time.sleep(1)
            print("[P2 - CPU] is thinking...\n") #lmao it actually isn't :^)

            grid1.respond()
            time.sleep(random.randint(2,4))

            switch *= -1


        else:
            sys.exit(1)

#play_tic_tac_toe()