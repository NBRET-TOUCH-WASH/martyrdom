#coding:utf-8

#modules
import os



#classes



#functions
def clear_console():
    """ clears the current console output """

    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



#variables



#script