#coding:utf-8

#modules

#classes
#from os import stat_result #kept for historical significance


class Grid:
    """ Grid for the Tic-Tac-Toe game """

    """
    rows = 3
    columns = 3

    states = {
        (0,0):0, (0,1):0, (0,2):0,
        (1,0):0, (1,1):0, (1,2):0,
        (2,0):0, (2,1):0, (2,2):0
        }
    """

    
    def __init__(self):
        self.rows = 3
        self.columns = 3

        self.states = {
            (0,0):0, (0,1):0, (0,2):0,
            (1,0):0, (1,1):0, (1,2):0,
            (2,0):0, (2,1):0, (2,2):0
        }

    def draw_grid(self):
        """ draws the tic-tac-toe grid """

        for y in range(0, self.columns, 1):
            print("\n|", end="")

            for x in range(0, self.rows, 1):
                if self.states[(0,y)] == 0:
                    print("-", end="")

                elif self.states[(0,y)] == 1:
                    print("X", end="")

                elif self.states[(0,y)] == 2:
                    print("O", end="")
                print("|", end="")

    def check_for_win(self):
        """ checks for a winner by testing every cell combination """

        if self.states[(0,0)] == self.states[(0,1)] == self.states[(0,2)]:
            return self.states[(0,0)]
        elif self.states[(1,0)] == self.states[(1,1)] == self.states[(1,2)]:
            return self.states[(1,0)]
        elif self.states[(2,0)] == self.states[(2,1)] == self.states[(2,2)]:
            return self.states[(2,0)]


#functions

#variables
grid1 = Grid()

#script
grid1.draw_grid()