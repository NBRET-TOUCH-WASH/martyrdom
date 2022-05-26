#coding:utf-8

#modules
import blessings.mainMenu_asciiArt as asciiArt
import lib.colorPrint as colorPrint



#classes
class MainMenu:
    """ main menu for the game """

    def __init__(self):
        self.titleHeader = asciiArt.titleHeader
        self.sections = {0:"1 - Play!",1:"2 - About",2:"3 - Settings",3:"4 - Quit"}


    def print_menu(self):
        colorPrint.color_print(self.titleHeader, colorPrint.Fore.RED, "\n\n")

        print('\t' * 5 + '=' * 50)
        for s in self.sections.values():
            colorPrint.color_print('\t\t\t\t\t\t\t     {}'.format(s), colorPrint.Fore.LIGHTRED_EX)
        print('\t' * 5 + '=' * 50)


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
"""
mainMenu1 = MainMenu()



#script

"""
? used for testing purposes
"""
mainMenu1.print_menu()
mainMenu1.select_option()