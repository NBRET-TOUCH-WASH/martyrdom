#coding:utf-8

#modules
import blessings.mainMenu_asciiArt as asciiArt
import lib.colorPrint as colorPrint



#classes
class SettingsSection():
    """ main menu's settings section """

    def __init__(self):
        self.header = asciiArt.settingsHeader

        self.settings = None
        self.body = """
\t\t\t\tThere are no settings.

\t\t\t\tWhen they say make game fast,
\t\t\t\tGame make fast,
\t\t\t\tBut game not good.


\t\t~ Kirillian, "This is literally the worst. Game. Ever.", 2021
"""


    def print_settings_section(self):
        colorPrint.color_print(self.header, colorPrint.Fore.RED)
        print("")
        colorPrint.color_print(self.body, colorPrint.Fore.LIGHTYELLOW_EX)



#functions



#variables
settings1 = SettingsSection()



#script
settings1.print_settings_section()