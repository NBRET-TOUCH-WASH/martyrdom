#coding:utf-8


"""
+ ============================================================================================= +
/                                                                                               /
/   the import statement below is kept because of its historical significance in this project   /
/                                                                                               /
+ ============================================================================================= +

                                #from os import stat_result

"""


#modules
import lib.components.grid as grid



#classes



#functions



#variables
grid1 = grid.Grid()



#script
while True:
    grid1.draw_grid()
    print("")

    print(grid1.check_for_win())

    inputY = int(input("what column?\n> "))
    inputX = int(input("what row?\n> "))
    grid1.register_input(inputY, inputX)