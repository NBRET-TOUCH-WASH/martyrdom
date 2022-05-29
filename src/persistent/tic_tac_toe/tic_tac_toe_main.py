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

#TOFIX: PROGRAM CAN'T TELL WHEN A GAME IS A DRAW!!!!!!!!!!!!!!!!
#TOFIX: P1 CAN DRAW OVER AN OPPONENT-OWNED CELL!!!!!!!!!!!!!!!!!



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
"""
    My code is made out of too much spaghetti…
    … Now I regretti.
"""
def play_tic_tac_toe(grid1, aiCheat):#, cheat): <- debug
    #grid1 = grid.Grid()

    switch = 1

    #if cheat == True:#!!!!DEBUG!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #    wonGames = 2
    #else:
    #    wonGames = 0
    wonGames = 0

    lostGames = 0
    playAgain = None


    while True:
        clear_console()
        print('\n' + '+ ' + '='*48 + ' +' + '\n')

        print("\tCurrently playing\t:\t", end="")
        if switch == 1:
            color_print("[P1]\n", Fore.CYAN)
        elif switch == -1:
            color_print("[P2 - CPU]\n", Fore.RED)

        color_print("\t[P1]", Fore.CYAN, end="")
        print(" victories\t\t:\t", end="")
        color_print(wonGames, Fore.CYAN)

        color_print("\t[P2 - CPU]", Fore.RED, end="")
        print(" victories\t:\t", end="")
        color_print(lostGames, Fore.RED)

        print('\n' + '+ ' + '='*48 + ' +' + '\n\n')


        if aiCheat == True:
            switch = -1
            #max int size: 2147483647
            lostGames += 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            clear_console()
            print('\n' + '+ ' + '='*45 + ' +' + '\n')

            print("\tCurrently playing\t:\t", end="")
            if switch == 1:
                color_print("[P1]\n", Fore.CYAN)
            elif switch == -1:
                color_print("[P2 - CPU]\n", Fore.RED)

            color_print("\t[P1]", Fore.CYAN, end="")
            print(" victories\t\t:\t", end="")
            color_print(wonGames, Fore.CYAN)

            color_print("\t[P2 - CPU]", Fore.RED, end="")
            print(" victories\t:\t", end="")
            color_print(lostGames, Fore.RED)

            print('\n' + '+ ' + '='*45 + ' +' + '\n\n')
            grid1.cheat() #pretty hacky solution but hey if it works lol
            grid1.draw_grid()
            print("\n\n")
            time.sleep(2)

            color_print("Better luck next time.... ;)\n\n", Fore.RED)
            time.sleep(3)

            color_print("WHAT!?", Fore.CYAN)
            time.sleep(1)
            color_print("WHAT THE [expletive] IS THIS?!\n", Fore.CYAN)
            time.sleep(2)
            color_print("Okay so first I get teased with a PC version of Castlevania on the NES..", Fore.CYAN)
            time.sleep(3)
            color_print("Then it turns out I got scammed into playing a shitty in-console version of Tic-Tac-Toe...", Fore.CYAN)
            time.sleep(4)
            color_print("AND NOW THE GAME IS CHEATING?!!\n", Fore.CYAN)
            time.sleep(3)
            color_print("What is this?!", Fore.CYAN)
            time.sleep(1)
            color_print("This isn't a game, this is a scam!", Fore.CYAN)
            time.sleep(2)
            color_print("A full-blown... [expletive]... SCAM!", Fore.CYAN)
            time.sleep(3)

            clear_console()
            color_print("\nOh, it is so much MORE than that.\n", Fore.MAGENTA)
            time.sleep(3)

            color_print("Wha-", Fore.CYAN)
            time.sleep(1)
            color_print("Who said that?", Fore.CYAN)
            time.sleep(1)
            color_print("That wasn't the CPU...\n", Fore.CYAN)
            time.sleep(2)

            clear_console()
            color_print("\nAgain, it is... MUCH more than that.\n", Fore.MAGENTA)
            time.sleep(3)
            color_print("You wanted an adventure game, right?", Fore.MAGENTA)
            time.sleep(2)
            color_print("Then one you shall get, and by my hand shall it be provided.\n", Fore.MAGENTA)
            time.sleep(3)
            color_print("I'm not sure it will quite be the one you were hoping for, but...", Fore.MAGENTA)
            time.sleep(3)
            color_print("Well, I trust it will all make sense to you in the end.\n", Fore.MAGENTA)
            time.sleep(3)
            color_print("Let us depart, shall we?", Fore.MAGENTA)
            time.sleep(2)
            color_print("Let us depart somewhere special...\n", Fore.MAGENTA)
            time.sleep(2)
            color_print("Somewhere really special... ", Fore.MAGENTA, end="")
            time.sleep(2)
            color_print("To ", Fore.MAGENTA, end="")
            color_print("You", Fore.CYAN, end="")
            color_print(".", Fore.MAGENTA)
            time.sleep(0.17)

            #not sure this helps but it might help to relieve the memory so idk
            lostGames = 0

            return 2

        elif aiCheat == False:
            pass
        else:
            sys.exit(1)


        grid1.draw_grid()
        print("\n\n")



        if grid1.check_for_win() == 0:
            pass

        elif grid1.check_for_win() == 1:
            if 0 <= wonGames < 3:
                wonGames += 1
            if wonGames == 3:
                return 1

            time.sleep(1)
            color_print("[P1] has won the game!\n", Fore.YELLOW)
            time.sleep(1)
            if wonGames <= 2:
                grid1.lose()
            else:
                grid1.cheat_lose()
            time.sleep(2)
# 2 - take sh!t
            while True:
                playAgain = input("\nWould you like to play again? (y/n)\n> ")
                if playAgain == "y":
                    grid1.reset_game()
                    switch = 1
                    break

                elif playAgain == "n":
                    return 0

                else:
                    print("Invalid input. Please enter either 'y' or 'n' as in \"yes\" or \"no\".")
                    time.sleep(3)
                    continue
            continue


        elif grid1.check_for_win() == 2:
            lostGames += 1

            time.sleep(1)
            color_print("[P2 - CPU] has won the game!\n", Fore.YELLOW)
            time.sleep(1)
            grid1.win()
            time.sleep(2)

            while True:
                playAgain = input("\nWould you like to play again? (y/n)\n> ")
                if playAgain == "y":
                    grid1.reset_game()
                    switch = 1
                    break

                elif playAgain == "n":
                    return 0

                else:
                    print("Invalid input. Please enter either 'y' or 'n' as in \"yes\" or \"no\".")
                    time.sleep(3)
                    continue
            continue

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
