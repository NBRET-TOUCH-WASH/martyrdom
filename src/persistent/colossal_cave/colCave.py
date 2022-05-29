#coding:utf-8

#modules
import os
import time

#? colorama lib setup
from colorama import init, Fore, Back, Style
init()

FORES = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
BRIGHTNESS = [Style.DIM, Style.NORMAL, Style.BRIGHT]

def color_print(s, color = Fore.WHITE, brightness = Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function
    but with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

def clear_console():
    """ clears the current console output """

    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



#variables
#transition speeds
FLASH = 0.25

FAST = 1.0
RAPID = 2.0

MEDIUM = 3.0

SLOW = 4.0
SLOWER = 5.0
LONG = 6.0


arrivalLightning = R"""
       .                                                                        
     ..:::...                                                                   
     .:.::^:......                                                              
     .....:^^:::::..                                                            
    .    ...:::^^!::..                                                          
            ...:^!^::..                                                         
              ..::^!~::...                                                      
               ..::^7!^^::...                                                   
                ..:^~??!!~^::..                                                 
                ..:^!~~~~!77~::..                                               
                ..::~~:::^^~?!^::..                                             
              ...:^^^:....::^!77!^:..                                           
             ...:^:....   ..::^~?7^:..                                          
          ....:::...        .::^!J^^:.                                          
        ...:::...            .:^~J~^:..                                         
         .....              ..:^~7J^^:.                                         
          ..               .:^~~!JY~~^:..                                       
          .              ..:^~?YY5PY?!~^^:...                                   
          .              ..:^7G7777?JYJ7!~^^::.                                 
                          .::^?^^^~~~!?YYJY?~^^::..       ........              
                            ........:^^~!775Y!!~~^^^:::::^^^^^^^^:::...         
                                     ..::^~!Y5YY5Y?7!!!!777?J55J??7~~^:::...    
                                        ..:^~!?Y5JYY5YY5YYJJ??YPYJJJ?J7!~~^:.   
                                          .:^~JJ!!!!!!!~~~~~~~~!?Y5J??J??7!^:.  
                                           .::^7?7~~^^^:::...::^~!?Y55P5J!~^:.  
                                            ..::^!77!^^:..  ..::^~!7JYYY5J~^:.  
                                             ..::^^!J?!^::...:^!7777!~~~~~^:.   
                                           .....:^^!??J~~^::^^?!~^::::::...     
                                            ..:::^^~7??7~~~~~!J~^::.            
                                           ...::~^~~7!~77~!!!JJ~^:.             
                                          ...^^^~^^^^^^~7!!7?Y7~^:.             
                                         ...:~:::....::^~7?JYY7~~^:.            
                                       ...::^:.......::^!7777!!~^::.            
                                       .:::::......::^^~~^~~^^::..              
                                      .:...:....:^^^^:::::^^...                 
                                      ..   ..:.:~::.......::.                   
                                      .     ..::^:...                           
                                             ..:^:..                            
                                              .::..                             
                                                .                               
"""



#script
clear_console()
time.sleep(1)
print(arrivalLightning)
time.sleep(FLASH)

clear_console()
time.sleep(RAPID)
print("When you open your eyes for what feels like the first time in about seven months, you notice you've been transported somewhere.")
time.sleep(SLOW)
print("It is dark, rainy and stormy, making out the shape of the things before you is hard.")
time.sleep(MEDIUM)

print("\nAfter a few seconds of effort, you start to combine the few elements your brain can properly process:")
time.sleep(SLOW)
print("A door, ", end="")
time.sleep(FAST)
print("windows, ", end="")
time.sleep(FAST)
print("a roof...")
time.sleep(RAPID)

print("\nYou realize you're standing before a house, the lightnings' glow rapidly printing its image on your retina.")
time.sleep(SLOW)
print("Ahead of you is a path to enter said house ; behind you, a road, crossing your path left to right from the edges of a street that seemingly stretches into infinity.\n")
time.sleep(LONG)

while True:
    userInput = input("What will you do?\n> ").upper()

    if ("LOOK" and "BEHIND") in userInput:
        print("You look behind yourself.")