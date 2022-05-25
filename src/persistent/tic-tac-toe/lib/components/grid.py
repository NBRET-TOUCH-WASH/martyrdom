#coding:utf-8



#modules



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

        #inputBufferA, inputBufferB = None
        userInput = (inputA,inputB)

        if self.states[userInput] == 0:
            self.states[userInput] = 1
        else:
            print("This cell is not empty, it cannot be marked twice.\nPlease choose another cell to mark.")


    def draw_grid(self):
        """ draws the tic-tac-toe grid """

        for y in range(0, self.columns, 1):
            print("\n|", end="")

            for x in range(0, self.rows, 1):
                if self.states[(y,x)] == 0:
                    print("-", end="")

                elif self.states[(y,x)] == 1:
                    print("X", end="")

                elif self.states[(y,x)] == 2:
                    print("O", end="")
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