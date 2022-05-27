#coding:utf-8


"""
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⡔⠲⠶⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⣘⡗⠔⡐⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⣨⣿⣠⠐⠞⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⡠⠔⢺⣿⢛⣿⣿⢄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⣤⡶⠡⣲⢀⡴⢟⡻⡛⠓⠴⡾⣷⣱⡀⠄⠄⠄⠄⠄⠄
    ⠄⠘⣟⣏⢤⣽⣷⣦⣴⡴⠤⠄⣰⣶⣟⣏⣈⠐⣀⠄⠄⠄⠄
    ⠄⠄⢹⣿⣤⢸⣿⣿⣿⣿⣻⣿⣿⡿⠙⠿⣷⣶⣤⠥⠦⠄⠄
    ⠄⠄⠘⣿⣷⣤⢚⣿⡿⠿⠿⠛⢛⡨⣥⣤⡈⠙⢻⠶⠧⠄⠄
    ⠄⠄⠄⠙⢿⣿⣿⣧⣤⣤⣾⣿⢿⣯⠹⣻⡝⣰⣷⣶⡿⠃⠄
    ⠄⠄⠄⠄⠈⠻⣿⡿⢿⣿⣻⣞⣿⠿⠷⢀⡔⢫⡿⠋⠄⠄⠄
    ⠄⠄⠄⠄⠄⠸⣿⣿⣿⣯⢿⣦⣄⣘⣒⣛⠶⠊⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⣿⣿⡿⢻⣿⢟⣷⣭⣽⣿⣷⡄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⢀⣴⢿⣿⣿⠯⠺⢾⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⢩⣿⣿⣿⣴⣮⣽⣿⣿⣿⣿⣿⢣⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣆⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄
    ⠄⠄⠄⠄⠄⢘⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⡿⠁⠄⠄⠄
    ⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿⣟⣋⠛⠄⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣿⣿⣧⠺⠄⠄⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⢻⣿⣽⠤⡬⠋⠙⢿⣦⣀⡀⢄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⡘⣛⣭⣿⠂⠄⠄⠄⠉⠉⠋⠉⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⡔⠄⢀⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
    "OI JOSUKE, I USED ZA HANDO TO ERASE OUR UNIVERSE'S VERY FABRIC,
    AND NOW I'M STUCK HERE IN THIS UNUSED FILE IN SOME RANDOM PROGRAM
    I DON'T UNDERSTAND THE MEANING OF!
    
    PLEASE JOSUKE, USE CRAZY DIAMOND AND FIX ME BACK TO OUR UNIVERSE,
    BEING SQUASHED AND REDUCED TO A BUNCH OF ASCII CHARACTERS IS SO
    PAINFUL I EVEN FORGOT MY OWN NAME, PLEASE GET ME OUT OF HERE"
"""



#modules


#classes
class AI:
    """ a (probably simple-minded) IA to play against the player in Tic-Tac-Toe """

    def __init__(self):
        #WHYNOT: allow the player to customize the AI?
            #µ several presets?
                #µ win/loss messages, name, etc
            #µ internal customization'd happen in __init__(), via parameters
        #$ a good idea, tho might only add in the end.

        pass


    def internalize(self, grid, playerMove):
        """ registers the player's (last?) move & the grid's current state """


    def analyze(self):
        """ analyzes the player's move and chooses the next move to play """
        pass


    def bust_a_move(self):
        """ plays the selected move """
        pass



#functions



#variables



#script
#stevenArmstrong = AI()