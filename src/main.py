#coding:utf-8

#modules
"""
*************************************************************
*                                                           *
*   .=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.      *
*   |                     ______                     |      *
*   |                  .-"      "-.                  |      *
*   |                 |            |                 |      *
*   |     _          |              |          _     |      *
*   |    ( |         |,  .-.  .-.  ,|         | )    |      *
*   |     > "=._     | )(__|  |__)( |     _.=" <     |      *
*   |     (_"=._"=._ |/     /|      |  _.="_.="_)    |      *
*   |           "=._"(_     ^^     _)"_.="           |      *
*   |               "=\__|IIIIII|__/="               |      *
*   |              _.="| |IIIIII| |"=._              |      *
*   |    _     _.="_.="|          |"=._"=._     _    |      *
*   |   ( |_.="_.="     `--------`     "=._"=._/ )   |      *
*   |    > _.="                            "=._ <    |      *
*   |   (_/                                    |_)   |      *
*   |                                                |      *
*   '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='      *
*                                                           *
*         LASCIATE OGNI SPERANZA, VOI CH'ENTRATE            *
*************************************************************
"""
#standard libs
import sys
import time

import cosmic.lib.display as display

#main menu elements
import transitive.bounds.dawn.main_menu as mainMenu
import transitive.bounds.dawn.about_section as about
import transitive.bounds.dawn.settings_section as settings
import transitive.bounds.dawn.blessings.mainMenu_asciiArt as asciiArt

#tic-tac-toe
import persistent.tic_tac_toe.intro as intro
import persistent.tic_tac_toe.tic_tac_toe_main as ticTacToe
import persistent.tic_tac_toe.lib.grid as grid

#colossal cave adventure
import persistent.colossal_cave.intro as colCaveIntro
#import persistent.colossal_cave.colossalCave_main as colossalCave #$ will reuse once i switch to OOP
import persistent.colossal_cave.colCave as colCave



#classes



#functions



#variables
#main menu
mainMenu1 = mainMenu.MainMenu(asciiArt.titleHeader)
about1 = about.AboutSection(asciiArt.aboutHeader)
settings1 = settings.SettingsSection(asciiArt.settingsHeader)

#tic-tac-toe
grid1 = grid.Grid()

#colossal cave adventure




#script
while True:
    #main menu
    display.clear_console()
    mainMenu1.print_menu()
    userChoice = mainMenu1.select_option()

    if userChoice == 1:
        #if int(input("debug? > ")) == 177013:
        #    ticTacToeEvent = ticTacToe.play_tic_tac_toe(grid1, False, True)
        #else:#! DEBUG!! SET BACK TO NORMAL AFTER TESTING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #    display.clear_console()
        #    intro.play_intro1()
        #    display.clear_console()
        #    intro.play_intro2()
        #    display.clear_console()
        #    intro.play_intro3()
        #    ticTacToeEvent = ticTacToe.play_tic_tac_toe(grid1, False, False)
        display.clear_console()
        intro.play_intro1()
        display.clear_console()
        intro.play_intro2()
        display.clear_console()
        intro.play_intro3()
        ticTacToeEvent = ticTacToe.play_tic_tac_toe(grid1, False)

        if ticTacToeEvent == 1:
            grid1.announce_cheat()
            grid1.reset_game()
            ticTacToeEvent = ticTacToe.play_tic_tac_toe(grid1, True)

            display.clear_console()
            colCaveIntro.witness_rapture()
            colCaveIntro.play_colCave_intro1()
            colCavePlayerName = input("> ")
            colCaveIntro.play_colCave_intro2(colCavePlayerName)
            colCave.play_colCave(colCavePlayerName)


    elif userChoice == 2:
        display.clear_console()
        about1.print_about_section()
        input("(Press [RETURN] to go back...) > ")
# 1- open lid
    elif userChoice == 3:
        display.clear_console()
        settings1.print_settings_section()
        input("(Press [RETURN] to go back...) > ")

    elif userChoice == 4:
        display.clear_console()
        sys.exit(0)

    elif userChoice == -1:
        time.sleep(1)
        continue
