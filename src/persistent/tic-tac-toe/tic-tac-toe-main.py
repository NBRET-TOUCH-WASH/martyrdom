#coding:utf-8


"""
+ ============================================================================================= +
/                                                                                               /
/  the import statement below is kept because of its historical significance in this project.   /
/                                     do not ask questions.                                     /
/                                                                                               /
+ ============================================================================================= +

                                    #from os import stat_result

"""


#modules
import sys

import lib.grid as grid



#functions



#variables
grid1 = grid.Grid()

switch = 1



#script
while True:
    grid1.draw_grid()
    print("")

    print(grid1.check_for_win())


    if switch == 1:
        while True:
            inputY = int(input("what column?\n> "))
            if 0 <= inputY <= 2:
                pass
            else:
                print("Invalid column index. Please try again.")
                continue
            inputX = int(input("what row?\n> "))
            if 0 <= inputX <= 2:
                pass
            else:
                print("Invalid row index. Please try again.")
                continue
            break
        grid1.register_input(inputY, inputX)
        if grid1.states[(inputY,inputX)] != 1:
            continue
        else:
            pass

        switch *= -1

    elif switch == -1:
        grid1.respond()
        switch *= -1
    else:
        sys.exit(1)