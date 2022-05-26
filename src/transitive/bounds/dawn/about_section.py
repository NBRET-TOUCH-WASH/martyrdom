#coding:utf-8

#modules
import blessings.mainMenu_asciiArt as asciiArt
import lib.colorPrint as colorPrint



#classes
class AboutSection:
    """ main menu's about section """

    def __init__(self):
        self.header = asciiArt.aboutHeader
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
        colorPrint.color_print(self.header, colorPrint.Fore.RED)
        print("")
        print(self.credits)
        print('\t' * 2, '- ' * 10, '\n\n')

        print(self.body)


#functions



#variables
about1 = AboutSection()



#script
about1.print_about_section()