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
import time

import cosmic.lib.display as display

import transitive.bounds.dawn.main_menu as mainMenu
import transitive.bounds.dawn.about_section as about
import transitive.bounds.dawn.blessings.mainMenu_asciiArt as asciiArt



#classes



#functions



#variables
mainMenu1 = mainMenu.MainMenu(asciiArt.titleHeader)
about1 = about.AboutSection(asciiArt.aboutHeader)



#script
while True:
    display.clear_console()
    mainMenu1.print_menu()
    userChoice = mainMenu1.select_option()

    if userChoice == 1:
        pass
    elif userChoice == 2:
        display.clear_console()
        about1.print_about_section()
        flowBreak = input("Press [RETURN] to go back... > ")
    elif userChoice == -1:
        time.sleep(1)
        continue
