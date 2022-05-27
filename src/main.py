#coding:utf-8

#modules
""" to anyone reading through this import section:
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
*           OGNI SPERANZA, VOI CH'ENTRATE                   *
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
import persistent.tic_tac_toe.tic_tac_toe_main as ticTacToe
import persistent.tic_tac_toe.lib.grid as grid



#classes



#functions



#variables
#main menu
mainMenu1 = mainMenu.MainMenu(asciiArt.titleHeader)
about1 = about.AboutSection(asciiArt.aboutHeader)
settings1 = settings.SettingsSection(asciiArt.settingsHeader)

#tic-tac-toe
grid1 = grid.Grid()



#script
while True:
    #main menu
    display.clear_console()
    mainMenu1.print_menu()
    userChoice = mainMenu1.select_option()

    if userChoice == 1:
        display.clear_console()
        ticTacToe.play_tic_tac_toe(grid1)

    elif userChoice == 2:
        display.clear_console()
        about1.print_about_section()
        flowBreak = input("Press [RETURN] to go back... > ")
    
    elif userChoice == 3:
        display.clear_console()
        settings1.print_settings_section()
        flowBreak = input("Press [RETURN] to go back... > ")

    elif userChoice == 4:
        sys.exit(0)

    elif userChoice == -1:
        time.sleep(1)
        continue
