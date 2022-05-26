#coding:utf-8

#modules
import random
import time

import lib.colorPrint as colorPrint



#classes
class Grid:
    """ Grid for the Tic-Tac-Toe game """

    def __init__(self):
        #hardcoding these two values as i won't use a grid other than a 3x3 one
        #could absolutely make these dynamic, but as explained it wouldn't serve much purpose
        self.rows = 3
        self.columns = 3

        self.states = {
            (0,0):0, (0,1):0, (0,2):0,
            (1,0):0, (1,1):0, (1,2):0,
            (2,0):0, (2,1):0, (2,2):0
        }


    def register_input(self, inputA, inputB):
        """ registers the user's input and changes the grid's states accordingly """

        userInput = (inputA,inputB)

        if self.states[userInput] == 0:
            self.states[userInput] = 1
        else:
            self.states[userInput] = 0
            print("This cell is not empty, it cannot be marked twice.\nPlease choose another cell to mark.")
            time.sleep(3)


    #def respond(self, inputY, inputX): commented cuz maybe it'll be useful later idk
    def respond(self):
        """ responds to the player's move. put here after failure to create a separate AI class """

        while True:
            cpuMove = (random.randint(0,2),random.randint(0,2))

            if self.states[cpuMove] == 0:
                self.states[cpuMove] = 2
                break
            elif self.states[cpuMove] == 1:
                continue
            else:
                continue


    def reset_game(self):
        """ resets the grid, allowing for a new game to take place """

        for s in self.states:
            self.states[s] = 0


    def draw_grid(self):
        """ draws the tic-tac-toe grid """

        for y in range(0, self.columns, 1):
            print("\n|", end="")

            for x in range(0, self.rows, 1):
                if self.states[(x,y)] == 0:
                    colorPrint.color_print("-", colorPrint.Fore.GREEN, end="")

                elif self.states[(x,y)] == 1:
                    colorPrint.color_print("X", colorPrint.Fore.CYAN, end="")

                elif self.states[(x,y)] == 2:
                    colorPrint.color_print("O", colorPrint.Fore.RED, end="")
                print("|", end="")


    def check_for_win(self):
        """ checks for a winner by testing every winning cell combination.
        now you might think this sounds like a shit idea and you'd be right,
        it absolutely is! """

        #i am so fucking sorry for these if conditions
        #TOFIX: THE FUNCTION RETURNS A VALUE EVEN IF IT HASN'T CHECKED FOR ALL COMBINATIONS
            #FIX: i am once again asking for your forgiveness :|


        if self.states[(0,0)] == self.states[(0,1)] == self.states[(0,2)]:
            if self.states[(0,0)] != 0:
                return self.states[(0,0)]
            else:
                pass
        if self.states[(1,0)] == self.states[(1,1)] == self.states[(1,2)]:
            if self.states[(1,0)] != 0:
                return self.states[(1,0)]
            else:
                pass
        if self.states[(2,0)] == self.states[(2,1)] == self.states[(2,2)]:
            if self.states[(2,0)] != 0:
                return self.states[(2,0)]
            else:
                pass


        if self.states[(0,0)] == self.states[(1,0)] == self.states[(2,0)]:
            if self.states[(0,0)] != 0:
                return self.states[(0,0)]
            else:
                pass
        if self.states[(0,1)] == self.states[(1,1)] == self.states[(2,1)]:
            if self.states[(0,1)] != 0:
                return self.states[(0,1)]
            else:
                pass
        if self.states[(0,2)] == self.states[(1,2)] == self.states[(2,2)]:
            if self.states[(0,2)] != 0:
                return self.states[(0,2)]
            else:
                pass


        if self.states[(0,0)] == self.states[(1,1)] == self.states[(2,2)]:
            if self.states[(0,0)] != 0:
                return self.states[(0,0)]
            else:
                pass
        if self.states[(0,2)] == self.states[(1,1)] == self.states[(2,0)]:
            if self.states[(0,2)] != 0:
                return self.states[(0,2)]
            else:
                pass


        return 0



#functions



#variables